# Retrieval evaluation

| Metric | Value |
|---|---|
| Questions | 103 |
| Answerable questions with indexed documents (coverage) | 84 of 98 (85.7%) |
| hit@5 on covered questions | 94.0% (target 85%) |
| hit@5 on covered P0 questions | 94.7% (target 95%), 19 of 19 P0 covered |
| Mean reciprocal rank | 85.8% |
| Retrieved correctly and answered with high confidence | 100.0% |
| No-answer correctness | 0.0% |
| Lowest top similarity among answered questions | 0.8124209315695565 |
| Highest top similarity among no-answer questions | 0.8475865234265809 |

## Failures

| Question | Priority | Confidence | Returned documents |
|---|---|---|---|
| PRG-07 | P1 | high | programs-bachelor, admissions-bachelor-requirements, web-bachelors-degree-entry-requirements, web-bachelors-of-science-bsc-in-business-management-and-sustainability-bms, web-bachelors-of-science-bsc-in-banking-and-finance-bnf |
| TTB-02 | P0 | high | people-course-lecturers-files, people-course-lecturers-files, announcements-current-files, procedures-course-registration, programs-course-descriptions |
| PPL-05 | P2 | high | about-contacts, canteen-hours, people-office-responsibilities, people-office-responsibilities, about-academic-regulations |
| MHP-01 | P1 | high | procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript, finance-late-payment |
| MHP-02 | P1 | high | procedures-resits, procedures-resits, procedures-resits, procedures-complaints, procedures-complaints |
| NEG-01 | P1 | high | about-contacts, people-org-chart, procedures-complaints, procedures-complaints, campus-location |
| NEG-02 | P1 | high | erp-fee-statement, erp-fee-statement, finance-fee-notices, finance-fee-schedule, finance-payment-channels |
| NEG-03 | P2 | high | people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, programs-curriculum-files |
| NEG-04 | P2 | high | procedures-resits, procedures-resits, procedures-resits, procedures-resits, about-academic-regulations |
| NEG-05 | P2 | high | about-contacts, about-contacts, web-home-2, campus-location, campus-location |

## Not yet covered (expected documents missing from the index)

CMP-03, CMP-04, CMP-05, CMP-06, CMP-09, TRN-02, CAN-01, CAN-03, PPL-01, PPL-02, STL-01, STL-05, MHP-04, VAR-03
