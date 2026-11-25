# Local setup in README cannot index: default embedding provider needs the admin token

## What happens

Following the README "Local setup" exactly:

```bash
pip install -e ".[dev]"
cp .env.example .env
docker compose -f docker/docker-compose.yml up -d db
ictkb migrate && ictkb validate
ictkb index
```

`.env.example` sets `EMBEDDING_PROVIDER=worker`, and `WorkerEmbedder.__init__` (`src/ictkb/embedding.py:80`) raises
before any network call:

```
RuntimeError: ADMIN_TOKEN is not set
```

Contributors don't have the admin token (and shouldn't), so nobody but the maintainer can build a local index
from the README. Reproduced on commit 2c9f3eb with:

```bash
EMBEDDING_PROVIDER=worker ADMIN_TOKEN= python -c "from ictkb.embedding import get_embedder; get_embedder()"
```

## Proposal

Docs only, no code change:

1. In README "Local setup", install the local extra and switch the provider for contributors:
   ```bash
   pip install -e ".[dev,local-embeddings]"
   cp .env.example .env    # then set EMBEDDING_PROVIDER=fastembed
   ```
2. Add one line saying a local `fastembed` index uses `intfloat/multilingual-e5-large` (about 2.2 GB, downloaded once)
   and is **not** interchangeable with the shared bge-m3 index (the indexer already refuses to mix models through `kb_meta`).
3. Optionally comment the `.env.example` line: `worker` is for the maintainer and CI, `fastembed` for contributors.

I can open a small docs PR for this if that's welcome.

## Context

Found while setting up a fully local, offline copy of the knowledge base (fastembed + the compose `db` service).
With `EMBEDDING_PROVIDER=fastembed`, `ictkb migrate`, `validate` and `index` work without any cloud credential.
