# Upstream issue drafts (Egbemichel/ictukb)

Each file is one issue: the first `# ` line is the title, the rest is the body. Post with:

```bash
f=docs/joelfah/issues/01-local-setup-needs-admin-token.md
gh issue create -R Egbemichel/ictukb --title "$(head -1 "$f" | sed 's/^# //')" --body "$(tail -n +3 "$f")"
```

| # | File | Area | Needs infra-owner approval to fix | Status |
|---|---|---|---|---|
| 01 | [01-local-setup-needs-admin-token.md](01-local-setup-needs-admin-token.md) | README / `.env.example` | No (docs) | posted: [#2](https://github.com/Egbemichel/ictukb/issues/2) |
| 02 | [02-fastembed-cache-in-tmp.md](02-fastembed-cache-in-tmp.md) | `src/` | Yes | posted: [#3](https://github.com/Egbemichel/ictukb/issues/3) |
| 03 | [03-min-similarity-per-provider.md](03-min-similarity-per-provider.md) | config / docs | No (docs) | ready (numbers filled), not posted |
| 04 | [04-fastapi-missing-answer-verification.md](04-fastapi-missing-answer-verification.md) | `src/` or docs | Depends on option | posted: [#4](https://github.com/Egbemichel/ictukb/issues/4) |
| 05 | [05-compose-db-port-exposed.md](05-compose-db-port-exposed.md) | `docker/` | Yes | posted: [#5](https://github.com/Egbemichel/ictukb/issues/5) |
| 06 | [06-docs-still-say-cohere.md](06-docs-still-say-cohere.md) | `docs/` | No (docs) | posted: [#6](https://github.com/Egbemichel/ictukb/issues/6) |

Content issues (missing information per category, retrieval failures PRG-05, TTB-04, PPL-05, PPL-06, MHP-01 to 03)
come after the local evaluation, so they carry fresh evidence.

## Pull requests

| PR | Branch | Fixes | Status |
|---|---|---|---|
| [#7](https://github.com/Egbemichel/ictukb/pull/7) | `docs/embedding-provider-refs` | #6 | open |
| [#8](https://github.com/Egbemichel/ictukb/pull/8) | `docs/readme-local-embeddings` | #2 (docs part) | open |

Both add the same `contributors.yml` entry; when one merges, the other's identical change should merge cleanly.
