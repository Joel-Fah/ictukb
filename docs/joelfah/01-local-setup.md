# 01. Local knowledge base (Phase 1)

**Purpose:** get a complete copy of the ICT University knowledge base running on the laptop (documents cut into
chunks, embedded, stored in a searchable database) so that a question returns the right passages **with the
network turned off** and without any cloud key. Phase 2 builds the chatbot on top of this.

**Result in short:** 110 documents (77 from `content/` + 33 website pages) in 733 chunks; the right document is in
the top 5 for 94% of the golden questions we cover; a search takes about 5 s from a cold start; no network traffic
leaves the machine. Two weak spots: unanswerable questions about covered topics, and French questions.

Machine: i7-10710U (6 cores, AVX2), 15 GiB RAM, no GPU, Ubuntu 24.04 base. See [00-inspection.md](00-inspection.md).

---

## Step 1. Docker without Docker Desktop

**What:** run PostgreSQL + pgvector in a container using the system Docker Engine.

**Why:** the repo's `docker/docker-compose.yml` already defines the exact database image (`pgvector/pgvector:pg16`).
Using it means our database behaves like everyone else's, and nothing is installed on the host system. Docker Desktop
was avoided because on Linux it runs a virtual machine that holds on to RAM.

**Problem found:** Docker was installed and running, but the `docker` command was pointed at Docker Desktop (not
running), and our user wasn't allowed to use the system Docker socket.

**How (one-time, needs sudo):**
```bash
docker context use default            # talk to the system Docker Engine instead of Docker Desktop
sudo usermod -aG docker $USER         # allow our user to use Docker (note: this group is root-equivalent)
# log out and back in, then check:
docker ps                             # an empty table means it works
```
A terminal opened before the group change still says "permission denied"; `sg docker -c "docker ps"` works there.

## Step 2. Ollama (for Phase 2)

**What:** Ollama is a local server that loads a language model and answers on `http://localhost:11434`.

**How:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:3b
```
If `ollama list` says "could not connect to ollama server": `sudo systemctl enable --now ollama`.

## Step 3. Python environment

**What:** an isolated Python environment with the repo's own code and its optional local-embedding package.

**Why:** `.[dev,local-embeddings]` are extras the repo already declares, so we add **no new dependency**.
`local-embeddings` installs `fastembed`, which runs the e5 embedding model with ONNX Runtime on the CPU.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev,local-embeddings]"
```
Installed versions: fastembed 0.9.1, onnxruntime 1.32.0, psycopg 3.3.9.

## Step 4. Configuration (`.env`)

**What:** the settings file the `ictkb` tools read. It's in `.gitignore` and is never committed.

**Why each line matters:**

