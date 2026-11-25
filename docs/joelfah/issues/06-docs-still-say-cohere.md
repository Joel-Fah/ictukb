# Docs still describe Cohere as the default embedding provider

## What happens

Since 6667b3a the default embedding provider is `worker` (Cloudflare Workers AI, `@cf/baai/bge-m3`), in both
`src/ictkb/config.py` and `.env.example`. Some docs still describe Cohere as the default:

- `docs/architecture.md:42`: "The default is Cohere `embed-multilingual-v3.0`, which handles English and French."
- `docs/runbook.md`, one-time setup step 3: "Create a Cohere account and an API key (or set
  `EMBEDDING_PROVIDER=fastembed` for a local model)."
- `docs/runbook.md`, step 5: repository secrets list `DATABASE_URL`, `COHERE_API_KEY`, `DEPLOY_HOOK_URL`, but no
  workflow reads `COHERE_API_KEY` any more. `deploy.yml`, `eval.yml`, `ingest-daily.yml` and `ingest-live.yml` set
  `EMBEDDING_PROVIDER: worker` and read `secrets.ADMIN_TOKEN`; `deploy.yml` also reads `CLOUDFLARE_API_TOKEN` and
  `CLOUDFLARE_ACCOUNT_ID`.

## Proposal

Docs-only PR:

- `architecture.md`: the default is `worker` (bge-m3 through the Worker, 1024 dimensions, English and French);
  `cohere` stays available, `fastembed` (`multilingual-e5-large`) runs locally, `hash` is for tests.
- `runbook.md`: step 3 points to the Worker setup instead of a Cohere account; step 5 lists `DATABASE_URL`,
  `ADMIN_TOKEN`, `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` (and optionally `DEPLOY_HOOK_URL`).

I can open the PR if that's welcome.
