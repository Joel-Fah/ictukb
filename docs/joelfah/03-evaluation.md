# 03. Measuring and tuning (Phase 3)

**Purpose:** find out how good the assistant really is, which settings help, and where it is weakest, by measuring
on the repo's golden questions instead of on questions we picked ourselves.

**Result in short:** the final configuration (`qwen2.5:3b`, 4 passages, seed 42) answers 8 of 15 answerable golden
questions fully correctly and 4 partially, gets 1 wrong, and refuses 2 (one rightly: the finance-office directory is generated from a Google Sheet that isn't configured yet).
4 of 5 unanswerable questions are refused; no invented contact detail reached the student. Finance and multi-hop
questions are the weakest. A smaller model invented more; fewer passages lost needed information. The biggest lesson
was about measurement itself: **one run of 20 questions is noisy**.

Numbers and the full before/after table: [chatbot/BENCHMARKS.md](../../chatbot/BENCHMARKS.md). Every answer with its
verdict: `chatbot/reports/generation-<run>.csv`.

---

## How we measured

1. **Retrieval** on all 103 golden questions with the repo's own script (`eval/run_eval.py`): is the expected
   document in the top 5?
2. **Generation** on 20 of them with our script `chatbot/eval_generation.py`: 9 high-priority (P0) questions across
   categories, 3 multi-hop questions (needing two documents), the 3 French questions, and the 5 the knowledge base
   can't answer. For each, it records the answer, retrieved and cited documents, refusals, flagged facts and timings.
3. **Verdicts by hand**: every answer read against every passage the model was given, then marked *correct*,
   *partial*, *wrong* or *refused*, with a note (in the CSV; the final 3B and 7B runs were later confirmed by Joel in [verdict-review.md](verdict-review.md), the older runs are still marked "confirm"). The automatic columns
   ("expected document cited") turned out to be poor proxies: an answer can cite the right document and still state
   the wrong date.
4. **One change at a time**, each run logged with the machine's memory and load. With `--live`, the run can be
   watched as it happens (`tail -f chatbot/reports/generation-<run>.log`).

## The runs

| Run | What changed | Outcome |
|---|---|---|
| baseline | Phase 2 settings | 8 correct / 4 partial / 1 wrong / 2 refused; 0 invented facts shown |
| qwen1.5b | smaller model | slightly more literal, but **5 invented facts** ("2-3 business days", canteen "cash and mobile money", "ERP (Electronic Records Processing)", a button label, a resit prediction); cites almost nothing; not faster here → **rejected** |
| baseline-v2 | drop passages that are only `[[TO FILL]]` | FIN-06 fixed (the 1.5b had invented canteen payment methods from the *heading* of an empty section); new small inventions in French |
| topk3 | 3 passages instead of 4 | the 4th passage was sometimes the needed one (FIN-06 refused, MHP-03 lost the tuition); full answers not faster → **rejected** |
| final | v2 + fixed seed + "call the university ICT University" for French | 8 / 4 / 1 / 2; French answers correct; 1 unsupported sentence (ERP-03) |

## What we learned

### 1. Measurement noise was as large as the effects we were measuring

Between baseline and v2, the passages given to the model were identical for every question, yet **14 of 20 answers
changed**. Temperature 0.1 still samples, and without a fixed seed each run is a different draw. An invented name
appeared in one run and vanished in the next; a correct answer became partial. So:

- differences of 1-2 answers between configurations mean nothing on a single run of 20 questions;
- only large, repeated effects can be trusted: the 1.5b's 5 invented facts, top-k 3 cutting needed passages, the
  placeholder fix (a mechanism we can see), and the French name problem (seen in 4 runs);
- we added a fixed seed (`CHAT_SEED=42`). Answers now match for most of their length but can still diverge near the
  end, because Ollama reuses cached prompt work and multi-threaded CPU arithmetic isn't exactly repeatable.
  Exact repeatability isn't possible on this setup; the seed is still worth it, because students get consistent answers.

### 2. Speed numbers lie unless you know what the cache did

Top-k 3 seemed to cut the time to first word from 15.5 s to 4.5 s. The prompt was only 15% shorter; the rest was
Ollama's prompt cache (prompts read at 200-3000 tokens/s instead of about 40). Full answers were not faster. The
machine's state mattered more than the setting: a leftover model in memory pushed swap to 8 GB and slowed a whole run.

### 3. Smaller isn't faster when memory is the bottleneck

The 1.5b model needs about 1 GB less, but with the laptop already swapping it wasn't measurably faster, and it
invented far more. On this hardware the 3B is the better trade.

### 4. Empty sections are dangerous

A draft section whose body is `[[TO FILL]]` still has a heading such as "Which payment methods does the canteen
accept (cash, mobile money, other)?". A model reads that as an answer. Dropping such passages (and refusing when
nothing else is left) fixed it for every model.

### 5. Some errors only a human catches

Our code checks catch invented numbers, months, emails and links that are *not in the passages*. They can't catch:
- a wrong date that *is* in the passages (PRC-02 in one run gave the superseded 19 November deadline instead of 23),
- the right fact applied to the wrong case (the special-resit rule "out of 100" given for a normal resit),
- a dropped condition (365,000 "for the Bachelor", when the source says the level isn't specified),
- an invented small number when the same digits appear elsewhere ("2-3 business days").

These need a human check, a bigger model, or better-structured content (see below).

## Weakest areas

| Area | What goes wrong | Possible fix |
|---|---|---|
| **Finance** (2/9 fully correct across three 3B runs) | Caveats dropped, false refusals, "due on 9 November" (that's the fees-control date) | Content: a question-style section "When is each installment due?" stating what's known and unknown; the prompt can't fix this reliably |
| **Multi-hop** (5/9) | Only one half answered; `finance-clearance` never retrieved; resit types mixed | Retrieve per sub-question, or content that links the two topics |
| **Admissions** (1/3) | A step for Top-Up students presented as for everyone; wrong office credited | Shorter, one-case-per-section content |
| **French** | Retrieval weaker (English-only content); names invented until the exact-name rule | French golden questions and French headings upstream |
| **Unanswerable but on-topic** (NEG-02, NEG-04) | Pass the similarity threshold; the model mostly refuses, sometimes restates rules | An answer-verification step, as upstream does in its Worker ([#4](https://github.com/Egbemichel/ictukb/issues/4)) |

Strong areas: timetables (3/3), ERP procedures (5/6), course-registration procedures (5/6), off-topic refusals (always).

## What we did not test

- ~~`qwen2.5:7b`~~: tested later (2026-11-26), after a reboot with the browsers closed: 13/15 correct, no invented
  facts, 62 s per answer. Profile and decision in [models.md](models.md#qwen257b-reads-conditions-but-slow).
- Passage length (`CHAT_MAX_CHUNK_CHARS`) and the threshold beyond Phase 1's sweep.
- More than one run per configuration: each run takes 10-15 minutes and a full hand check; with more time, 3 runs
  per configuration would make the comparisons solid.
