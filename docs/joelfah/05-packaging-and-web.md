# 05. Packaging and a web page (Phase 5)

**Purpose:** make the assistant easy to set up again (for a demo, a fresh machine, or the course report) and easy to
use for someone who doesn't want a terminal. The chatbot stays ours: it lives in `chatbot/` on our fork's
`local-chatbot` branch and is not contributed to the shared knowledge base. (The fork is public, so it can be read,
but it never goes upstream.)

## Two commands

```bash
./chatbot/setup.sh      # one time
./chatbot/run.sh        # terminal chat;  ./chatbot/run.sh --web  for the browser page
```

### What `setup.sh` does, and why each step is there

| Step | What | Why it's scripted this way |
|---|---|---|
| 1 | Checks Python 3.11+, Docker usable without sudo, Ollama installed and running | These were our Phase 0-1 obstacles (Docker Desktop context, docker group). The script prints the exact fix instead of failing later with a cryptic error |
| 2 | `.venv` + `pip install -e ".[dev,local-embeddings]"` | The repo's own extras only; pip's noisy output goes to `.venv/setup-pip.log` and is shown only on failure |
| 3 | Copies `chatbot/env.template` to `.env` **only if `.env` doesn't exist**; otherwise checks it uses `fastembed` | Never overwrite a user's settings; refuse to continue with a cloud provider |
| 4 | Starts only the `db` container, waits until it accepts connections, runs `ictkb migrate` | A fixed `sleep` would be flaky; `pg_isready` is exact |
| 5 | `ictkb validate`, `ictkb index` (and `ictkb crawl` with `--crawl`) | Indexing is incremental (content hashes), so a re-run is quick |
| 6 | `ollama pull qwen2.5:3b` if missing | |
| 7 | Unit tests + one search | Proves the installation works before you rely on it |

`FASTEMBED_CACHE_PATH` is exported by both scripts, so the 2.2 GB model can never land in `/tmp` again (failure
log #2 and #3). The scripts never call `sudo`: system installs stay the user's decision.

**Tested:** a full re-run on the development laptop finished in 15 s with nothing re-indexed (77 unchanged), the
existing `.env` kept byte for byte, 22 tests passing and the registration search correct. The failure path was
tested in a shell without Docker access: it stops at step 1 with "Run: sudo usermod -aG docker ...". Not tested:
a first run on a fresh machine (the download steps were each exercised in Phase 1, but not through the script).

### `run.sh`

Starts the database if it isn't up, checks Ollama, then runs the terminal chat, or the web page with `--web`.

## The web page

`./chatbot/run.sh --web`, then open http://127.0.0.1:8765.

- **Same pipeline** as the terminal (`chat.Assistant`), so every safeguard applies: the similarity threshold, the
  redaction of invented contacts, the number/date check, draft and stale notes.
- **Streams** the answer as it's written: the server sends newline-delimited JSON events (`text` pieces, then a
  `done` event with confidence, cited sources, passages and timings). The page shows the text line by line, styles
  sources, notes and warnings, and offers "details" (which passages were retrieved and which were given to the model).
- **No new dependency, works offline:** Python's `http.server`; one HTML file with inline CSS and JavaScript; no CDN,
  no fonts from the internet. Light and dark themes follow the system.
- **Local and safe by design:**
  - listens on 127.0.0.1 only;
  - accepts only `application/json` requests (a form on another website can't send that without a browser
    preflight check, which the server never approves);
  - refuses any `Host` other than `127.0.0.1`/`localhost` (blocks "DNS rebinding", where a website points its own
    name at your machine);
  - inserts everything as text, never as HTML, and only makes `http(s)` links clickable;
  - answers one question at a time (the embedding model, the database connection and Ollama are shared).
- **Tested:** 7 unit tests with a fake assistant (streaming, bad input, wrong content type, foreign host name), and a
  live request through `run.sh --web`: correct, cited installment answer, first words after 26 s, done in 44 s.

## Trade-offs

| Choice | Gained | Gave up |
|---|---|---|
| Shell scripts, not a Python installer or Makefile | Readable, no extra tool, matches how we set it up by hand | Linux/macOS only (Windows would need WSL) |
| Scripts don't install Docker or Ollama | No `sudo` in our scripts; the user stays in control | Two manual installs on a fresh machine |
| Standard-library web server | No dependency, nothing to keep updated | No multi-user features; one question at a time |
| Stream raw text + a summary event | Same output as the terminal, little code | The page parses lines to style them; a format change in the terminal output changes the page |
