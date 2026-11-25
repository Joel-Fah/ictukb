# Missing information: canteen hours and payment methods (drafts with [[TO FILL]])

### What information is missing?

These golden questions are listed as "Not yet covered" in `docs/evaluation-latest.md`. Their documents exist but are
`status: draft` with `owner: unassigned`, and the sections that answer them are still `[[TO FILL]]`:

| Golden question | Question | Document |
|---|---|---|
| CAN-02 (P1) | What time does the canteen open and close? | `canteen-hours` |
| CAN-04 (P2) | Does the canteen accept mobile money? | `canteen-payment` |
| VAR-05 (P2) | wat time canteen open | `canteen-hours` |

| Document | Unfilled sections | What to collect (from `docs/upload-checklist.csv`) |
|---|---|---|
| [`canteen-hours`](https://github.com/Egbemichel/ictukb/blob/main/content/canteen/canteen-hours.md) | "At what times does the canteen open and close on each day?"<br>"Is it closed on weekends or holidays?"<br>"Whom should a student contact about the canteen?" | Photograph of the canteen sign with the hours (Canteen manager, `incoming/canteen/canteen_hours_YYYY-MM-DD.jpg`) |
| [`canteen-payment`](https://github.com/Egbemichel/ictukb/blob/main/content/canteen/canteen-payment.md) | "Which payment methods does the canteen accept (cash, mobile money, other)?" | (no item in the upload checklist yet) |

### Office or person who holds the information

Canteen manager

### Category

canteen

### Note on the empty sections' headings

The heading "Which payment methods does the canteen accept (cash, mobile money, other)?" contains example answers.
While the body is `[[TO FILL]]`, a model reads the heading as content: in our local tests, `qwen2.5:1.5b` answered
"The canteen accepts cash and mobile money", which no source states. Until the section is filled, a heading without
example options (e.g. "Which payment methods does the canteen accept?") would avoid that.

---
*How this list was made:* `eval/golden_questions.yml` + the "Not yet covered" list in `docs/evaluation-latest.md` + `docs/upload-checklist.csv` + the documents' own sections, combined by [coverage_gaps.py](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/scripts/coverage_gaps.py). No facts about the university are added here; the fill must come from the offices or official documents.