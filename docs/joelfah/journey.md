# The journey: building a local ICT University assistant

An overview of how the assistant was built, what went wrong, what we traded off, and what we learned. Details live
in the phase pages ([00](00-inspection.md), [01](01-local-setup.md), [02](02-chatbot.md)), the
[failure log](failure-log.md) and the [reports](reports/).

## 1. The goal and its constraints

A chatbot that answers prospective and current students' questions about ICT University (admissions, fees,
registration, ERP, campus, student life) **from the school's own knowledge base, with sources**, and says
"I don't know" rather than guessing. It also has to work:

- **on a student laptop**: Intel i7-10710U (6 cores), 15 GiB RAM of which only 3-6 GiB is usually free (browsers,
  VS Code), **no GPU**;
- **with no cloud service and no paid key**, and with the network off after setup;
- **with a minimal stack**: no new Python dependencies.

These constraints shaped every choice below.

## 2. The process

| Phase | What we did | Key outcome |
|---|---|---|
| 0. Inspect | Measured the laptop, read the repo, chose the stack | Small model (`qwen2.5:3b`), Docker for the database, retrieval called directly in Python |
| 1. Local knowledge base | Docker, local e5 embeddings, indexed 77 documents + crawled 33 website pages (733 chunks) | Right document in the top 5 for 94% of golden questions; no network traffic; threshold recalibrated |
| 2. Chatbot | Built `chatbot/`; tested 12 questions over 4 rounds, checking every answer against its sources | Grounded, cited answers in English and French; refusals work; invented contact details removed by code |
| 3. Measure and tune | 5 runs of 20 golden questions, every answer checked by hand; model, passages, seed | Final: 8 correct / 4 partial / 1 wrong / 2 refused of 15; 4/5 unanswerable refused; 3B kept, top-k 4 kept; finance and multi-hop weakest |
| 4. Contribute | Sent 6 issues + 2 docs PRs; prepared 9 more issues covering all 35 uncovered golden questions, content-writing patterns, French questions, multi-hop failures | [04-contributions.md](04-contributions.md) |
| 5. Package | `setup.sh` + `run.sh` (two commands), a local web page with streaming answers | Re-run of setup in 15 s; web page answers with the same safeguards; 29 unit tests |

## 3. Main challenges

1. **The repo assumed the cloud.** The default embedding provider calls a Cloudflare service and needs the
   maintainer's token. Going local meant switching to fastembed and recalibrating everything that depended on the
   cloud model (the confidence threshold), plus finding traps such as the `/tmp` model cache (it bit us twice).
2. **Similarity can't tell "topic covered" from "fact present".** With e5, "What is my fee balance?" scores
   higher than some real questions, because fee documents exist. No threshold separates them; the refusal has to
   come from the model reading the passages, which a 3B model mostly, but not always, does.
3. **A small model hallucinates in specific, predictable places**: contact details when it redirects the
   student, dates when its decoding settings are off, names and abbreviations when it translates or explains,
   and gaps it fills when a section is empty. See the [failure log](failure-log.md): 37 entries, 10 of them invented
   facts (5 from the 1.5b model alone in one run).
4. **Speed on a CPU.** Reading a 650-850-token prompt takes most of the time: first words after about 17 s, a full
   answer in about 34 s. Memory pressure (swap) makes it worse and variable.
5. **French.** The knowledge base is English-only, so French questions retrieve worse, and French answers tend to
   translate names, which is where invented names appeared.
6. **Evaluating honestly.** "Looks right" was wrong more than once; we even misjudged one answer ourselves (failure
   21). Only a line-by-line check against every passage the model saw was reliable.
7. **Noise in the measurements.** With identical passages, 14 of 20 answers changed between two runs; timings
   changed up to 10x with the machine's memory state and Ollama's prompt cache. Small differences between
   configurations were not real. Only large, repeated effects (or a mechanism we could see) justified a decision.
