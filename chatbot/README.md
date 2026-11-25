# ICT University assistant (local)

A chatbot (terminal or browser) that answers questions about ICT University from the shared knowledge base in this
repository. Everything runs on your own computer: the search index (PostgreSQL + pgvector in Docker), the embedding
model (e5, through fastembed) and the language model (`qwen2.5:3b`, through Ollama). After the one-time setup it
needs no network and no API key. This folder is personal: it is not contributed to the shared knowledge base.

Setup, design decisions and measurements are in the project journal: [docs/joelfah/](../docs/joelfah/README.md).

## Quick start: two commands

You need, once: Python 3.11+, Docker Engine usable without sudo, and [Ollama](https://ollama.com) running.
`setup.sh` checks all three and prints the exact fix if one is missing.

```bash
./chatbot/setup.sh          # one time: venv, .env, database, index, models, self-test (first run: ~4 GB download)
./chatbot/run.sh            # terminal chat
./chatbot/run.sh --web      # or: browser page at http://127.0.0.1:8765 (local only)
```

`setup.sh` is safe to run again (it skips what's done and never overwrites an existing `.env`); add `--crawl` to
also re-read the university website. Measured on the development laptop: a re-run takes about 15 s.

### By hand (what the scripts do)

```bash
. .venv/bin/activate
export FASTEMBED_CACHE_PATH=$HOME/.cache/fastembed    # otherwise fastembed stores the model in /tmp
docker compose -f docker/docker-compose.yml up -d db
python -m chatbot.chat             # interactive
python -m chatbot.chat --debug "How do I register for courses?"   # one-off, with scores and timings
python -m chatbot.web --port 8765  # web page
```

Commands inside the terminal chat: `/sources` (passages retrieved for the last question, with scores), `/debug`
(toggle scores and timings), `/quit`.

### The web page

Same pipeline and safeguards as the terminal. The answer streams in as it's written; under it, "details" shows the
confidence, the passages retrieved (and which were given to the model) and the timings. It listens on 127.0.0.1
only, accepts only JSON requests from a localhost host name (so other websites open in your browser can't use it),
and loads nothing from the internet. One question is answered at a time.

## How it answers

```
question ─► detect language (en/fr) ─► search the local index (top 4 passages, hybrid vector + keyword)
                                             │
             best similarity < MIN_SIMILARITY ┤──► fallback: "not in the knowledge base" + official contacts
                                             │     (the language model is not called)
                                             ▼
             rules + passages (trimmed) + question ─► qwen2.5:3b (streamed)
                                             │
             cited [doc-ids] ─► "Sources:" list + draft/stale warnings
             no citation (the model declined) ─► official contacts
```

- **Retrieval is in-process:** `chatbot/retrieval.py` imports `ictkb.search.search()` directly instead of calling the
  FastAPI server. The function is already used this way by `ictkb search` and `eval/run_eval.py`; the API layer only
  adds API keys and rate limiting, and a second process would load a second copy of e5 (about 1.6 GB).
- **Local-only guard:** the chatbot refuses to start if `EMBEDDING_PROVIDER` is not `fastembed`.
- **Placeholders:** `[[TO FILL]]` in draft documents is shown to the model as "(not documented yet)", which the
  rules tell it to treat as unknown.
- **Contacts** in the fallback are read from the `about-contacts` document in the index, never written in the code.
- **Sources and warnings** are printed by the program from the cited ids, not written by the model, so they are
  always real documents with their real `last_verified` date and status.
- Each question is answered independently (no conversation memory), so earlier turns can't push the retrieved
  passages out of the small context window.

## Settings

Knowledge-base settings come from `.env` (read by ictkb): `DATABASE_URL`, `EMBEDDING_PROVIDER`, `KB_ENV`,
`MIN_SIMILARITY` (0.81 for e5, see the journal). The chatbot's own settings are environment variables with defaults
in [config.py](config.py):

| Variable | Default | Meaning |
|---|---|---|
| `CHAT_MODEL` | `qwen2.5:3b` | Ollama model |
| `OLLAMA_URL` | `http://127.0.0.1:11434` | Ollama server |
| `CHAT_TOP_K` | 4 | Passages retrieved per question |
| `CHAT_MAX_CHUNK_CHARS` | 1200 | Each passage is cut to this length |
| `CHAT_MAX_CONTEXT_CHARS` | 4000 | All passages together |
| `CHAT_MIN_SIMILARITY` | (from `.env`) | Override the confidence threshold |
| `CHAT_RELATIVE_CUTOFF` | 0.05 | Drop passages scoring this much below the best one |
| `CHAT_NUM_CTX` | 4096 | Model context window (tokens) |
| `CHAT_TEMPERATURE` | 0.1 | Low = factual answers |
| `CHAT_REPEAT_PENALTY` | 1.05 | Qwen 2.5's default; 1.15 corrupted copied dates |
| `CHAT_MAX_ANSWER_TOKENS` | 400 | Hard cap on answer length |
| `CHAT_SEED` | 42 | Fixed sampling seed: the same question gets (almost) the same answer |
| `CHAT_KEEP_ALIVE` | `30m` | How long Ollama keeps the model in memory between questions |
| `CHAT_WEB_PORT` | 8765 | Port of the web page (`--port` overrides it) |
| `FASTEMBED_CACHE_PATH` | `~/.cache/fastembed` | Where the e5 model is stored (fastembed's own default is `/tmp`) |

## Files

| File | Role |
|---|---|
| `config.py` | Settings and defaults |
| `retrieval.py` | Calls the repo's hybrid search; returns passages + confidence; reads the contacts document |
| `prompt.py` | System prompt, context formatting and trimming, language detection, citations, fallback text (EN/FR) |
| `llm.py` | Streaming client for Ollama's `/api/chat` (uses `httpx`, already a repo dependency) |
| `chat.py` | Terminal loop and the answer pipeline |
| `tests/` | Unit tests that need neither the database nor the model: `python -m pytest chatbot/tests` |
| `setup.sh`, `run.sh` | One-time setup and start (terminal or `--web`) |
| `env.template` | The local-only `.env` that `setup.sh` copies when there is none |
| `web.py`, `web_page.html` | Local web page (standard library HTTP server, NDJSON streaming, no external resources) |
| `eval_generation.py` | Runs golden questions through the whole pipeline and writes a report + CSV for hand verdicts: `python -m chatbot.eval_generation --label <name> [--live]` |
| `BENCHMARKS.md` | Hardware, method, before/after results, decisions, weakest categories |
| `reports/` | Evaluation reports, CSVs with verdicts, live logs, machine state per run |

No new dependencies: the chatbot uses only the standard library and packages the repo already declares.
