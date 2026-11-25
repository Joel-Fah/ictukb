# Failure log

Every failure we observed while building the assistant: what happened, what the source actually says, why it
happened, what we changed, and whether it's fixed. Model answers were checked by hand against the source documents.
Transcripts are in [reports/](reports/).

**Types:**
- **Invented fact**: something stated that is in no source (the dangerous kind).
- **Distorted fact**: a fact from the source, changed.
- **Over-generalised**: a sourced statement applied beyond its condition.
- **Incomplete**: a correct answer missing items that were in the passages.
- **Format/noise**: no factual error, but output that misleads or clutters.
- **System**: a failure of our setup, not of the model.

| # | When | Question | What happened | Source says | Type | Root cause | Fix | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Phase 0 | (setup) | `ictkb index` from the README fails: "ADMIN_TOKEN is not set" | - | System | Repo default `EMBEDDING_PROVIDER=worker` needs the maintainer's token | `EMBEDDING_PROVIDER=fastembed` in `.env`; reported upstream [#2](https://github.com/Egbemichel/ictukb/issues/2), docs PR [#8](https://github.com/Egbemichel/ictukb/pull/8) | Worked around locally |
| 2 | Phase 1 | (setup) | The 2.2 GB e5 model is stored in `/tmp`, so it would re-download after each reboot and break offline use | - | System | fastembed's default cache dir is `tempfile.gettempdir()` | `export FASTEMBED_CACHE_PATH=$HOME/.cache/fastembed`; the chatbot sets it itself; reported [#3](https://github.com/Egbemichel/ictukb/issues/3) | Fixed in chatbot; manual for `ictkb` |
| 3 | Phase 3 | (setup) | `eval/run_eval.py` hung for 5 min at 3% CPU | - | System | **Failure 2 again**: the export was forgotten in that shell, so fastembed started re-downloading into `/tmp` | Killed, removed the partial download, reran with the export | Lesson: every shell that runs `ictkb`/`eval` needs the export |
| 4 | Phase 1 | All 5 no-answer golden questions | Marked "high confidence" (no-answer correctness 0%) | - | System | `MIN_SIMILARITY=0.64` was tuned for the cloud model; e5 scores everything 0.79-0.89 | Measured and set 0.81: keeps 100% of answerable, refuses 3/5; reported [#9](https://github.com/Egbemichel/ictukb/issues/9) | Fixed (3/5); 2 left to the model |
| 5 | Phase 1 | "What is my current fee balance?" / "Will I pass my resit?" | Similarity 0.848 / 0.833, above any usable threshold | No personal data exists | System (limit) | Similarity measures topic, not whether the specific fact is there | The model's rules must refuse them; tested in Phase 2 | Refused correctly in runs 2-4 |
| 6 | Phase 1 | "Comment payer les frais de scolarité ?" | Top results include graduation and travel fares; English equivalent returns only fee documents | - | System (limit) | Content is English-only, so keyword search can't match French words | None yet | Open (Phase 3) |
| 7 | Run 1 | "Quels sont les programmes de master proposés ?" | The same line repeated hundreds of times; never stopped | - | Format/noise (severe) | No answer-length cap; near-greedy decoding of a 3B model | 400-token cap, repetition guard (3 identical lines → stop) | Fixed (unit-tested) |
| 8 | Run 1 | "What documents do I need for a Bachelor application?" | Copied "[SEE OUR PROGRAMS](...) [APPLY NOW](...)", 7 repeated citations | Website navigation buttons in the crawled page | Format/noise | Raw Markdown links in crawled pages | Links reduced to plain text before the model sees them | Fixed |
| 9 | Run 1 | "How do I get my transcript?" | Added a paragraph on transfer students | Unrelated passage scored 0.820 vs best 0.884 | Format/noise | Weak passages given to the model get used | Drop passages > 0.05 below the best | Fixed |
| 10 | Run 2 | "Can I pay my fees in installments?" | "second installment is from November 20th to **December 3rd**" | "20 to 30 November 2026" | **Invented fact** | Our repeat penalty 1.15 penalised recently used tokens and corrupted the copied date. Reproduced every time at 1.15; correct at 1.05 | Repeat penalty back to 1.05; code check flags numbers/months not in the sources | Fixed; check unit-tested with this exact answer |
| 11 | Run 2 | "Quels sont les programmes de master proposés ?" | Programme names translated; acronyms "ICTE", "ICTP" invented | English names, no such acronyms | **Invented fact** | Translating names into French | Per-question rule: keep names in English, don't translate or expand | Fixed in run 4 |
| 12 | Run 2-3 | "Comment payer les frais de scolarité ?" | Correct answer followed by "Je n'ai pas cette information" + contacts | - | Format/noise (our bug) | Model wrote `[Venteurs "finance-installments"]`; our parser needed `[id]`, found no citation, treated it as a refusal | Citations matched anywhere; footer chosen by refusal detection | Fixed |
| 13 | Run 3 | "What is my current fee balance?" | "contact the Finance office at **finance@ictuniversity.edu.cm**" | No such address anywhere in the knowledge base | **Invented fact** | Asked to redirect the student, the model composes a plausible address | Rule: no contact details not in the sources (not enough, see 15); stream redaction | Fixed by code (see 15) |
| 14 | Run 3 | "Quels sont les programmes de master proposés ?" | "Université de Technologie d'Ichoua-Tchokwe"; BMS called "Faculté des Sciences et Technologies" | "ICT University"; BMS = Business Management and Sustainability | **Invented fact** | Translating/expanding names | Rule placed next to "Answer in French": keep names in English | Fixed in run 4 (watch in Phase 3) |
| 15 | Run 4 | "What is my current fee balance?" | Invented the same finance@ address again despite the new rule | - | **Invented fact** | Rules reduce, but don't prevent | Streaming holds back the current word and replaces any email/URL not in the sources with "[contact removed: not in the sources]" | Fixed by code; unit-tested on this answer; not yet seen live |
| 16 | Run 3 | "Will I pass my resit?" | "if your current total plus the resit score does not exceed 79, you will pass" | The 79 is a cap on the final total, not a pass condition | Distorted fact | Reasoning beyond the text | None specific | Gone in run 4 (model variability) |
| 17 | Run 1-4 | "Which Masters programs are offered?" | Lists the 6 ICT Master's, omits the 3 BMS Master's | The passage lists all 9 | Incomplete | 3B model drops part of a list | Rule "give every item"; helped in French (complete in run 4), not in English | Open (Phase 3) |
| 18 | Run 1-4 | "Who do I contact if the ERP is not working?" | "contact the Database Administrator or your office", given as general advice | That advice is for "forgotten password and no access to your email" | Over-generalised | Condition dropped | None specific | Open (Phase 3) |
| 19 | Run 4 | "What documents do I need for a Bachelor application?" | All documents "forwarded to the Department of Transcript and Verification" | Only Top-Up files are forwarded | Over-generalised | Condition dropped | None specific | Open (minor) |
| 20 | Run 4 | "At what time does the canteen open?" | Correct refusal, but no official contacts shown | - | Format/noise (our bug) | Refusal wording "is not provided" not in our phrase list | Phrase added | Fixed (unit-checked) |
| 21 | Phase 1 / correction | "Which Masters programs are offered?" | We first logged "Information Systems and Networking" as invented | `programs-masters` spells it out | **Our error** | We checked only one of the passages the model saw | Check every passage in the context before calling something invented | Corrected |
| 22 | Phase 3, 1.5b | PRC-09 "How long does a transcript take?" | "approximately **2-3 business days**" | Processing time not stated | **Invented fact** | Small model fills a gap | Model rejected. The number check **missed it**: the digits 2 and 3 appear elsewhere in the passages | Open limit of the check |
| 23 | Phase 3, 1.5b | FIN-06 "What payment methods are accepted?" | "The canteen accepts **cash and mobile money**" | Section body is `[[TO FILL]]`; the words are in its heading "(cash, mobile money, other)?" | **Invented fact** | An empty section's heading read as content | Passages with nothing but placeholders are dropped; if none remain, fallback without the model | Fixed (FIN-06 correct in v2 and final; unit-tested) |
| 24 | Phase 3, 1.5b and 3B | MHP-01, VAR-01 | "ERP (**Electronic Records Processing**)", "ERP (**Electronic Registration Process**)" | Never expanded in the sources | **Invented fact** | Models expand abbreviations | French rule "do not expand abbreviations such as ERP"; not seen in the final run | Mitigated (prompt only) |
| 25 | Phase 3, 3B v2/topk3/seed check | VAR-02 (French) | "Université de Technologie", "Université Internationale des Technologies et des Communications" | "ICT University" | **Invented fact** | Translating the school's name (also #14); with the seed it appeared every time | Per-question rule: 'Call the university "ICT University"' | Fixed in final run (watch) |
| 26 | Phase 3, 3B v2 | VAR-01 (French) | Form "signé et apposé **par la poste**" | Stamps of the Finance Office and the Head of Department or Dean | **Invented fact** | Mistranslation of "stamped" | None specific | Not seen in final |
| 27 | Phase 3, 3B v2 | ADM-01 | "The **Admissions Office** evaluates which credits can be transferred" | The Deans evaluate; Admissions then admits | Distorted fact | Roles swapped between two named offices | None specific | Varies by run (correct in topk3, final) |
| 28 | Phase 3, 3B topk3 | PRC-02 "What is the course registration deadline?" | "**Thursday 19 November 2026**" | Latest notice: Monday 23 November (19 Nov was an earlier notice) | Distorted fact | Several dates in the passage; the model picked a superseded one. The number check can't catch it (the date *is* in the passages) | None; correct in the other 3B runs | Open: a human-only catch |
| 29 | Phase 3, 3B topk3/final | MHP-02 "How do I resit, and what will it cost?" | Normal resit "a fresh mark **out of 100**" | Normal: out of 70 added to CA; out of 100 is the special resit | Distorted fact | Two cases in one section, mixed | None specific | Open |
| 30 | Phase 3, all 3B runs | FIN-01 "How much are tuition fees for the Bachelors program?" | Refuses (or, at top-k 3 and with 1.5b, "365,000 is the Bachelor tuition") | "XAF 365,000 ... the level it applies to is not specified" | False refusal / dropped condition | The answer is a fact with a caveat; models either drop the fact or the caveat | Content could state the caveat as its own question-style section | Open |
| 31 | Phase 3, 3B final | ERP-03 "I forgot my ERP password" | "You do **not need to contact** the ERP support ... handled internally" | Contact the Database Administrator if you lost access to your email | Invented claim | Model adds reassurance | None specific | Open |
| 32 | Phase 3, topk3 | FIN-06, MHP-03 | Refused / tuition missing | The needed passage was ranked 4th | System | top-k 3 cut it | Kept top-k 4 | Fixed by decision |
| 33 | Phase 3 | (evaluation) | With identical passages, **14 of 20 answers changed** between two runs | - | System (measurement) | Temperature 0.1 still samples; no fixed seed | `CHAT_SEED=42`; answers now match for most of their length but can still diverge late (prompt cache, multi-threaded arithmetic) | Mitigated |
| 34 | Phase 3 | (evaluation) | During one run both models were in memory; swap reached 8 GB and the run slowed | - | System (our mistake) | Ollama keeps a model loaded 30 min after use (`keep_alive`), so the 1.5b stayed next to the 3B | Unloaded it (`keep_alive: 0`); lesson: unload models between experiments | Fixed |
| 35 | Phase 3 | (evaluation) | First word "3x faster" with top-k 3 | - | System (measurement) | Mostly Ollama's prompt cache, not the setting (prompt only 15% shorter) | Report full-answer time and prompt read speed, not just time to first word | Documented |

## What the log shows

- **All invented facts were contact details, dates, or names in translation**: exactly the things a student would act on.
- **Two of the worst failures were caused by our own settings or code** (10: repeat penalty; 12: citation parser).
  Every change needs re-checking against sources, not just "the answer looks better".
- **Instructions alone weren't enough** for the invented email (13 → 15). What reliably works is a check in code
  that doesn't depend on the model obeying.
- **Fixes can be model-variable**: 16 disappeared without a specific fix, and the live re-check of 15 didn't
  reproduce the email at all. One clean run proves little; regression tests on recorded bad answers prove more.
  Phase 3 measured this directly (33): most answers change between unseeded runs.
- **The redactor works live**: in the baseline, v2 and final runs the model wrote the invented finance@ address
  again, and each time the student saw "[contact removed: not in the sources]" instead.
- **What's left is subtle**: Phase 3's open entries (28-31) are facts from the passages applied to the wrong case,
  a superseded date, a dropped caveat. No string check catches those; they need a human, a stronger model, or
  content written one case per section.
