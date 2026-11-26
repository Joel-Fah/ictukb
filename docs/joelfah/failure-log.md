# Failure log

Every failure we observed while building the assistant: what happened, what the source actually says, why it
happened, what we changed, and whether it's fixed. Model answers were checked by hand against the source documents.
Transcripts are in [reports/](reports/).

**Types:**
- **Invented fact**: something stated that is in no source (the dangerous kind).
- **Distorted fact**: a fact from the source, changed.
- **Over-generalised**: a sourced statement applied beyond its condition.
- **Incomplete**: a correct answer missing items that were in the passages.
- **False refusal**: "I don't have that information" when the passages did contain it.
- **Format/noise**: no factual error, but output that misleads or clutters.
- **System**: a failure of our setup, not of the model.

Why each type happens is explained [after the table](#why-models-behave-this-way).

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
| 36 | 7B test | FIN-05 "What are the installment dates and amounts?" | A complete, cited answer followed by "I don't have that information ... Official contacts"; counted as refused | The answer was right: it ended with "the dates of the first and third installments are **not provided in** the sources" | Format/noise (our bug) | `is_refusal()` looks for refusal phrases anywhere in the answer, so an honest note about one missing detail marks the whole answer as a refusal; the web page would show *Not in the knowledge base* | `refusal_kind()` returns refusal / gap / none: a first-person refusal ("I do not have that information") anywhere, or an impersonal one ("not provided in") in the first sentence, is a refusal; an impersonal one later is a *gap*: the answer stays an answer (sources shown, amber *Check this answer*), and the contacts are introduced with "Some details are not in the knowledge base". A first try ("first sentence or under 250 characters") failed on recorded answers: it missed a 312-character 3B refusal and turned a short partial answer into a refusal | Fixed (unit-tested with the recorded answers; replayed on all 8 recorded runs: every refusal stays a refusal, only this answer changes) |

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
- **A stronger model did reduce them** (7B test): in its run, one dropped caveat (MHP-03) and none of the others.
  It also showed that our checks were tuned to the 3B's habits: its precise "X is not provided in the sources"
  tripped the refusal detector on a correct answer (36). Changing the model means re-checking the code around it.

---

## Why models behave this way

The explanations below are the generally accepted mechanisms behind each type of failure, matched to what we saw.
We can't look inside the model to prove which mechanism caused a given answer; treat them as the most likely
reasons, supported by the patterns in the table (which failures repeat, what fixed them, what didn't).

### The one idea behind almost everything: a language model predicts plausible text

A model like Qwen doesn't look facts up. It writes one token (a word piece) at a time, each time choosing a likely
next token given everything before it: our rules, the passages, the question, and what it has written so far. What
counts as "likely" was learned from huge amounts of text during training. Retrieval-augmented generation works
because the passages make the *correct* continuation very likely: if the passage says "20 to 30 November 2026",
copying it is the most probable thing to write. **Failures happen whenever something else becomes more probable than
copying the passage**: a pattern learned in training, a habit of helpful assistants, or a mistake earlier in the
same answer that the model then continues from. A model has no built-in sense of "I'm not sure"; it produces fluent
text either way, which is why a wrong answer reads exactly as confidently as a right one.

Small models (1.5B-3B parameters) follow this pattern more often, because they have less capacity to keep the
instructions, several passages and the question all in view at once.

### Invented fact (failures 10, 11, 13-15, 22-26, 31)

**What's happening:** the model fills a gap with what *usually* comes next in similar text.

- **Strong patterns from training beat the passages.** University websites usually have addresses like
  `finance@<domain>`; when the model writes "contact the Finance office at", an email in that shape is the most
  likely continuation, even though no such address is in the passages (failures 13, 15). Likewise "ERP" is usually
  followed by an expansion in explanatory text, so it supplies one, wrongly ("Electronic Records Processing",
  failure 24), and a transcript request "usually" takes a few business days (failure 22).
- **Trained to be helpful.** Chat models are tuned on examples where a complete, confident, helpful answer is
  rewarded. "I don't know" is rarer in that training data than an answer, so a gap gets filled. A redirection
  ("contact the Finance office") feels incomplete without a contact detail, so one gets added.
- **Translation turns copying into composing.** When answering in French, the model can't copy the English passage;
  it has to rewrite it, and rewriting is where it composes freely: it "translates" the university's name into a
  plausible French institution name (failures 14, 25) or "stamped" into "stamped by the post office" (26).
- **Headings look like answers.** A section titled "Which payment methods does the canteen accept (cash, mobile
  money, other)?" with an empty body still contains the words "cash, mobile money". The model can't tell that the
  heading is a question awaiting an answer, so it turns the words into a statement (failure 23).
- **Decoding settings can corrupt copying.** A repeat penalty lowers the probability of tokens already used. The
  model had rephrased the source's "20 to 30 November 2026" as "from November 20th to ...": to finish the range it
  needed "November" again, but a strong penalty (1.15) made that token less likely than a nearby month, so it wrote
  "December 3rd" (failure 10). At Qwen's default (1.05) it copied the range correctly every time.

**Why rules alone didn't stop it:** an instruction like "never write an email that isn't in the sources" is just
more text in the prompt; it shifts probabilities but doesn't forbid anything. When the learned pattern is strong
enough, it wins (failure 15 survived the rule). That's why the reliable fixes were in code: the redactor removes the
email whatever the model does.

### Distorted fact (failures 16, 27-29)

**What's happening:** the right pieces, wrongly assembled.

- **Several similar facts compete.** A passage holding three registration deadlines (6 November, 19 November,
  23 November, with only the last one valid) gives the model three plausible dates; small models don't reliably
  track "the most recent notice wins", so they may pick a superseded one (failure 28).
- **Two cases in one section get blended.** "Normal resit: out of 70, added to CA" and "special resit: out of 100"
  sit side by side; when summarising, the model keeps "resit" and "out of 100" and loses which case each belongs to
  (failure 29). Two offices in one sentence (the Deans evaluate credits, the Admissions Office admits) get swapped the
  same way (failure 27).
- **Reasoning beyond the text.** Asked "will I pass?", the model tries to be useful by deriving a rule from the
  numbers it has ("capped at 79" becomes "you pass if the total doesn't exceed 79", failure 16). Small models are
  weak at this kind of reasoning and don't flag that they are reasoning rather than quoting.

### Over-generalised (failures 18, 19, 30)

**What's happening:** the condition is dropped, the fact is kept. Conditions ("only for Top-Up students", "if you no
longer have access to your email", "the level it applies to is not specified") are usually short qualifiers attached
to a longer statement. When the model compresses a passage into a short answer, qualifiers are the first thing to
go, because the main statement alone already reads as a complete, plausible sentence. The result answers a slightly
different question than the one the source answered.

### Incomplete (failure 17, and the FIN-05 amounts)

**What's happening:** the model stops early or follows one passage. Lists spread across passages, or a long list
followed by more text, compete with the model's learned sense of how long an answer "should" be. Once it has written
a list that looks complete (six Master's programmes), ending the list is a likely continuation, even if three more
items were in the passage. When two passages overlap (the website page and the curated document), the model tends to
follow one of them.

### False refusal (failures 30, 32)

**What's happening:** the answer exists but doesn't look like an answer. "The complete tuition is XAF 365,000. The
programme and level it applies to are not specified" doesn't match the question "How much are Bachelor fees?" word
for word, and the caveat sounds like "not specified", so the model concludes the information is missing. Our own
rules make this more likely: "if the sources don't contain the specific information, say so" is a strong instruction,
and with an uncertain match the safe-looking refusal wins. (Failure 32 is different: the passage wasn't in the
prompt at all, because top-k 3 cut it.)

### Format/noise: loops, copied markup, odd citations (failures 7, 8, 12)

- **Loops** (failure 7): with near-greedy decoding, the model picks the most likely token each time. Once it has
  written a line twice, writing it a third time becomes *more* likely (repetition reinforces itself), and nothing
  in the text says "stop". Small models fall into this more easily, especially in a long list. A length cap and a
  repetition guard break the cycle from outside.
- **Copied markup** (failure 8): crawled pages contain navigation buttons as Markdown links. To the model they're
  just text in the passage, and copying passage text is exactly what we asked for.
- **Citation formats** (failure 12): "[finance-installments]" is an unusual pattern, rarely seen in training, so the
  model sometimes writes its own variant. Matching ids anywhere in the text made our code robust to that.

### Similarity can't judge relevance (failures 4-6)

The embedding model turns each text into a vector that captures its *topic*, not the facts it states. "What is my
fee balance?" and the fee-statement document are about the same topic, so they score as very similar (0.848) even
though the document can't answer the question. In French, the English-only content shares no words with the question,
so the keyword half of the search contributes nothing and only the vector half works, with less precision. A
similarity threshold can filter off-topic questions, but deciding whether a passage *answers* a question needs
something that reads it (a model or a person).

### Sampling variance (failure 33)

At temperature 0.1 the model still samples: among near-equally likely tokens, it picks randomly. Two runs diverge at
the first such choice, and everything after that differs because each token depends on the ones before. That's why
the same question could be right in one run and wrong in the next. A fixed seed makes the random choices repeatable,
but tiny numerical differences (multi-threaded arithmetic, reuse of cached prompt work) can still flip a near-tie late
in an answer.

### What this means in practice

| Failure type | Reduced by | Reliably stopped by |
|---|---|---|
| Invented contact details, links | prompt rules | **code** (redaction against the passages) |
| Invented or out-of-source numbers and dates | correct decoding settings | **code** (flagging), except small common numbers |
| Invented names, expansions (French) | precise per-question rules ("call it ICT University") | nothing yet: needs checking |
| Answers from empty sections | - | **code** (drop placeholder-only passages) |
| Distorted facts, dropped conditions, incomplete lists | stronger model, clearer content (one case per section, valid date only) | a human check |
| False refusals | content that states facts and caveats separately | a human check |
| Loops | decoding settings | **code** (length cap, repetition guard) |
| On-topic unanswerable questions | similarity threshold (partly) | an answer-verification step, or the model's refusal |
