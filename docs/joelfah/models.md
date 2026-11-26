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
| Download | 986 MB | 1.9 GB | 4.7 GB |
| RAM in Ollama (4096-token context) | 1.17 GB (measured) | 2.17 GB (measured) | 5.1 GB (measured; 5.4 GB peak resident) |
| Runs evaluated | 1 (20 questions) | 4 Phase 3 runs (80 answers) + 4 Phase 2 rounds (12 questions) | 1 (20 questions) + 2 list questions |
| Answerable, of 15: correct / partial / wrong / refused | 9 / 2 / 3 / 1 | 8 / 4 / 1 / 2 (final run) | **13 / 1 / 0 / 1** |
| No-answer questions, of 5 | 3 refused, 1 grounded redirect, 1 wrong | 4 refused, 1 partial (final run) | 4 refused, 1 grounded redirect |
| Invented facts shown to the student | **5** in one run | 0-1 per run (contacts always removed by code) | **0** (and no contact invented, so nothing to remove) |
| Cited the expected document | **1/15** | 14/15 | 14/15 |
| Median first words / full answer | 17.1 s / 33.0 s (CPU busier during this run) | 10.8 s / 34.8 s (final); 15.5 s / 30.5 s (baseline) | **36.1 s / 62.3 s** (browsers closed, no swap) |
| Writing speed | 6.5 tokens/s | 4.5-7.5 tokens/s depending on load | 3.2-3.4 tokens/s |
| Verdict | **Rejected** | **Kept** (default) | **Optional quality mode** (proposed) |

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

## `qwen2.5:7b`: reads conditions, but slow

**Runs:** `generation-qwen7b` (the 20 questions, [report](../../chatbot/reports/generation-qwen7b.md),
[verdicts](../../chatbot/reports/generation-qwen7b.csv)), and the two list questions behind failures 17 and 19
(PRG-02, ADM-02) on both the 7B and the 3B with today's settings (`generation-qwen7b-lists`, `-qwen3b-lists`).
2026-11-26, after a reboot, browsers closed: 10 GB free at the start, 3.4 GB at the lowest, **swap never used**
(sampled every 2 s, [memory.csv](../../chatbot/reports/generation-qwen7b.memory.csv),
[machine state](../../chatbot/reports/generation-qwen7b.machine.txt)).

**Why test it:** the 3B's remaining errors (dropped conditions, incomplete lists, blended cases, French names) are
reading-comprehension errors, which larger models generally make less often.

**Strengths**
- **Keeps conditions and caveats**, the 3B's most common error:
  "365,000 ... the amount for the Bachelor's is not specified" (FIN-01, failed in all four 3B runs), the same caveat
  in French (VAR-02), the transfer/Top-Up step kept as such (ADM-01, 3B failure 19).
- **Keeps cases apart**: resit registration with "the fee is shown in the ERP for each course", without the
  special-resit "out of 100" rule the 3B mixed in (MHP-02, failure 29); the latest registration deadline, not a
  superseded one (PRC-02).
- **Complete lists**: all three installment amounts plus "the other dates are not published" (FIN-05); all 9 Master's
  programmes where the 3B, asked again the same day, still gave 6 (PRG-02, failure 17).
- **Says exactly what's missing** instead of filling the gap: "the processing time is not stated in the ERP
  manual" (PRC-09), "the cost is not explicitly stated but can be found in the ERP" (MHP-02).
- **No invented facts, names or contacts** in 22 answers: it never produced the `finance@` address the 3B invented in
  most NEG-02 runs; the university's name stayed "ICT University" in French; no expanded "ERP".
- "Will I pass my resit?" (NEG-04): says it doesn't know, then explains accurately what the result depends on. The
  best answer to that question in any run.

**How it fails**
- **One caveat still dropped**: for a Master's applicant, "the complete tuition is XAF 365,000" without "the level
  isn't specified" (MHP-03), the same error type as failure 30, but in 1 of 15 answers instead of most finance ones.
