# Generation evaluation: seedcheck-a

Run 2026-11-25 20:55.

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
| Answerable: expected document retrieved (top-k) | 2/2 (100%) |
| Answerable: expected document cited | 2/2 (100%) |
| Answerable: refused (false refusal if the document was retrieved) | 0/2 (0%) |
| No-answer: refused (correct) | - |
| Answers with unverified figures/dates | 0/2 (0%) |
| Answers with removed contact details | 0/2 (0%) |
| Answers stopped (loop or length cap) | 0/2 (0%) |
| Model called | 2/2 (100%) |
| Median first token (s), model answers | 10.7 |
| Median total time (s), model answers | 32.1 |
| Median answer speed (tokens/s) | 4.3 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 10.9 | 40.6 |  |
| VAR-02 | fr | True | True | False |  | 10.4 | 23.7 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
[retrieval 130 ms, confidence=high, best=0.907, threshold=0.81, language=en]
  0.907  admissions-how-to-apply  [How do I apply to ICT University?]
  0.862  web-home-2  [The ICT University]
  0.855  about-university-overview  [What is ICT University?]
  0.862  web-maters-degree-entry-requirements  [NEW STUDENTS !]
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: [admissions-how-to-apply].
2. Provide the required documents for your level (see Bachelor and Masters requirements documents for details).
3. For transfer and Top-Up students, contact the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
4. Follow up with "Check my application" on the ERP login page using the reference number you received.
5. Finance will verify the application fee to send the admission letter.

[admissions-how-to-apply] [web-maters-degree-entry-requirements]

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
[first token 10.9 s, total 40.6 s, prompt 1018 tok at 96 tok/s, answer 129 tok at 4.3 tok/s]
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
[retrieval 294 ms, confidence=high, best=0.820, threshold=0.81, language=fr]
  0.820  finance-fee-schedule  [How much is the tuition?]
  0.819  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.815  finance-scholarships  [Which scholarships or discounts exist and who qualifies?] DRAFT
  0.811  campus-directions  [What are the usual fares or travel times?] DRAFT
Les frais de scolarité à l'Université Internationale des Technologies et des Communications (ICT) sont de XAF 365,000 [finance-fee-schedule]. Les programmes et niveaux spécifiques ne sont pas documentés pour le moment.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 10.4 s, total 23.7 s, prompt 520 tok at 53 tok/s, answer 58 tok at 4.4 tok/s]
```

