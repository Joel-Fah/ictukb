# MIN_SIMILARITY is calibrated for bge-m3 only; other providers need their own threshold

> DRAFT, not posted. Waiting for measured e5 similarities from the local index (answerable vs no-answer golden
> questions). Fill the table below from real runs before posting.

## What happens

`.env.example` sets `MIN_SIMILARITY=0.64`. Per `docs/evaluation-latest.md`, that value separates answered and
no-answer questions for bge-m3 (lowest answered top similarity 0.498, highest no-answer 0.628). `config.py` defaults
to `0.35`.

Cosine similarity ranges differ between embedding models. With `EMBEDDING_PROVIDER=fastembed`
(`multilingual-e5-large`), the measured ranges on a local index are:

| Set | min top similarity | max top similarity |
|---|---|---|
| Answerable golden questions (covered) | [[TO FILL]] | [[TO FILL]] |
| No-answer golden questions | [[TO FILL]] | [[TO FILL]] |

## Proposal

Document in `.env.example` / `docs/architecture.md` that `MIN_SIMILARITY` depends on the provider, with a
recommended value per provider (bge-m3: 0.64; e5-large: [[TO FILL]]).
