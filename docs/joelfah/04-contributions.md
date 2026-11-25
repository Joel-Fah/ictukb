# 04. Contributing back to the knowledge base (Phase 4)

**Purpose:** the knowledge base is shared by every student chatbot, so the gaps and problems we found while building
ours are worth fixing at the source, through issues and pull requests that follow `CONTRIBUTING.md`.

**Rule we kept:** content contributions need an official source we can name (an office, a handbook, a notice). We
have none for the missing facts, so we **did not fill any `[[TO FILL]]`**. Instead we documented precisely what is
missing, where, and who holds it, so the people with access to the offices can fill it quickly.

## What we sent before Phase 4

| | Topic | Status |
|---|---|---|
| [#2](https://github.com/Egbemichel/ictukb/issues/2) | README local setup needs the admin token | open |
| [#3](https://github.com/Egbemichel/ictukb/issues/3) | fastembed caches the model in `/tmp` | open |
| [#4](https://github.com/Egbemichel/ictukb/issues/4) | FastAPI lacks the Worker's answer verification | open |
| [#5](https://github.com/Egbemichel/ictukb/issues/5) | Postgres published on all interfaces | open |
| [#6](https://github.com/Egbemichel/ictukb/issues/6) | Docs still say Cohere | open |
| [#9](https://github.com/Egbemichel/ictukb/issues/9) | `MIN_SIMILARITY` depends on the embedding model (with e5 measurements) | open |
| [PR #7](https://github.com/Egbemichel/ictukb/pull/7) | Docs: embedding provider references (fixes #6) | open |
| [PR #8](https://github.com/Egbemichel/ictukb/pull/8) | README: local setup with fastembed (fixes #2) | open |

## Phase 4 drafts (not posted yet)

All in [issues/](issues/README.md):

| Draft | What it asks for | Evidence |
|---|---|---|
| 07 | Configure the 8 Google Sheets that 14 uncovered questions depend on | every `sheet_id` in `sources/sheets.yml` is empty; templates already exist |
| 08-12 | Fill 18 draft documents (campus, canteen, transport, student life, academic and finance) | each unfilled section listed, with what to collect and from which office (`docs/upload-checklist.csv`) |
| 13 | Four writing patterns that make answers wrong | 80 hand-checked answers: e.g. FIN-01 failed in 5 of 5 runs because the fee and its caveat share a paragraph |
| 14 | 26 French golden questions | French hit@5 20/26 vs English 26/26 on the same questions |
| 15 | Multi-hop failures: one document fills the top 5 (MHP-01); MHP-02 expects a document without the answer | reproduced on two embedding models |

Drafts 07-12 together cover all 35 golden questions that `docs/evaluation-latest.md` lists as "Not yet covered".

## How the drafts were built

- **Generated, not typed**: [scripts/coverage_gaps.py](scripts/coverage_gaps.py) reads the golden questions, the
  production coverage list, each document's sections, the upload checklist and `sources/sheets.yml`, and lists, per
  uncovered question, the exact unfilled sections or unconfigured sheet. That avoids copying mistakes in 35 rows.
- **Measured, not asserted**: the French gap comes from
  [scripts/french_vs_english.py](scripts/french_vs_english.py)
  ([results](reports/french-vs-english-retrieval.md)); the content patterns from the Phase 3 verdicts.
- **Checked against what we actually tested**: an early draft said our assistant "refuses all" questions in one
  group; we had only tested one of them, so the claim was narrowed.

## What we found along the way

1. **13 Google Sheets are configured with empty `sheet_id`s**, so `ictkb sync-sheets` skips them all. Some of
   what looked like "missing documents" locally is missing everywhere.
2. **All 18 draft documents have `owner: unassigned`**: nobody is responsible for filling them.
3. **Seven draft headings contain example answers in parentheses** ("cash, mobile money, other"), which a model can
   turn into invented facts while the body is empty.
4. **One golden question can't pass as written** (MHP-02 expects a fee schedule that doesn't mention resits).

## Why no content pull requests

- Filling placeholders needs official sources we don't have.
- Golden-question and search changes live in `eval/` and `src/`, which need the infrastructure owner's approval;
  the issues ask for it first, with ready-to-use material (the French YAML, a proposed per-document cap with a test).
- Restructuring existing sections (draft 13) changes no facts but changes how they're written; that's the category
  owners' call, so it's proposed, not done.
