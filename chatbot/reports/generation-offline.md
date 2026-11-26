# Generation evaluation: offline

Run 2026-11-26 06:09.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:3b |
| top_k | 4 |
| max_chunk_chars | 1200 |
| max_context_chars | 4000 |
| min_similarity | None |
| relative_cutoff | 0.05 |
| num_ctx | 4096 |
| temperature | 0.1 |
| repeat_penalty | 1.05 |
| max_answer_tokens | 400 |
| seed | 42 |
| keep_alive | 30m |
| min_similarity (effective) | 0.81 |

## Summary (automatic proxies; verdicts are filled by hand in the CSV)

| Measure | Value |
|---|---|
| Questions | 2 |
| Answerable: expected document retrieved (top-k) | 1/1 (100%) |
| Answerable: expected document cited | 1/1 (100%) |
| Answerable: refused (false refusal if the document was retrieved) | 0/1 (0%) |
| No-answer: refused (correct) | 1/1 (100%) |
| Answers with unverified figures/dates | 0/1 (0%) |
| Answers with removed contact details | 0/1 (0%) |
| Answers stopped (loop or length cap) | 0/1 (0%) |
| Model called | 1/2 (50%) |
| Median first token (s), model answers | 31.6 |
| Median total time (s), model answers | 44.4 |
| Median answer speed (tokens/s) | 7.3 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| PRC-02 | en | True | True | False |  | 31.6 | 44.4 |  |
| NEG-01 | en |  |  | True |  |  | 0.1 |  |

## Answers as displayed

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
The course registration deadline is Monday 23 November 2026 [announcements-current-files]. From this date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline [procedures-course-registration]. Students must present valid, signed and stamped registration forms to their lecturers by 16 November 2026 to be included in the official class list [announcements-current-files].

Sources:
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### NEG-01 (about, no-answer, en)

> What is the rector's personal phone number?

Expected: (no answer expected); retrieved: about-contacts, people-org-chart, procedures-complaints, procedures-complaints

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

