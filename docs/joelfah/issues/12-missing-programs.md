# Missing information: PhD, graduation, thesis, final-year defense, scholarships, refunds, ERP updates, finance contacts (drafts with [[TO FILL]])

### What information is missing?

These golden questions are listed as "Not yet covered" in `docs/evaluation-latest.md`. Their documents exist but are
`status: draft` with `owner: unassigned`, and the sections that answer them are still `[[TO FILL]]`:

| Golden question | Question | Document |
|---|---|---|
| ADM-04 (P1) | How do I apply for the PhD program? | `admissions-phd-requirements` |
| ADM-08 (P1) | Are scholarships or discounts available? | `finance-scholarships` |
| PRG-03 (P1) | Which PhD research areas are available? | `programs-phd` |
| PRG-07 (P1) | What do I need to graduate with a Bachelors degree? | `programs-graduation-requirements` |
| PRG-08 (P1) | How is a Masters thesis structured and defended? | `programs-masters-thesis` |
| PRC-11 (P1) | What are the final year project deadlines and defense format? | `procedures-fyp-defense` |
| FIN-09 (P1) | Is there a refund policy? | `finance-refunds` |
| ERP-08 (P2) | What changed in the latest ERP update? | `erp-release-notes` |
| PPL-03 (P1) | Who handles finance questions? | `people-office-responsibilities` |

| Document | Unfilled sections | What to collect (from `docs/upload-checklist.csv`) |
|---|---|---|
| [`admissions-phd-requirements`](https://github.com/Egbemichel/ictukb/blob/main/content/admissions/admissions-phd-requirements.md) | "Which qualifications are required to apply for the PhD program?"<br>"What must the research proposal contain and how long should it be?"<br>"How is a supervisor assigned and how does the admission decision work?" | PhD application form and research proposal template (Admissions office or Dean of research, `incoming/admissions/admissions_phd-requirements_YYYY-MM-DD.pdf`) |
| [`finance-scholarships`](https://github.com/Egbemichel/ictukb/blob/main/content/finance/finance-scholarships.md) | "Which scholarships or discounts exist and who qualifies?"<br>"How does a student apply and what is the deadline?" | Scholarship and discount policy (Administration or Finance office, `incoming/finance/finance_scholarships_YYYY-MM-DD.pdf`) |
| [`programs-phd`](https://github.com/Egbemichel/ictukb/blob/main/content/programs/phd/programs-phd.md) | "Which research areas are available for PhD candidates?"<br>"What is the normal duration and the maximum duration of the PhD?"<br>"What coursework, if any, is required?" | PhD handbook (Dean of research, `incoming/programs/programs_phd_YYYY-MM-DD.pdf`) |
| [`programs-graduation-requirements`](https://github.com/Egbemichel/ictukb/blob/main/content/programs/programs-graduation-requirements.md) | "How many credits and what minimum GPA are required to graduate at each level?"<br>"Which additional requirements apply (final year project, internship, thesis, defense)?"<br>"How are honours or classes of degree determined?" | Graduation requirements per program, if documented separately (Registrar, `incoming/programs/programs_graduation-requirements_YYYY-MM-DD.pdf`) |
| [`programs-masters-thesis`](https://github.com/Egbemichel/ictukb/blob/main/content/programs/masters/programs-masters-thesis.md) | "How is the thesis topic chosen and approved, and who assigns the supervisor?"<br>"What is the required structure and length of the thesis?"<br>"What is the defense format and what are the deadlines?" | Thesis guidelines and thesis template (Dean of postgraduate studies, `incoming/programs/programs_masters-thesis_YYYY-MM-DD.pdf`) |
| [`procedures-fyp-defense`](https://github.com/Egbemichel/ictukb/blob/main/content/procedures/procedures-fyp-defense.md) | "What are the deadlines for the report and the defense?"<br>"What is the required report structure and length?"<br>"How is the defense organised and how is it graded?" | Final year project report template (Heads of department, `incoming/procedures/procedures_fyp-defense_YYYY-MM-DD.pdf`)<br>Defense evaluation grid (Heads of department, `incoming/procedures/procedures_fyp-defense_YYYY-MM-DD.pdf`) |
| [`finance-refunds`](https://github.com/Egbemichel/ictukb/blob/main/content/finance/finance-refunds.md) | "Is there a refund policy and under which conditions are refunds granted?"<br>"How is a refund requested and how long does it take?" | Refund policy, if written (Finance office, `incoming/finance/finance_refunds_YYYY-MM-DD.pdf`) |
| [`erp-release-notes`](https://github.com/Egbemichel/ictukb/blob/main/content/erp/erp-release-notes.md) | "What changed in the most recent ERP update?" | Release notes or changelog (ERP team, `incoming/erp/erp_release-notes_YYYY-MM-DD.pdf`) |
| [`people-office-responsibilities`](https://github.com/Egbemichel/ictukb/blob/main/content/people/people-office-responsibilities.md) | "Which office handles admissions, registration, finance, transcripts, ERP, student affairs and complaints?"<br>"What is the first point of contact for each type of question?" | (no item in the upload checklist yet) |

### Office or person who holds the information

Administration or Finance office, Admissions office or Dean of research, Dean of postgraduate studies, Dean of research, ERP team, Finance office, Heads of department, Registrar

### Category

programs (also: admissions, procedures, finance, erp, people)

---
*How this list was made:* `eval/golden_questions.yml` + the "Not yet covered" list in `docs/evaluation-latest.md` + `docs/upload-checklist.csv` + the documents' own sections, combined by [coverage_gaps.py](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/scripts/coverage_gaps.py). No facts about the university are added here; the fill must come from the offices or official documents.