- Cites less completely in a two-document answer: the Master's requirements in MHP-03 were copied verbatim but not
  cited (only the fee document was).
- Treats "What is my current fee balance?" as "where do I see it" (My Fees in the ERP, verbatim from the source), like
  the 1.5b: grounded, but not the refusal the golden set expects (NEG-02).
- Cosmetic: a list item repeated as a group ("BMS Master's programs (...)"), "iMBA (iMBA)", its own "Sources:" line
  above ours (PRG-02); "formulaire de registration" (anglicised French, VAR-01).
- **It exposed a bug in our code (failure 36):** it ends complete answers with an honest "the dates of the first and
  third installments are not provided in the sources". Our refusal detector looks for phrases like "not provided in"
  anywhere in the answer, so it treated a correct, cited answer as a refusal: the "I don't have that information"
  contacts block was appended, the run counted it as refused, and the web page would have shown *Not in the knowledge
  base*. (Now fixed: such answers are labelled a *gap* and stay answers.) In all earlier runs, every cited answer that matched a refusal phrase really was a refusal (3B: FIN-01 and
  NEG-02); FIN-05 is the first complete answer to match, which is why this didn't show before.

**Why (likely):** more parameters give more room to represent "this fact applies only when..." while keeping the rules,
the passages and the question in view; the 3B, summarising under the same load, drops the qualifier first. Larger
instruction-tuned models also follow "say what isn't in the sources" more literally, which is why it flags gaps
precisely (and why it tripped our phrase-based detector). See
[why models behave this way](failure-log.md#why-models-behave-this-way).

**Cost / speed** (measured; the estimates were 2-2.5 tokens/s and 1.5-2 min):

| | 3B (final run) | 7B | 7B vs 3B |
|---|---|---|---|
| First words (median) | 10.8 s | 36.1 s | about 3.3x slower |
| Full answer (median) | 34.8 s | 62.3 s | about 1.8x slower |
| Writing | 4.5 tokens/s | 3.3 tokens/s | the 3B's final run had 5-8 GB in swap; it wrote 7.5 tokens/s in the baseline run |
| Reading the prompt | 23-124 tokens/s (thousands when cached) | 12-26 tokens/s (69 once, partly cached) | |
| RAM: Ollama + chatbot | 2.2 + 1.6 GB | 5.1-5.4 + 1.6 GB | needs the browsers closed (5.7 GB free with them open) |

The first question took 131 s, including loading the model; the slowest answer after that took 110 s (MHP-03, the
longest answer, 178 tokens).

**Is it better, or is it noise?** One 7B run against four 3B runs. Between two 3B runs with the same settings,
answers moved by 1-2 verdicts; the 7B is 5 correct answers above the best 3B run, and fixed the 3B's recurring errors
(FIN-01 in four of four runs, PRG-02 again today) rather than different questions at random. That is larger than the
noise we measured, but a second 7B run would make it solid.

**Decision (proposed, by the rule set before the test):** it fixes the finance and list errors and invented nothing
new, so it becomes an **optional quality mode**: `CHAT_MODEL=qwen2.5:7b ./chatbot/run.sh [--web]`, with browsers
closed. The 3B stays the default: twice the wait and twice the memory are too much for everyday use on this laptop.
Failure 36, which would have mislabelled its best answers on the web page, is fixed.

---

## The embedding model (for completeness)

`intfloat/multilingual-e5-large` (via fastembed, 1024 dimensions) finds the passages; it doesn't write answers.
About 1.6 GB of RAM in the chatbot process; similarities cluster high (0.79-0.89), so the confidence threshold was
recalibrated to 0.81 (0.64 was for the cloud model, [01-local-setup.md](01-local-setup.md)). It finds the right
document in the top 5 for 94% of covered golden questions, and is weaker in French (20/26 vs 26/26 on the same
questions, [report](reports/french-vs-english-retrieval.md)). It was not changed in this project: the schema and the
shared index are built around it.
