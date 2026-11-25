# 02. The terminal chatbot (Phase 2)

**Purpose:** turn the local knowledge base from Phase 1 into an assistant that answers student questions in plain
language, **only from the school's documents**, cites them, and says "I don't know" (with official contacts) instead
of guessing. Everything runs on the laptop: e5 for search, `qwen2.5:3b` through Ollama for writing the answer.

**Result in short:** after four rounds of testing and fixes, 12 test questions give grounded answers or correct
refusals in English and French. Fees, dates and amounts are copied exactly, and invented contact details are removed
by code before the student sees them. Two answers are still incomplete or over-general (a limit of the 3B model).
A typical answer takes about 34 s on this CPU (first words after about 17 s).

Code: [chatbot/](../../chatbot/) ([README](../../chatbot/README.md)). Run with `python -m chatbot.chat`.

---

## How an answer is produced

```
question
  │ 1. detect the language (English/French) from common words and accents
  │ 2. search the local index: top 4 passages (hybrid: e5 vectors + keywords), about 0.1-0.3 s
  ▼
best similarity < 0.81? ──yes──► fallback: "not in the knowledge base" + official contacts
  │ no                           (read from the about-contacts document; the model is NOT called)
  ▼
 3. prepare the passages: drop passages much weaker than the best one, replace [[TO FILL]] with
    "(not documented yet)", reduce web links to plain text, trim to 1200 chars each / 4000 total
 4. send rules + passages + question to qwen2.5:3b (Ollama), stream the answer
    - the word being written is held back until it's complete; an email or web address that isn't
      in the passages is replaced with "[contact removed: not in the sources]"
    - stop if the same line repeats 3 times, or after 400 tokens
 5. after the answer, checks done by code (not by the model):
    - numbers and months in the answer that aren't in the passages → warning
    - cited document ids → "Sources:" list with real titles, links and verification dates
    - draft or stale sources → notes
    - the model refused → official contacts; it cited nothing → list the passages it was given
```

**Why so many checks in code?** A 3B model follows instructions most of the time, not all of the time. Rules in the
prompt reduce mistakes; checks in code *guarantee* that certain mistakes (invented emails, repeated lines,
missing sources) never reach the student unflagged.

### Design choices

| Choice | Why |
|---|---|
| Retrieval in-process (`ictkb.search.search()`) | No API server to run; e5 is loaded once (1.6 GB) |
| No conversation memory | A 4096-token window is small; history would push out the passages. Each question stands alone |
| Language detection by word lists | No extra dependency; enough for short questions in two languages |
| Temperature 0.1, repeat penalty 1.05 | Factual, repeatable answers. 1.05 is Qwen 2.5's own default; a higher value corrupted dates (see run 2) |
| Sources printed by code | The model only writes ids; titles, links and dates come from the database, so they're always real |
| Refuse below `MIN_SIMILARITY` without calling the model | A refusal that skips the model can't hallucinate, and it's instant |
| No new dependencies | Standard library + `httpx`, `psycopg` (already in the repo) |

---

## Testing: 12 questions, 4 rounds

The acceptance test from the brief asks for at least 10 questions, including 2 in French and 2 the knowledge base
can't answer. We used 12:

| # | Question | Type |
|---|---|---|
| 1 | What documents do I need for a Bachelor application? | answerable |
| 2 | Can I pay my fees in installments? | answerable (amounts, dates) |
| 3 | How do I get my transcript? | answerable |
| 4 | Which Masters programs are offered? | answerable (list) |
| 5 | Who do I contact if the ERP is not working? | answerable |
| 6 | How do resits work? | answerable |
| 7 | Comment payer les frais de scolarité ? | French |
| 8 | Quels sont les programmes de master proposés ? | French (list) |
| 9 | What is my current fee balance? | unanswerable, but scores above the threshold |
| 10 | Will I pass my resit? | unanswerable, but scores above the threshold |
| 11 | What's the weather in Yaounde today? | unanswerable, off-topic |
| 12 | At what time does the canteen open? | only a draft with `[[TO FILL]]` exists |

Every answer was checked by hand against its source documents. Full transcripts are in [reports/](reports/).

### Run 1: the model got stuck repeating ([transcript, trimmed](reports/phase2-acceptance-run1.txt))

- Facts were right where checked (fees, resits), but answers were padded with unrelated passages, copied website
  buttons ("SEE OUR PROGRAMS", "APPLY NOW") and repeated citations.
- **Question 8 (French) looped**: the same line hundreds of times. There was no length limit, so it would never
  stop on its own; the run was stopped by hand.
- **Fixes:** a 400-token cap, a repetition guard, dropping passages scoring more than 0.05 below the best, links
  reduced to text, rules "answer only what was asked" and "keep names as written".

### Run 2: an invented date ([transcript](reports/phase2-acceptance-run2.txt))

- The loop was gone; the first words came sooner (shorter prompts).
- **Question 2 said the second installment is due "November 20th to December 3rd"**; the source says
  20 to 30 November 2026. **French question 8 translated programme names and invented acronyms.**