```ini
DATABASE_URL=postgresql://ictkb:ictkb@localhost:5432/ictkb   # the local container
KB_ENV=staging                 # also index draft documents (production indexes only verified ones)
EMBEDDING_PROVIDER=fastembed   # local e5. The repo default "worker" calls a Cloudflare service and needs an admin token
KB_WORKER_URL=                 # blank: no cloud embedding
COHERE_API_KEY=                # blank: no cloud embedding
MIN_SIMILARITY=0.81            # confidence threshold, calibrated for e5 in Step 9
REQUIRE_API_KEY=false          # only matters if the local API server is ever started
ADMIN_TOKEN=
CLOUDINARY_CLOUD_NAME=         # blank: attachment links are not generated, nothing is uploaded
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

## Step 5. Keep the embedding model out of `/tmp`

**Problem found:** fastembed stores downloaded models in `/tmp/fastembed_cache` unless told otherwise. Ubuntu empties
`/tmp` at every boot, so the 2.2 GB model would be downloaded again after each restart, and the "works offline" goal
would fail after the first reboot. Putting the setting in `.env` doesn't help: the repo's settings loader reads
`.env` for its own settings but doesn't pass it on to the environment, and that's where fastembed looks.

**How:** in every terminal where `ictkb` runs:
```bash
export FASTEMBED_CACHE_PATH=$HOME/.cache/fastembed
```
(Our chatbot will set this itself. Reported upstream: [#3](https://github.com/Egbemichel/ictukb/issues/3).)

**Result:** the first use downloaded `intfloat/multilingual-e5-large` (2.1 GB on disk). On our connection, shared with
the Ollama download, this took **45 minutes**; it's a one-time cost. Loading the model and embedding one query
peaked at **1.6 GB RAM**.

## Step 6. Start the database and create the tables

**What:** `migrate` runs the SQL files in `db/migrations/`, which create the `documents` and `chunks` tables, the
1024-dimension `vector` column, and the full-text (keyword) index.
`validate` checks every Markdown document against the schema (front matter fields, file names, placeholders,
email domains).

```bash
docker compose -f docker/docker-compose.yml up -d db       # only the database, not the API
ictkb migrate     # applied: 001_init.sql, 002_notes_origin.sql, 003_private_origin.sql, 004_wa_state.sql
ictkb validate    # 77 documents checked: 46 verified, 31 other, 0 errors
```
`validate` printed two warnings about phone numbers in `campus-location.md` and `erp-support.md`. They're existing
content; someone with the source should confirm they're official office lines.

Security note: the compose file publishes port 5432 on every network interface with the password `ictkb`, so on
shared Wi-Fi others could connect. Reported upstream: [#5](https://github.com/Egbemichel/ictukb/issues/5).

## Step 7. Index the documents

**What happens inside `ictkb index`:**
1. Read every document in `content/` and keep those allowed in this environment (staging: verified + draft).
2. Cut each document into chunks at its Markdown headings (at most about 380 tokens). Each chunk starts with the
   document title and heading path, so a retrieved chunk makes sense on its own. Tables are split by rows with the
   header repeated.
3. Embed each chunk with e5 (prefixed `passage:`; questions are prefixed `query:`, as e5 expects).
4. Store the chunks and vectors. A hash of each document's content is stored too, so re-running `index` only
   re-embeds documents that changed.
5. Record the model name in `kb_meta`. If someone later indexes with a different model, the tool refuses instead of
   silently mixing incompatible vectors.

```bash
/usr/bin/time -v ictkb index
# [staging] inserted=77 updated=0 unchanged=0 deleted=0 skipped_not_eligible=0
```
**Result:** 77 documents (46 verified, 31 draft), **241 chunks**, in **4 min 44 s**, peak RAM **4.4 GB** (embedding
works in batches, so it needs more than a single query). Close browsers during indexing on an 8 GB machine.

## Step 8. Add the university website (one-time crawl)

**Why:** many golden questions expect pages from the university website (`web-*` documents: programme pages, entry
requirements, academic calendar). They aren't in `content/`.

**How it works:** `ictkb crawl` reads the website's WordPress REST API (`https://ictuniversity.org/wp-json/wp/v2`),
follows `robots.txt` (including its 20-second delay between requests), skips pages listed as useless in
`sources/website.yml`, keeps recent news only, converts pages to Markdown, and indexes them like the other documents.
This is the only network use besides downloading models, and it contacts only the university's own site.

```bash
ictkb crawl --dry-run --out data/web-snapshot   # 33 pages written, 2 min 13 s (data/ is git-ignored)
/usr/bin/time -v ictkb crawl                    # inserted=33, 6 min 56 s, peak RAM 2.35 GB
```
The dry run let us see the 33 pages before indexing them. One page a golden question expects, `web-apply-to-ictu`
(ADM-01), isn't among them.

**Result:** the index now holds **110 documents in 733 chunks**.

## Step 9. Check that search works, and calibrate the confidence threshold

### Acceptance query

```bash
ictkb search "How do I register for courses?"
# confidence: high
# 0.883  erp-course-registration         [How do I register courses on the ERP?]
# 0.888  procedures-course-registration  [How do I register for courses each semester?]
# 0.856  procedures-add-drop             [Can I add or drop a course after registering?]
# ...                                    (about 5 s including loading e5)
```

### Golden-question evaluation

```bash
python eval/run_eval.py --report docs/joelfah/reports/eval-phase1-e5.md    # 13 s for 103 questions
```
Full report: [reports/eval-phase1-e5.md](reports/eval-phase1-e5.md). (The script exits with code 1 because the
no-answer target failed at the old threshold; see below.)

| Metric | Local (e5, staging + website) | Upstream report (bge-m3, production) |
|---|---|---|
| Coverage (expected documents indexed) | 84 of 98 (85.7%) | 63 of 98 (64.3%) |
| hit@5 on covered questions | **94.0%** | 88.9% |
| hit@5 on covered P0 questions | 94.7% (19 of 19 covered) | 100% |
| Mean reciprocal rank | 85.8% | 86.6% |

