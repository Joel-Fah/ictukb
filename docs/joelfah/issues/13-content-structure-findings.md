# Content patterns that make chatbot answers wrong (evidence from 5 local evaluation runs)

## Context

We ran 20 golden questions through a local RAG chatbot built on this knowledge base (retrieval with `ictkb.search`,
answers by `qwen2.5:3b`; also `qwen2.5:1.5b`), 5 runs, 80 model-written answers, each checked by hand against the source
documents. Most failures traced back to a few **content patterns**, not to retrieval: the right passage was found,
but the way it is written led the model to a wrong or incomplete answer. These patterns probably affect every
chatbot built on the knowledge base, so they seem worth fixing at the source.

Details and transcripts: [evaluation write-up](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/03-evaluation.md),
[per-answer verdicts](https://github.com/Joel-Fah/ictukb/tree/local-chatbot/chatbot/reports).

## Patterns

### 1. A fact and its caveat in one paragraph

`finance-fee-schedule`, "How much is the tuition?":
> The complete tuition is XAF 365,000 (Central African francs). The programme and level it applies to are not
> specified in the information collected so far; fees may differ between Bachelor, Masters and PhD programs.

FIN-01 ("How much are tuition fees for the Bachelors program?") failed in **5 of 5 runs**: 3 times the model refused
("does not specify the tuition for Bachelor programs"), twice it dropped the caveat ("the Bachelor tuition is
XAF 365,000").

*Suggestion:* a question-style section that answers the level question directly, e.g. "Is the tuition the same for
Bachelor, Masters and PhD?" stating what is known and what isn't, so the caveat is an answer of its own.

### 2. Several dates for one thing, only one of them valid

`procedures-course-registration`, "What is the course registration deadline?", gives 23 November 2026 and then the
earlier dates from superseded notices (6 November, 19 November). In one run the model answered with the superseded
19 November. Similarly, "9 November 2026" (the date fees control resumed) sits next to the installment rules in
`announcements-current-files` and `finance-installments`; FIN-05 ("What are the installment dates and amounts?") was
answered with "the first installment is due on 9 November" in **4 of 5 runs**.

*Suggestion:* keep the valid date in the answer section; move superseded dates to the `conflict_note` (or a
separate "Earlier notices" section). Where a due date is unknown, say so explicitly ("The due date of the first
installment has not been published").

### 3. Several cases in one sentence

`admissions-how-to-apply`, step 3: "For transfer and Top-Up students, the documents go to the Department of
Transcript and Verification ..., which checks their authenticity; the Deans of the faculties evaluate which credits
can be transferred; the Admissions Office ... then admits the student." In 2 of 5 runs the model attributed a role to
the wrong office or presented the Top-Up step as applying to everyone.

*Suggestion:* one case per section ("What happens to a transfer or Top-Up application?"), short sentences, one actor
per sentence.

### 4. Draft headings that contain example answers

While a section is `[[TO FILL]]`, a heading with examples in parentheses looks like content. From "Which payment
methods does the canteen accept (cash, mobile money, other)?", `qwen2.5:1.5b` answered "The canteen accepts cash and
mobile money", which no source states. Seven draft headings follow this pattern:

- `canteen-payment`: "Which payment methods does the canteen accept (cash, mobile money, other)?"
- `timetables-publication`: "Where are class timetables published (ERP, notice board, other)?"
- `announcements-channels`: "Where do official announcements appear (ERP, notice boards, WhatsApp, email, social media)?"
- `campus-floor-plans`: "What is on each of the three floors and how are they connected (stairs, lift)?"
- `people-org-chart`: "How is the university organised (rector, deans, registrar, heads of department)?"
- `programs-graduation-requirements`: "Which additional requirements apply (final year project, internship, thesis, defense)?"
- `student-life-sug`: "How can students reach it (office, official channel)?"

*Suggestion:* drop the parenthesised examples from headings (they can move to the collection guide), or exclude
sections whose body is only `[[TO FILL]]` from indexing in staging. (Our chatbot now skips such passages, which fixed
it locally.)

## Proposal

If the maintainers agree, these could become a few lines in CONTRIBUTING.md's "Writing a document" section, and the
four documents above could be restructured by their owners (each change keeps the existing facts and sources;
nothing new is added).