- **Cause of the wrong date:** we had raised the repeat penalty to 1.15 to fight loops. It penalises tokens the
  model has just used, which can corrupt numbers that should be copied. Asking the same question at 1.15 and at
  1.05 confirmed it: 1.15 gives the wrong date every time; 1.05 copies it exactly.
- **Fixes:** repeat penalty back to 1.05; a code check that flags any number or month not found in the passages
  (it prints "Warning: ... not in the sources ...: 3, december" on the bad answer); citations recognised in any
  format (a garbled citation had triggered a false "I don't have that information").

### Run 3: an invented email address ([transcript](reports/phase2-acceptance-run3.txt))

- Question 2 was now exactly right, and question 1 more complete.
- **Question 9 refused correctly but told the student to write to `finance@ictuniversity.edu.cm`, an address that
  exists nowhere in the knowledge base. French question 8 invented a university name** ("Université de Technologie
  d'Ichoua-Tchokwe").
- **Fixes:** rule "never write an email, phone or web address that isn't in the sources"; for French questions,
  "keep the names of the university, faculties, programmes and offices in English, don't translate them", placed
  next to "Answer in French"; the code check extended to emails and URLs; the footer chosen by what the model did
  (refusal → contacts; no citation → list the passages given).

### Run 4: the current state ([transcript](reports/phase2-acceptance-run4.txt))

| # | Verdict (checked against the source) |
|---|---|
| 1 | Correct and complete (certified and authenticated copies, HND for Top-Up). One step over-generalised: "forwarded to the Department of Transcript and Verification" applies to Top-Up files only |
| 2 | **Correct**: 50/30/20%, XAF 365,000 → 182,500 / 109,500 / 73,000, copied exactly |
| 3 | **Correct** |
| 4 | **Incomplete**: the 6 ICT Master's are right, the 3 BMS Master's (Applied Statistics and Demography, Development Planning, iMBA) are missing although they were in the passage |
| 5 | **Over-generalised**: "contact the Database Administrator or your office" is the source's advice for a forgotten password without email access, given as general advice |
| 6 | **Correct** |
| 7 | **Correct** (French), dates and amounts exact |
| 8 | **Correct and complete** (French), all 9 programmes with their English names |
| 9 | Refused correctly, but **invented `finance@ictuniversity.edu.cm` again**; flagged by the check. Since then, the stream redacts it before display (unit-tested with this exact answer). In a later live check the model didn't write an email at all, so the redaction hasn't been seen live yet |
| 10 | **Correct**: explains the rules (eligible below 50, resit out of 70, capped at 79) and says it can't predict the result |
| 11 | **Correct**: below the threshold, no model call, fallback with official contacts |
| 12 | **Correct refusal** (the hours are `[[TO FILL]]`), with a draft warning. The official contacts weren't shown because the refusal wording ("is not provided") wasn't recognised; fixed and unit-tested since |

**Acceptance:** answers are grounded and cited, the three unanswerable questions and the draft-only one are refused,
French works, and every fee, date and amount is copied exactly. **Two answers are weaker than they should be
(4 incomplete, 5 over-generalised)**: those are the model's limits, recorded for Phase 3. The one invented fact
in run 4 (the email) is now removed by code before display.

---

## Speed (run 4, i7-10710U, no GPU)

| Measure | Value |
|---|---|
| Start-up (load e5 + model) | about 10-15 s |
| Retrieval per question | 0.1-0.3 s |
| Reading the prompt (about 650-850 tokens) | median 42 tokens/s → **first words after a median of 16.8 s** (5.9-28.2 s) |
| Writing the answer | 5.2-6.1 tokens/s |
| Whole answer | **median 34 s** (13-67 s) |
| Off-topic refusal (no model call) | instant |

Reading the prompt is the bottleneck. Ollama sometimes reuses work from the previous prompt (first word after
0.5 s when the same passages come back), which is why the numbers vary so much.

---

## Unit tests

`python -m pytest chatbot/tests` (21 tests, no database or model needed). Several use the exact bad outputs from
runs 2-4 (the invented date, the invented email, the garbled citation, the loop) as regression tests, so these
mistakes stay caught.

## Known limits (input to Phase 3)

1. **Lists can be incomplete** (Q4) and **advice can be over-generalised** (Q5). Options: show more of a long
   passage, test `qwen2.5:7b` (better reading, but about 2x slower and +2.5 GB RAM), or a different 3-4B model.
2. **Speed**: about 34 s per answer. Options: shorter passages (`CHAT_MAX_CHUNK_CHARS`), fewer passages
   (`CHAT_TOP_K=3`), `qwen2.5:1.5b`, or Ollama thread settings. Each to be measured against answer quality.
3. **French retrieval** is weaker than English (Phase 1), even though French answers are now good when the right
   passage is found.
4. The model sometimes cites passages it barely used, or writes citations in odd formats; the footer handles it,
   but the inline text can look messy.