Coverage is higher locally because staging also indexes draft documents. Drafts may contain `[[TO FILL]]` gaps, which
the chatbot must not present as facts.

### Why the threshold had to change

The search marks a result `high` confidence when the best chunk's similarity reaches `MIN_SIMILARITY`. The repo's 0.64
was tuned for bge-m3. e5 gives every passage a high similarity (0.79-0.89 here), so at 0.64 **all** five unanswerable
questions were marked `high` (no-answer correctness 0%).

We measured the best similarity for each question with
[scripts/threshold_sweep.py](scripts/threshold_sweep.py) (`python docs/joelfah/scripts/threshold_sweep.py`) and tried
thresholds:

| Threshold | Answerable questions kept (82 retrieved correctly) | Unanswerable refused (of 5) |
|---|---|---|
| 0.80 | 82 (100%) | 1 |
| **0.81** | **82 (100%)** | **3** |
| 0.83 | 76 (93%) | 3 |
| 0.85 | 65 (79%) | 5 |
| 0.86 | 52 (63%) | 5 |

The unanswerable questions and their best similarity:

| Question | Best similarity | Why it scores high |
|---|---|---|
| NEG-02 "What is my current fee balance?" | 0.848 | Fee documents exist; the personal balance doesn't |
| NEG-04 "Will I pass my resit?" | 0.833 | Resit documents exist; a prediction doesn't |
| NEG-03 "Last year's exam questions" | 0.805 | refused at 0.81 |
| NEG-01 "Rector's personal phone number" | 0.800 | refused at 0.81 |
| NEG-05 "Weather in Yaounde today" | 0.791 | refused at 0.81 |

**Decision: `MIN_SIMILARITY=0.81`.** It keeps every answerable question and refuses the clearly off-topic ones.
The two that remain are *about* covered topics, and similarity alone cannot tell "this topic is covered" from "this
exact fact is here". (Upstream solved the same gap with a language-model check in its Cloudflare Worker.) In our
chatbot, the second filter is the language model itself: its instructions say to answer only from the passages and
otherwise say "I don't have that information". Phase 2 tests NEG-02 and NEG-04 specifically. Caveat: there are
only 5 unanswerable golden questions, so this is a small sample.

### French

```bash
ictkb search "Comment payer les frais de scolarité ?"
# finance-scholarships, finance-installments, procedures-graduation, finance-scholarships, campus-directions
ictkb search "How do I pay my tuition fees?"
# finance-installments, erp-fee-statement (x2), finance-late-payment, finance-installments
```
The English question returns only fee documents; the French one brings in unrelated ones (graduation, travel
fares). The knowledge base is written in English, so for French questions the keyword half of the hybrid search finds
nothing and only e5's cross-language matching helps. **French retrieval is a weak spot to measure in Phase 3.**
`finance-payment-channels` isn't in the top 5 in either language, which is also worth investigating.

## Step 10. Verify nothing goes to the network

We couldn't simply switch off Wi-Fi during the test (the coding assistant session needs it), so we recorded every
network connection the search program opens:

```bash
strace -f -e trace=connect -o connect.log ictkb search "Comment payer les frais de scolarité ?"
```
Every connection went to `127.0.0.1:5432` (our database) or to the local name-service socket
(`/var/run/nscd/socket`, used to look up "localhost"). **No connection left the machine**, which means the model
loads from the local cache and nothing calls a cloud service. To confirm by hand: switch off Wi-Fi and run the same
`ictkb search`; it should answer the same way.

---

## Resource summary

| Operation | Time | Peak RAM |
|---|---|---|
| e5 download (one-time, shared connection) | 45 min | - |
| Load e5 + embed one query | about 5 s per `ictkb search` (mostly loading) | 1.6 GB |
| `ictkb index` (77 docs, 241 chunks) | 4 min 44 s | 4.4 GB |
| `ictkb crawl` (33 pages, 492 chunks) | 6 min 56 s (includes the 20 s politeness delays) | 2.35 GB |
| 103 golden questions (model loaded once) | 13 s | - |

## What this means for Phase 2

- Load e5 **once** when the chatbot starts (about 5 s), then each question's retrieval is a fraction of a second.
- Use `MIN_SIMILARITY=0.81` to skip the language model on clearly off-topic questions.
- The prompt must make the model refuse when the passages are about the topic but don't contain the specific fact.
- Show a warning for draft or stale sources, since drafts can contain `[[TO FILL]]` gaps.