8. **The errors that remain are subtle.** By the end, the code stops invented contacts, loops and out-of-source
   numbers, but not a superseded date that *is* in the passage, a rule applied to the wrong case, or a dropped
   caveat. These need a human check, a stronger model, or content written one case per section.

## 4. Trade-offs we made

| Decision | We gained | We gave up |
|---|---|---|
| Local only (e5 + Ollama) | Privacy, no cost, works offline | Speed (34 s answers) and quality of a 3B model vs cloud models |
| `qwen2.5:3b` instead of 7B as the default | Fits next to e5 with the browsers open; answers in about 35 s | Measured later: the 7B got 13/15 right against 8/15 and fixed the dropped-caveat and incomplete-list errors, but takes about 62 s and needs the browsers closed ([models.md](models.md)) |
| Similarity threshold 0.81 | Off-topic questions refused instantly, without the model | 2 of 5 unanswerable questions pass; relies on the model to refuse them |
| Checks in code (redaction, number check, loop guard) | Guarantees that don't depend on the model obeying | More code to maintain; the number check can flag a correct number written differently |
| Drop passages far below the best one | Less padding, shorter prompts, faster | A relevant passage that scores low is lost |
| Stream the answer (hold back only one word) | Students see text as it's written | Contact details can only be checked word by word, not with full-sentence context |
| No conversation memory | Every question gets the full context window | Follow-up questions ("and how much is it?") don't work |
| Staging index (drafts included) | Coverage 84/98 vs 63/98 | Drafts can contain `[[TO FILL]]` gaps; mitigated with "(not documented yet)" and draft warnings |
| Answer in the user's language | French speakers served | Translation is where the model invented names; names are now kept in English |
| `qwen2.5:3b` over `qwen2.5:1.5b` (Phase 3) | 0-1 invented facts per run instead of 5; citations | No speed gain from the smaller model on this swapping machine anyway |
| 4 passages over 3 | The needed passage is often 4th | A slightly longer prompt |
| Fixed seed | The same question gets (almost) the same answer; fairer comparisons | One fixed draw: if it's a bad one, it's consistently bad (seen with the French name before the fix) |
| Drop `[[TO FILL]]`-only passages | No answers invented from empty sections' headings | A heading that would at least tell the student "this exists" is not shown |

## 5. Lessons

1. **Measure on your own setup.** Thresholds, speed, and failure modes from someone else's setup (cloud model, other
   hardware) didn't transfer.
2. **Put guarantees in code, use the prompt for tendencies.** The invented email survived a direct rule; a
   15-line redactor ended it.
3. **Every "improvement" can break something else.** A higher repeat penalty stopped loops and invented a date.
4. **Keep the bad outputs.** Each recorded failure became a regression test, so it stays caught.
5. **Check against every passage before calling something a hallucination**, and correct the record when wrong.
6. **Contribute what you learn.** Several local problems (admin token, `/tmp` cache, threshold, open port) were
   problems for every contributor, so they went upstream as issues.
7. **Know your noise before comparing.** Run the same configuration twice before believing a difference between two
   configurations; record the machine's state with every timing.
8. **Bad content makes bad answers.** The weakest answers (finance, multi-hop) trace back to sections that mix cases,
   hold a fact and its caveat in one sentence, or are empty drafts. Better content will help more than prompt tweaks.

## 6. Still open

- **Content** (Phase 4): the weak finance and multi-hop answers point at concrete content fixes; the missing
  `campus-office-directory`; French headings and golden questions.
- **Unanswerable but on-topic questions** would benefit from an answer-verification step like upstream's Worker.
- **More runs per configuration**, including a second `qwen2.5:7b` run to confirm its one-run lead.
- **Human confirmation** of the verdicts in `chatbot/reports/generation-*.csv`.

Phase 3 details: [03-evaluation.md](03-evaluation.md) and [chatbot/BENCHMARKS.md](../../chatbot/BENCHMARKS.md).
