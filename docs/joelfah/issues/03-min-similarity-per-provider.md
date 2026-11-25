# MIN_SIMILARITY is calibrated for bge-m3 only; other providers need their own threshold

## What happens

`.env.example` sets `MIN_SIMILARITY=0.64`, which fits bge-m3: per `docs/evaluation-latest.md`, the lowest top
similarity among answered questions is 0.498 and the highest among no-answer questions is 0.628. `config.py`
defaults to `0.35`. Nothing says the value depends on the embedding model.

With `EMBEDDING_PROVIDER=fastembed` (`multilingual-e5-large`), e5 gives every passage a high cosine similarity. On a
local staging index (77 `content/` documents + 33 crawled pages, 733 chunks, commit 2c9f3eb), `python eval/run_eval.py`
reports:

| Metric | e5 local, MIN_SIMILARITY=0.64 |
|---|---|
| hit@5 on covered questions | 94.0% |
| No-answer correctness | **0.0%** (every NEG question is `high`) |
| Lowest top similarity among answered questions | 0.812 |
| Highest top similarity among no-answer questions | 0.848 |

Sweep of the threshold (82 answerable questions retrieved correctly, 5 no-answer questions):

| Threshold | Answerable kept | No-answer refused |
|---|---|---|
| 0.64 | 82 (100%) | 0 |
| 0.81 | 82 (100%) | 3 |
| 0.83 | 76 (93%) | 3 |
| 0.85 | 65 (79%) | 5 |

With e5 the ranges overlap: NEG-02 ("What is my current fee balance?", 0.848) and NEG-04 ("Will I pass my resit?",
0.833) score like answerable questions, because fee and resit documents exist. Similarity alone can't reject them,
which is the case the Worker's verification step (6667b3a) handles. The Python search has no such step (#4).

## Proposal

Docs only:

1. In `.env.example`, comment that `MIN_SIMILARITY` depends on the provider: about 0.64 for `worker` (bge-m3),
   about 0.81 for `fastembed` (e5-large, measured above), and to recalibrate with `python eval/run_eval.py` after
   changing the model.
2. Mention in `docs/architecture.md` §4 that with e5 the similarity ranges overlap, so a local deployment needs an
   answer-verification step (#4) or a prompt that refuses when the passages don't contain the specific fact.

Measurement script used for the sweep:
https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/scripts/threshold_sweep.py
