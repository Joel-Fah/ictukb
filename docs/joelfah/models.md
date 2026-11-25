# Models: how each one behaved

One page per model, side by side: what it costs on this laptop, how often it was right, and *how* it went wrong.
Every claim points to its evidence: the per-answer verdicts in `chatbot/reports/generation-<run>.csv`, the
transcripts next to them, and the numbered entries of the [failure log](failure-log.md). Numbers come from the
20-golden-question evaluation ([03-evaluation.md](03-evaluation.md), [BENCHMARKS](../../chatbot/BENCHMARKS.md))
unless stated otherwise.

Laptop: Intel i7-10710U (6 cores, AVX2), 15 GiB RAM of which 3-6 GiB is usually free, no GPU. All chat models run
through Ollama 0.40.18 at temperature 0.1, 4096-token context, 4 passages per question.

## At a glance

| | `qwen2.5:1.5b` | `qwen2.5:3b` (in use) | `qwen2.5:7b` |
|---|---|---|---|
| Parameters / quantisation | 1.5B, Q4_K_M | 3.1B, Q4_K_M | 7.6B, Q4_K_M |
| Download | 986 MB | 1.9 GB | about 4.7 GB |
| RAM in Ollama (4096-token context) | 1.17 GB (measured) | 2.17 GB (measured) | to measure |
| Runs evaluated | 1 (20 questions) | 4 Phase 3 runs (80 answers) + 4 Phase 2 rounds (12 questions) | pending |
| Answerable, of 15: correct / partial / wrong / refused | 9 / 2 / 3 / 1 | 8 / 4 / 1 / 2 (final run) | pending |
| No-answer questions, of 5 | 3 refused, 1 grounded redirect, 1 wrong | 4 refused, 1 partial (final run) | pending |
| Invented facts shown to the student | **5** in one run | 0-1 per run (contacts always removed by code) | pending |
| Cited the expected document | **1/15** | 14/15 | pending |
| Median first words / full answer | 17.1 s / 33.0 s (CPU busier during this run) | 10.8 s / 34.8 s (final); 15.5 s / 30.5 s (baseline) | estimate: ~40-50 s / ~1.5-2 min |
| Writing speed | 6.5 tokens/s | 4.5-7.5 tokens/s depending on load | estimate: ~2-2.5 tokens/s |
| Verdict | **Rejected** | **Kept** (default) | **Testing** |

Timings vary with memory pressure and Ollama's prompt cache (see [03-evaluation.md](03-evaluation.md), lesson 2):
compare models on quality first, and only on large timing differences.

---

## `qwen2.5:1.5b`: literal, but fills gaps

**Run:** `generation-qwen1.5b` ([report](../../chatbot/reports/generation-qwen1.5b.md),
[verdicts](../../chatbot/reports/generation-qwen1.5b.csv)).

**Strengths**
- **Copies the passage closely.** Several answers were *more complete* than the 3B's: all three installment amounts
  (FIN-05), the "level not specified" caveat kept in French (VAR-02), the correct official-transcript request steps
  (MHP-01).
- Answers in French well when the passage is right (VAR-01, VAR-02 correct).

**How it fails**
- **Fills gaps with plausible inventions**, five in one run:
  "approximately 2-3 business days" for a transcript (PRC-09, failure 22);
  "the canteen accepts cash and mobile money", read from the *heading* of an empty draft section (FIN-06, failure 23);
  "ERP (Electronic Records Processing)" (MHP-01, failure 24); a button "Send me a link" (ERP-03);
  "if you meet these criteria, you should pass your resit" (NEG-04).
- **Asserts a figure without its condition:** "the Bachelor tuition is XAF 365,000" where the source says the level
  isn't specified (FIN-01).
- **Barely cites:** the expected document was cited in 1 of 15 answers, so a student can't check where an answer
  came from (the page then lists the passages "given, not cited").
- Treated "What is my current fee balance?" as "how do I see my balance" and answered with the ERP steps: grounded
  and arguably helpful, but not the refusal the golden set expects (NEG-02).

