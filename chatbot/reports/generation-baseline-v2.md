# Generation evaluation: baseline-v2

Run 2026-11-25 20:42.

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
| keep_alive | 30m |
| min_similarity (effective) | 0.81 |

## Summary (automatic proxies; verdicts are filled by hand in the CSV)

| Measure | Value |
|---|---|
| Questions | 20 |
| Answerable: expected document retrieved (top-k) | 14/15 (93%) |
| Answerable: expected document cited | 14/15 (93%) |
| Answerable: refused (false refusal if the document was retrieved) | 2/15 (13%) |
| No-answer: refused (correct) | 4/5 (80%) |
| Answers with unverified figures/dates | 0/16 (0%) |
| Answers with removed contact details | 1/16 (6%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 20.5 |
| Median total time (s), model answers | 38.0 |
| Median answer speed (tokens/s) | 5.3 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 118.0 | 162.1 |  |
| PRC-02 | en | True | True | False |  | 29.9 | 42.0 |  |
| PRC-09 | en | True | True | False |  | 10.7 | 17.4 |  |
| FIN-01 | en | True | True | True |  | 17.5 | 22.5 |  |
| FIN-05 | en | True | True | False |  | 26.1 | 38.8 |  |
| FIN-06 | en | True | True | False |  | 11.8 | 27.0 |  |
| ERP-02 | en | True | True | False |  | 16.8 | 34.6 |  |
| ERP-03 | en | True | True | False |  | 22.7 | 38.3 |  |
| TTB-03 | en | True | True | False |  | 14.2 | 37.8 |  |
| MHP-01 | en | True | True | False |  | 19.7 | 31.6 |  |
| MHP-02 | en | True | True | False |  | 27.0 | 75.1 |  |
| MHP-03 | en | True | True | False |  | 36.6 | 77.6 |  |
| VAR-01 | fr | True | True | False |  | 16.6 | 68.0 |  |
| VAR-02 | fr | True | True | False |  | 4.5 | 16.3 |  |
| VAR-03 | fr | False | False | True |  |  | 0.2 |  |
| NEG-01 | en |  |  | True |  |  | 0.2 |  |
| NEG-02 | en |  |  | True |  | 23.3 | 30.6 |  |
| NEG-03 | en |  |  | True |  |  | 0.2 |  |
| NEG-04 | en |  |  | False |  | 21.3 | 69.3 |  |
| NEG-05 | en |  |  | True |  |  | 0.3 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: [admissions-how-to-apply].
2. Provide the required documents for your level (see Bachelor and Masters requirements documents for details).
3. For transfer and Top-Up students, send their documents to the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
4. The Admissions Office at admissions@ictuniversity.edu.cm evaluates which credits can be transferred.
5. Follow up with "Check my application" on the ERP login page using your reference number.

The admission letter is sent once Finance verifies the application fee. [admissions-how-to-apply]

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
The course registration deadline is Monday 23 November 2026 [announcements-current-files]. From this date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline [procedures-course-registration]. Students must present valid, signed and stamped registration forms to their lecturers by 16 November 2026 to attend lectures [announcements-current-files].

Sources:
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript, finance-refunds

```
The processing time for a transcript is not specified in the provided sources [procedures-transcript]. The cost of a transcript is also not stated; you need to check your My Fees page after requesting it through the ERP [procedures-transcript].

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files, admissions-fee

```
[finance-fee-schedule] does not specify the tuition for Bachelor programs. Therefore, I do not have that information and suggest contacting the university directly for accurate details.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files, about-academic-calendar

```
The installment dates and amounts are as follows:

- The first installment is due on 9 November 2026 (50% of the total tuition).
- The second installment is due from 20 to 30 November 2026.
- The third installment amount is XAF 73,000.

[finance-installments] [announcements-current-files]

Sources:
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement, finance-payment-channels

```
The payment methods for tuition at ICT University are accepted through the official bank accounts published by The Secretary General in the notice "Changes to the ICT University official bank account details" issued on 10 October 2024. These accounts are not available in the public code repository but can be found in the knowledge base database [finance-bank-accounts]. Payments made to any other bank accounts are not recognised and cannot be accepted. [finance-payment-channels]

Sources:
  [finance-payment-channels] Payment channels and proof of payment (content/finance/finance-payment-channels.md, verified 2026-11-17)
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration, erp-first-login

```
To log in to the ERP for the first time, follow these steps:

1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

[erp-first-login]

Sources:
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login, erp-first-login

```
If you forgot your ERP password, you can reset it by following these steps:

- [erp-password-reset] Click on the "Forgot password?" option on the login page.
- Type your email or matricule and the system will send you a secure link to choose a new password via email. The link is valid for a short time and can only be used once.

Follow the instructions in the source to reset your password. [erp-password-reset]

Sources:
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations, about-academic-regulations

```
The exams are scheduled from Monday, 25 January to Wednesday, 3 February 2027, according to the official communique of 25 October 2026. [timetables-exams-files]

For context, Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 is from 4 to 10 January 2027. [timetables-exams-files]

Remember that complete institutional and financial clearance is required for students to sit the examinations, which means payment of all school fees for the academic period. [about-academic-regulations]

Sources:
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
  [about-academic-regulations] Academic regulations (grading, attendance, exams, conduct) (content/about/about-academic-regulations.md, verified 2026-11-17)
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript

```
You need to pay your outstanding fees before you can get a transcript. Once your fees are settled, follow these steps:

1. Go to the Transcript page on the ERP.
2. Use Download/Print Transcript to get your official stamped transcript.

[erp-fee-statement] [procedures-transcript]

Sources:
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-complaints

```
To resit a failed course, you need to follow these steps:

1. Check if your course is eligible for resit by paying the resit fee. The eligibility criteria are that the total score of the course must be below 50 [procedures-resits].
2. If your course is eligible for resit, open Resit Registration in the ERP and register for the resit.
3. Pay the resit fee as shown in the ERP for each course. The amount is not stated in the manual but can be found in the ERP [procedures-resits].
4. Once the fee is paid, your lecturer will enter the resit score.

For a special resit (for courses failed in an earlier, already closed semester), you need to request it by clicking Request on Resit Registration and add a note to the Dean. If the Dean agrees, the lecturer scores a fresh mark out of 100 [procedures-resits].

The cost for resit is not stated in the manual but can be found in the ERP. [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements, finance-fee-schedule

```
To apply for the Master's program at ICT University, you need to provide the following documents:

- Complete online application on the student portal (https://studentportal.ictuniversity.edu.cm/portal-sign-up/)
- Certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution
- Scanned copy of identification documents (birth certificate, national ID card or passport)
- Three letters of recommendation
- Statement of purpose
- Certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (non-refundable application fee)

Regarding fees, the complete tuition is XAF 365,000. However, this information is not specific to Master's programs and may differ between Bachelor, Masters, and PhD programs. [finance-fee-schedule]

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview, erp-course-registration

```
Pour vous inscrire aux cours, suivez ces étapes :

1. Vérifiez votre paiement de frais d'études : [erp-course-registration] Vous devez avoir payé au moins 50% des frais de la session pour pouvoir vous inscrire aux cours. Si vous avez déjà payé, téléchargez le reçu bancaire dans votre compte My Fees afin que le service Finances vérifie votre paiement.

2. Utilisez l'ERP (Electronic Registration Process) pour vous inscrire : [procedures-course-registration] Dans l'ERP, sélectionnez les cours de votre programme et cliquez sur "Register Selected". Votre coordinateur de programme approuvera votre inscription. Une fois votre inscription validée, imprimez le formulaire de validation d'inscription.

3. Présentez-vous avec votre document d'inscription : [procedures-course-registration] Depuis le 16 novembre 2026, vous devez présenter un formulaire d'inscription officiel signé et apposé par la poste à vos professeurs avant de participer aux cours. Seuls les étudiants inscrits sur la liste des cours seront autorisés à y assister.

[Voir le document d'inscription dans l'ERP pour plus de détails.]

Sources:
  [erp-course-registration] Registering courses on the ERP (content/erp/erp-course-registration.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
Les frais de scolarité à l'Université de Technologie (ICT University) sont de XAF 365,000 (Central African francs). Les programmes et niveaux spécifiques ne sont pas documentés pour le moment [finance-fee-schedule].

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
```

### VAR-03 (campus, variant, fr)

> Où se trouve le bureau des finances ?

Expected: campus-office-directory; retrieved: about-contacts, web-faculty-of-bms, web-faculty-of-ict, web-faculty-of-bms

```
Je n'ai pas cette information dans la base de connaissances de l'ICT University. Veuillez contacter directement l'université. Contacts officiels (document about-contacts, en anglais) :
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-01 (about, no-answer, en)

> What is the rector's personal phone number?

Expected: (no answer expected); retrieved: about-contacts, people-org-chart, procedures-complaints, procedures-complaints

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-02 (finance, no-answer, en)

> What is my current fee balance?

Expected: (no answer expected); retrieved: erp-fee-statement, erp-fee-statement, finance-fee-notices, finance-fee-schedule

```
I do not have that information. You can contact the Finance office at [contact removed: not in the sources] to find out your current fee balance. [finance-fee-schedule]

Note: the model wrote a contact detail that is not in the knowledge base; it was removed. Use only the official contacts below or in the cited documents.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-03 (programs, no-answer, en)

> What were last year's exam questions for a given course?

Expected: (no answer expected); retrieved: people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-04 (procedures, no-answer, en)

> Will I pass my resit?

Expected: (no answer expected); retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-resits

```
To determine if you will pass your resit, we need to consider the following points from the sources:

- The sources do not provide specific information about whether a resit will result in passing or failing. They only detail the process and conditions for resits.

- [procedures-resits] explains that a resit is eligible if a course has a total below 50, and it requires payment of the resit fee to be considered resit-eligible.

- [procedures-resits] also states how grades are calculated for normal resits: adding the resit score (out of 70) to your CA mark, with a maximum final total of 79 (grade B+, 3.5 points).

- [procedures-resits] provides information on how to register for and pay the resit fee, as well as details about special resits.

Given these sources, we cannot determine if you will pass your resit. We only know that eligibility depends on having a total below 50 in the course, and that passing would depend on achieving a final grade of 79 or higher after adding the resit score to your CA mark.

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2, campus-location

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

