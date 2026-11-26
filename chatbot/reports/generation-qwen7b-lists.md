# Generation evaluation: qwen7b-lists

Run 2026-11-26 05:22.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:7b |
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
| Median first token (s), model answers | 42.8 |
| Median total time (s), model answers | 74.0 |
| Median answer speed (tokens/s) | 3.3 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| PRG-02 | en | True | True | False |  | 60.8 | 93.2 |  |
| ADM-02 | en | True | True | False |  | 24.9 | 54.8 |  |

## Answers as displayed

### PRG-02 (programs, list, en)

> Which Masters programs are offered?

Expected: programs-masters, web-masters-programs; retrieved: programs-masters, web-masters-programs, web-masters-programs, web-masters-programs

```
The following Masters programs are offered:

1. Applied Statistics and Demography
2. Development Planning
3. iMBA (iMBA)
4. Artificial Intelligence
5. Applied ICTs in Education
6. Applied ICT in Public Health
7. Information Systems Security
8. Information Technology
9. Information Systems and Networking
10. BMS Master's programs (Applied Statistics and Demography, Development Planning, iMBA)

Sources: [programs-masters], [web-masters-programs]

Sources:
  [programs-masters] Masters programs, general rules (https://ictuniversity.org/masters-programs/, verified 2026-11-18)
  [web-masters-programs] Masters Programs (https://ictuniversity.org/masters-programs/, verified 2026-11-25)
```

### ADM-02 (admissions, list, en)

> What documents do I need for a Bachelors application?

Expected: admissions-bachelor-requirements, web-bachelors-degree-entry-requirements; retrieved: admissions-bachelor-requirements, admissions-masters-requirements, admissions-bachelor-requirements, admissions-fee

```
To complete an application for a Bachelor's degree, you need to provide the following documents:
- A certified copy of the birth certificate
- Certified copies of the GCE "O" Level certificate, GCE "A" Level certificate, Probatoire, and Baccalaureate
- Authenticated copies of the GCE "O" Level certificate, GCE "A" Level certificate, Probatoire, and Baccalaureate [admissions-bachelor-requirements].

Sources:
  [admissions-bachelor-requirements] Bachelor admission requirements and documents (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
```