**Why (likely):** a smaller model has less capacity to keep the rules, four passages and the question in view at once,
so learned patterns ("transcripts take a few days", "canteens accept cash") win more often; and it seems to have
picked up the citation format less reliably. See [why models behave this way](failure-log.md#why-models-behave-this-way).

**Cost / speed:** about 1 GB less RAM than the 3B, but **not measurably faster** here: on this laptop the bottleneck
was memory pressure and reading the prompt, not the model size alone.

**Decision:** rejected. For a school assistant, a wrong fact is worse than an incomplete one, and 5 invented facts
against 0-1 is a large, real difference (not run-to-run noise).

---

## `qwen2.5:3b`: cites reliably, drops conditions

**Runs:** Phase 2 rounds 1-4 ([02-chatbot.md](02-chatbot.md)); Phase 3 `generation-baseline`, `-baseline-v2`,
`-topk3`, `-final` ([reports](../../chatbot/reports/)).

**Strengths**
- **Cites its sources**: 14/15 answerable questions cited the expected document; the footer and the web page can show
  real sources.
- **Copies figures exactly at the right settings**: deadlines, dates, steps (PRC-02, TTB-03, ERP-02 correct in all
  three 3B runs at top-k 4; the 50/30/20% installment split was exact in every Phase 2 round after the repeat-penalty fix).
- **Refuses well**: 4 of 5 unanswerable questions refused in every Phase 3 run (the fifth, "Will I pass my resit?",
  usually declines to predict but restates the rules).
- Strong on procedures with numbered steps (ERP 5/6, procedures 5/6, timetables 3/3 fully correct across the three
  top-k 4 runs).

**How it fails**
- **Drops conditions and caveats** (the most common error): "365,000" without "level not specified" (FIN-01 failed in
  all four 3B runs: three false refusals, one caveat dropped, failure 30); the Top-Up students' step presented as for everyone
  (ADM-01, failure 19); password-reset advice given for "ERP not working" (failure 18).
- **Incomplete lists**: the 6 ICT Master's without the 3 business Master's (failure 17).
- **Blends cases in one passage**: a superseded deadline (19 instead of 23 November, failure 28), the special-resit
  rule given for a normal resit (failure 29), roles of two offices swapped (failure 27).
- **Invents contact details when redirecting**: "contact the Finance office at finance@ictuniversity.edu.cm" in
  most runs of NEG-02 (Phase 2 rounds 3-4, Phase 3 baseline, v2 and final; failures 13, 15). Since Phase 2 the address is **removed by code** before display, so
  it never reached the student in Phase 3.
- **Invents names when translating to French**: "Université de Technologie d'Ichoua-Tchokwe", "ICTE", "ERP
  (Electronic Registration Process)" (failures 11, 14, 24-26). Fixed by giving the exact name in the per-question
  instructions (correct in the final run).
- **Sensitive to settings**: a repeat penalty of 1.15 corrupted a copied date ("November 20th to December 3rd",
  failure 10); without a length cap it looped on a French list (failure 7). Both fixed (1.05, 400-token cap, loop guard).
- **Varies between runs**: with identical passages, 14 of 20 answers changed between two unseeded runs (failure 33);
  a fixed seed makes answers match for most of their length.

**Why (likely):** it copies when the passage *looks* like the answer, and summarises when it has to combine; in
summarising, short qualifiers are the first thing lost. Redirection and translation make it compose text instead
of copying it, which is where it invents. See [why models behave this way](failure-log.md#why-models-behave-this-way).

**Cost / speed:** about 2.2 GB in Ollama + 1.6 GB for e5 in the chatbot: fits next to browsers and VS Code. First
words after about 11-16 s, full answer about 30-35 s.

**Decision:** kept as the default. Its errors are mostly *incomplete or over-general* rather than invented, and the
invented kind (contacts) is caught by code. The remaining errors need a careful reader: that's what the 7B test is for.

---

## `qwen2.5:7b`: pending

**Why test it:** the 3B's remaining errors (dropped conditions, incomplete lists, blended cases, French names) are
reading-comprehension errors, which larger models generally make less often. Whether it does on our questions is
unknown until measured.

**What to expect (estimates, not measurements):** about 5-5.5 GB in Ollama, so about 7-7.5 GB for the whole chatbot:
more than the 5.7 GB free with browsers open, so browsers must be closed during the run. On a CPU, writing speed is
limited mostly by reading the model's weights from memory; at about 2.5x the 3B's size, expect about 2-2.5 tokens/s,
first words after about 40-50 s, a full answer in about 1.5-2 minutes.

**Plan:** the same 20 golden questions (`CHAT_MODEL=qwen2.5:7b python -m chatbot.eval_generation --label qwen7b --live`)
with browsers closed, memory and swap sampled every 2 s, every answer checked against its sources. Decision rule: if
it fixes the finance and list errors without inventing anything new, offer it as an optional "quality mode"
(`CHAT_MODEL=qwen2.5:7b`) with the 3B staying the default; if it is barely better, the 3B stays alone.

*This section will be replaced by the measured profile.*

---

## The embedding model (for completeness)

`intfloat/multilingual-e5-large` (via fastembed, 1024 dimensions) finds the passages; it doesn't write answers.
About 1.6 GB of RAM in the chatbot process; similarities cluster high (0.79-0.89), so the confidence threshold was
recalibrated to 0.81 (0.64 was for the cloud model, [01-local-setup.md](01-local-setup.md)). It finds the right
document in the top 5 for 94% of covered golden questions, and is weaker in French (20/26 vs 26/26 on the same
questions, [report](reports/french-vs-english-retrieval.md)). It was not changed in this project: the schema and the
shared index are built around it.
