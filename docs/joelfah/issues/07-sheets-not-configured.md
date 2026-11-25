# 8 golden-question topics depend on Google Sheets that are not configured (sheet_id is empty)

## What happens

Every sheet in `sources/sheets.yml` has `sheet_id: ""`. Per the file's own header, unconfigured sheets are skipped
by `ictkb sync-sheets`, so these documents exist nowhere (not in production, not in a local index). Among the 35
golden questions listed as "Not yet covered" in `docs/evaluation-latest.md`, **14
depend on 8 of these sheets**:

| Document (sheet) | Golden questions waiting for it | Header template already in the repo | Office (from the upload checklist) |
|---|---|---|---|
| `campus-office-directory` | CMP-04, CMP-05, CMP-09, MHP-04, VAR-03 | `templates/sheets/campus-office-directory.csv` | Administration |
| `campus-room-directory` | CMP-03, CMP-06 | `templates/sheets/campus-room-directory.csv` | Administration |
| `canteen-menu` | CAN-01, CAN-03 | `templates/sheets/canteen-menu.csv` | Canteen manager |
| `people-delegates` | PPL-01 | `templates/sheets/people-delegates.csv` | (not in the checklist) |
| `people-heads-of-department` | PPL-02 | `templates/sheets/people-heads-of-department.csv` | (not in the checklist) |
| `student-life-clubs` | STL-01 | `templates/sheets/student-life-clubs.csv` | Student affairs |
| `student-life-events` | STL-05 | `templates/sheets/student-life-events.csv` | Student affairs |
| `transport-schedule` | TRN-02 | `templates/sheets/transport-schedule.csv` | Transport coordinator |

The other 5 sheets (`programs-curriculum`, `timetables-exams`, `announcements-current`, `people-staff-directory`,
`people-course-lecturers`) are also unconfigured; some of their questions are currently answered by the `*-files`
documents from `ictkb intake`.

Seen locally: VAR-03 "Où se trouve le bureau des finances ?" was refused ("not in the knowledge base") in all five
of our evaluation runs, because nothing about office locations is indexed.

## Proposal

1. Create each sheet from its header template in `templates/sheets/`, share it as "Anyone with the link can view",
   and set its `sheet_id` (infrastructure owner, `sources/`).
2. Say who fills each one (the offices above), and whether contributors may send a filled CSV instead (the
   connector already supports `csv_path` for offline work).

Happy to help structure the CSVs once a source office is named.

---
*How this list was made:* `eval/golden_questions.yml` + the "Not yet covered" list in `docs/evaluation-latest.md` + `docs/upload-checklist.csv` + the documents' own sections, combined by [coverage_gaps.py](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/scripts/coverage_gaps.py). No facts about the university are added here; the fill must come from the offices or official documents.