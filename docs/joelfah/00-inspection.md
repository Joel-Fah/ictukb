# 00. Inspection (Phase 0)

**Purpose:** before installing anything, find out what the laptop can handle and what the repository already
provides, so every later choice fits the hardware and reuses existing code instead of rebuilding it.
Nothing was changed in this phase; only read-only commands were run.

## The laptop

| Item | Value | What it means for us |
|---|---|---|
| OS | Zorin OS 18.1 (Ubuntu 24.04 base), x86_64 | Standard Linux; Docker and Ollama both support it |
| CPU | Intel i7-10710U, 6 cores / 12 threads, AVX2, no AVX-512 | Enough for a small quantised model; AVX2 speeds up both ONNX (embeddings) and llama.cpp (Ollama) |
| GPU | Intel UHD (integrated) | Not usable for model inference: everything runs on the CPU |
| RAM | 15 GiB total, but only about 3.4 GiB free with browsers and VS Code open | **The real constraint.** The embedding model and the chat model must share whatever is free |
| Swap | 7.6 GiB zram + 2 GiB file | Cushions peaks, but swapping makes models very slow |
| Disk | 602 GB free | Not a constraint (models need about 4-5 GB in total) |
| Python | 3.12.3 | The repo needs at least 3.11 |
| Docker | Engine 29.10.0 + Compose v5.6.1 installed and running, **but** the CLI pointed at Docker Desktop (not running) and the user wasn't in the `docker` group | Needed a one-time fix (see 01) |
| Ollama | Not installed | Installed in Phase 1 |
| PostgreSQL | Not installed natively | We use the Docker image instead |

Commands used: `cat /etc/os-release`, `lscpu`, `free -h`, `swapon --show`, `df -h`, `lspci`, `docker version`,
`docker context ls`, `ollama --version`, `python3 --version`.

## What the repository already gives us

Read: `README.md`, `CONTRIBUTING.md`, `pyproject.toml`, `.env.example`, `docker/docker-compose.yml`,
`src/ictkb/{embedding,search,config,cli,db}.py`, `src/ictkb/api/routers/search.py`, `examples/starter-chatbot/`.

- **77 documents** in `content/` (46 verified, 31 draft with `[[TO FILL]]` placeholders).
- **`ictkb` command line tool**: `migrate` (create tables), `validate` (check the documents), `index` (chunk + embed +
  store), `crawl` (read the university website), `search` (test a query), and more.
- **Hybrid search** in `src/ictkb/search.py`: a plain Python function `search(conn, embedder, query, top_k)` that
  returns ranked chunks with similarity, source document, `last_verified` and a `stale` flag.
- **Embedding providers** (`src/ictkb/embedding.py`): `worker` (Cloudflare, the repo's default, needs the maintainer's
  admin token), `cohere` (cloud, paid key), `fastembed` (**local**, e5), `hash` (tests only).
- **A FastAPI server** that wraps `search()` behind API keys and rate limits.
- **A starter chatbot** (`examples/starter-chatbot/`) that calls the HTTP API and leaves `generate()` empty.
- **103 golden questions** (`eval/golden_questions.yml`) and an evaluation script.

### Surprises worth knowing

1. The repo's default provider is now `worker` (cloud). We must override it, or indexing fails asking for an admin
   token. Reported upstream as [#2](https://github.com/Egbemichel/ictukb/issues/2).
2. `MIN_SIMILARITY=0.64` was tuned for the cloud model (bge-m3). Different models give different similarity ranges,
   so we must re-tune it for e5.
3. The newest "answer verification" step (a model double-checks whether retrieved passages really answer the
   question) exists only in the Cloudflare Worker, not in the Python code we run locally.
   Reported as [#4](https://github.com/Egbemichel/ictukb/issues/4).
4. Many golden questions expect `web-*` documents, which come from crawling the website, not from `content/`.

## The three decisions

| Decision | Choice | Reasoning |
|---|---|---|
| Chat model | `qwen2.5:3b` (fallback `qwen2.5:1.5b`) | A 3B model quantised to 4 bits needs about 2.3 GB; with e5 (about 1.6 GB) that fits if some browser tabs are closed. Qwen handles English and French. The 1.5B fallback saves about 1 GB if needed. Speed is measured later, not assumed. |
| Database | Docker Engine, only the `db` service | Uses the exact image the repo uses (`pgvector/pgvector:pg16`), costs well under 100 MB of RAM when idle, and keeps PostgreSQL off the host system. Docker Desktop was rejected because on Linux it runs a whole virtual machine. |
| Retrieval | In-process call to `ictkb.search.search()` | The function is clean and already used this way by `ictkb search` and the evaluation. Running the API server instead would add a process, load a second copy of e5 (more RAM), and only bring API keys and rate limits, which we don't need locally. |

A fourth decision came up while reading: **crawl the website once** so the index also contains the `web-*` pages.
