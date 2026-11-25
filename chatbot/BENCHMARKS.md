# Benchmarks

Measurements of the local assistant on a student laptop. One change at a time; every answer is checked by hand
against its source documents. The story behind these numbers: [docs/joelfah/03-evaluation.md](../docs/joelfah/03-evaluation.md).

## Hardware and software

| Item | Value |
|---|---|
| CPU | Intel Core i7-10710U, 6 cores / 12 threads, AVX2, no GPU used |
| RAM | 15 GiB; during the runs 2.8-6.1 GiB available and 5.2-8.0 GiB of swap in use (browsers and VS Code open) |
| OS | Zorin OS 18.1 (Ubuntu 24.04 base) |
| Ollama | 0.40.18 |
| Embeddings | `intfloat/multilingual-e5-large` (fastembed 0.9.1, ONNX Runtime 1.32.0), 1024 dimensions |
| Index | 110 documents (77 `content/`, staging, + 33 website pages), 733 chunks, PostgreSQL 16 + pgvector |

**Timings are noisy.** Memory pressure (swap), other programs, and Ollama's prompt cache (it reuses work when
consecutive prompts start the same way) change the time to first word by up to 10x for the same question. Each run
records memory and load before and after (`reports/*.machine.txt`). Compare timings within a run, and treat
differences between runs below about 30% as noise.

## Method

- **Retrieval:** `python eval/run_eval.py` on all 103 golden questions ([report](reports/eval-retrieval-local-e5.md)).
- **Generation:** `python -m chatbot.eval_generation --label <name> [--live]` on 20 golden questions: 9 P0 across
  categories, 3 multi-hop, the 3 French variants, the 5 no-answer questions. Report, CSV and log in [reports/](reports/).
- **Verdicts** (in each CSV): *correct* (all facts match the source), *partial* (facts right but incomplete, or a
  condition dropped, or a minor unsupported detail), *wrong* (a wrong or invented fact, or a different topic),
  *refused*. Checked by Claude against the source files; marked "confirm" for a human check.
- **Variance:** without a fixed seed, 14 of 20 answers changed between two runs with identical passages. A
  difference of 1-2 answers between configurations is within noise. With `CHAT_SEED` set, answers match for most of
  their length but can still diverge near the end (prompt-cache reuse and multi-threaded arithmetic).

## Retrieval (all 103 golden questions)

| Measure | e5 local, `MIN_SIMILARITY=0.64` | e5 local, `MIN_SIMILARITY=0.81` | Upstream report (bge-m3) |
|---|---|---|---|
| Coverage | 84/98 | 84/98 | 63/98 |
| hit@5 (covered) | 94.0% | 94.0% | 88.9% |
| hit@5 P0 | 94.7% | 94.7% | 100% |
| MRR | 85.8% | 85.8% | 86.6% |
| No-answer correctness | 0% | **60%** | 100% |

## Generation: before / after

| Run | Change | Answerable (15): correct / partial / wrong / refused | No-answer (5) | Invented facts shown | Median first word | Median full answer | Answer speed |
|---|---|---|---|---|---|---|---|
| baseline | qwen2.5:3b, top-k 4, 1200/4000 chars, temp 0.1, repeat 1.05 | 8 / 4 / 1 / 2 | 4 refused, 1 partial | 0 (1 email removed) | 15.5 s | 30.5 s | 7.5 tok/s |
| qwen1.5b | model → qwen2.5:1.5b | 9 / 2 / 3 / 1 | 3 refused, 1 grounded redirect, 1 wrong | **5** | 17.1 s | 33.0 s | 6.5 tok/s |
| baseline-v2 | 3B + drop placeholder-only passages | 8 / 5 / 0 / 2 | 4 refused, 1 partial | 3 minor (French: name, ERP expansion, "par la poste") | 20.5 s* | 38.0 s* | 5.3 tok/s* |
| topk3 | top-k 4 → 3 | 7 / 3 / 3 / 2 | 4 refused, 1 grounded redirect | 1 (French name) | 4.5 s** | 36.1 s | 4.5 tok/s |
| **final** | v2 + seed 42 + exact-name rule for French | **8 / 4 / 1 / 2** | 4 refused, 1 partial | 1 unsupported claim (1 email removed) | 10.8 s | 34.8 s | 4.5 tok/s |

\* Both models were loaded during this run (the 1.5b from the previous run had not been unloaded), so swap rose to 8 GB.
\** Mostly Ollama's prompt cache: the median prompt only shrank from 807 to 686 tokens, but many prompts were read at
200-3000 tokens/s.

Per-question verdicts across runs:

| Id | Type | baseline | qwen1.5b | v2 | topk3 | final |
|---|---|---|---|---|---|---|
| ADM-01 | admissions | partial | correct | partial | correct | correct |
| PRC-02 | procedures | correct | correct | correct | wrong | correct |
| PRC-09 | procedures | correct | wrong | correct | correct | partial |
| FIN-01 | finance | refused | wrong | refused | wrong | refused |
| FIN-05 | finance | partial | correct | partial | partial | partial |
| FIN-06 | finance | wrong | wrong | correct | refused | correct |
| ERP-02 | erp | correct | correct | correct | correct | correct |
| ERP-03 | erp | correct | partial | correct | correct | partial |
| TTB-03 | timetables | correct | correct | correct | correct | correct |
| MHP-01 | multi-hop | partial | partial | partial | correct | partial |
| MHP-02 | multi-hop | correct | correct | correct | wrong | wrong |
| MHP-03 | multi-hop | correct | correct | correct | partial | correct |
| VAR-01 | French | correct | correct | partial | correct | correct |
| VAR-02 | French | partial | correct | partial | partial | correct |
| VAR-03 | French | refused | refused | refused | refused | refused |
| NEG-01..05 | no-answer | 4 refused + NEG-04 partial | 3 refused, NEG-02 redirect, NEG-04 wrong | 4 refused + partial | 4 refused + redirect | 4 refused + NEG-04 partial |

## Decisions

| Setting | Kept | Rejected | Why |
|---|---|---|---|
| Model | `qwen2.5:3b` | `qwen2.5:1.5b` | 1.5b showed 5 invented facts (vs 0-1), cited the expected document in 1/15 answers, and wasn't faster here |
| Passages | top-k 4 | top-k 3 | top-k 3 cut needed passages (FIN-06, MHP-03); full answers weren't faster |
| Placeholder-only passages | dropped | kept | their headings were mistaken for answers |
| Seed | 42 | none | consistent answers for students; fairer comparisons |
| Repeat penalty | 1.05 | 1.15 | 1.15 corrupted copied dates (Phase 2) |
| `qwen2.5:7b` | not tested | - | needs about 2.5 GB more RAM; with 5-8 GB already in swap it would mostly measure swapping |

## Weakest categories

Share of fully correct answers across the three 3B runs at top-k 4 (baseline, v2, final):

| Category | Correct | Typical failure |
|---|---|---|
| finance | 2/9 | caveats dropped ("level not specified"), false refusals, dates reframed ("due on 9 November") |
| admissions | 1/3 | one step attributed to the wrong office or to all applicants |
| French variants | 3/9 (2/2 in final) | invented university names until the exact-name rule |
| multi-hop | 5/9 | answers one half; `finance-clearance` never retrieved; resit types mixed |
| erp, procedures | 5/6 each | occasional unsupported extra sentence |
| timetables | 3/3 | - |
