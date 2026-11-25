# FastAPI reference implementation lacks the answer verification that the Worker performs

## What happens

Commit 6667b3a added answer verification to the Cloudflare Worker (`cloudflare-worker/src/index.js`,
`verifyAnswer`): a best similarity of 0.70 or more is accepted, below 0.45 is rejected, and in between
`@cf/meta/llama-3.1-8b-instruct-fp8` judges YES/NO whether the passages answer the question. The response also gains
a `verification` field.

The Python side (`src/ictkb/search.py`, used by `ictkb search`, `eval/run_eval.py` and the FastAPI app) still decides
`confidence` from similarity alone (`best >= MIN_SIMILARITY`) and returns no `verification` field.

`docs/api.md` doesn't document the `verification` field either.

So the two implementations of `POST /v1/search` described in `docs/api.md` can give different `confidence` for the
same question, which matters most on no-answer questions (the reason verification was added). Someone who builds a
chatbot against a local FastAPI instance will see a different no-answer behaviour than against the live API.

## Proposal (pick one)

1. Document the difference in `docs/api.md` and `docs/architecture.md`: the FastAPI app is similarity-only and
   doesn't return `verification`.
2. Or port the same thresholds to `search.py` as an optional step, with the grader pluggable (it can be skipped when
   no model is configured, returning `verification: "similarity-only"` so the response shape matches).

Option 1 is a docs change. Option 2 touches `src/` and needs the infrastructure owner's approval.
