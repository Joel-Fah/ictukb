# Generation evaluation: topk3

Run 2026-11-25 20:53.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:3b |
| top_k | 3 |
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
| Answerable: expected document cited | 13/15 (87%) |
| Answerable: refused (false refusal if the document was retrieved) | 1/15 (7%) |
| No-answer: refused (correct) | 3/5 (60%) |
| Answers with unverified figures/dates | 0/16 (0%) |
| Answers with removed contact details | 0/16 (0%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 4.5 |
| Median total time (s), model answers | 36.1 |
| Median answer speed (tokens/s) | 4.5 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 26.9 | 74.0 |  |
| PRC-02 | en | True | True | False |  | 3.4 | 23.8 |  |
| PRC-09 | en | True | True | False |  | 16.2 | 30.4 |  |
| FIN-01 | en | True | True | False |  | 22.2 | 41.6 |  |
| FIN-05 | en | True | True | False |  | 4.4 | 25.6 |  |
| FIN-06 | en | True | True | False |  | 2.7 | 12.3 |  |
| ERP-02 | en | True | True | False |  | 16.0 | 55.7 |  |
| ERP-03 | en | True | True | False |  | 2.8 | 34.0 |  |
| TTB-03 | en | True | True | False |  | 0.6 | 25.6 |  |
| MHP-01 | en | True | True | False |  | 9.5 | 41.4 |  |
| MHP-02 | en | True | True | False |  | 3.4 | 59.9 |  |
| MHP-03 | en | True | True | False |  | 4.6 | 54.4 |  |
| VAR-01 | fr | True | False | False |  | 5.3 | 42.1 |  |
| VAR-02 | fr | True | True | False |  | 4.0 | 19.5 |  |
| VAR-03 | fr | False | False | True |  |  | 0.2 |  |
| NEG-01 | en |  |  | True |  |  | 0.2 |  |
| NEG-02 | en |  |  | False |  | 17.4 | 38.3 |  |
| NEG-03 | en |  |  | True |  |  | 0.2 |  |
| NEG-04 | en |  |  | False |  | 2.4 | 16.1 |  |
| NEG-05 | en |  |  | True |  |  | 0.2 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview

```
[retrieval 226 ms, confidence=high, best=0.907, threshold=0.81, language=en]
  0.907  admissions-how-to-apply  [How do I apply to ICT University?]
  0.862  web-home-2  [The ICT University]
  0.855  about-university-overview  [What is ICT University?]
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: [admissions-how-to-apply].
2. Provide the required documents for your level (see the Bachelor and Masters requirements documents).
3. For transfer and Top-Up students, send their documents to the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
4. The Deans of the faculties will evaluate which credits can be transferred.
5. The Admissions Office (admissions@ictuniversity.edu.cm) will then admit the student into the program.
6. Follow your application with "Check my application" on the ERP login page, using the reference number you received.
7. The admission letter is sent once Finance has verified the application fee.

[admissions-how-to-apply] [web-home-2]

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
  [web-home-2] Home (https://ictuniversity.org/, verified 2026-11-25)
[first token 26.9 s, total 74.0 s, prompt 798 tok at 30 tok/s, answer 172 tok at 3.7 tok/s]
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files

```
[retrieval 415 ms, confidence=high, best=0.892, threshold=0.81, language=en]
  0.892  procedures-course-registration  [What is the course registration deadline?]
  0.851  procedures-course-registration  [How do I register for courses each semester?]
  0.853  announcements-current-files  [Notice of 13 November 2026: course registration, class lists and the enrolment list] STALE
The course registration deadline is Thursday 19 November 2026 [procedures-course-registration]. 

A penalty of 10,000 FCFA applies to any student who registers after this date [procedures-course-registration]. 

Effective from Monday 23 November 2026, students must present a valid, signed and stamped registration form to their lecturers before attending lectures [announcements-current-files].

Sources:
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
[first token 3.4 s, total 23.8 s, prompt 1047 tok at 441 tok/s, answer 88 tok at 4.3 tok/s]
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript

```
[retrieval 218 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  procedures-transcript  [What do I need before I can get a transcript?]
  0.849  procedures-transcript  [How do I request an official stamped transcript?]
  0.825  procedures-transcript  [How do I get my transcript?]
The processing time for a transcript is not specified in the provided sources. The cost of a transcript is also not stated; you need to check your My Fees page after submitting the request through the Registrar's Office. [procedures-transcript] [procedures-transcript] [procedures-transcript]

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
[first token 16.2 s, total 30.4 s, prompt 670 tok at 42 tok/s, answer 61 tok at 4.3 tok/s]
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files

```
[retrieval 797 ms, confidence=high, best=0.858, threshold=0.81, language=en]
  0.858  finance-fee-schedule  [How much is the tuition?]
  0.817  finance-installments  [Can I pay my fees in installments?]
  0.800  announcements-current-files  [Notice of 9 November 2026: resumption of fees control] STALE
[finance-fee-schedule] The complete tuition is XAF 365,000. However, [finance-installments] states that this amount is paid in three installments: the first installment is 50% of the tuition, which is XAF 182,500. Therefore, for the Bachelors program, the complete tuition remains XAF 365,000.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
[first token 22.2 s, total 41.6 s, prompt 706 tok at 33 tok/s, answer 90 tok at 4.6 tok/s]
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files

```
[retrieval 392 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  finance-installments  [What are the installment dates?]
  0.857  finance-installments  [Can I pay my fees in installments?]
  0.837  announcements-current-files  [Latest notice: end of course registration (23 November 2026) and second installment] STALE
The installment dates and amounts are as follows:

- First installment: 50% of the total tuition, due on or before Monday, November 9, 2026.
- Second installment: 30% of the total tuition, due between 20 to 30 November 2026.
- Third installment: 20% of the total tuition, not specified in the sources.

[finance-installments] [announcements-current-files]

Sources:
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
[first token 4.4 s, total 25.6 s, prompt 850 tok at 246 tok/s, answer 98 tok at 4.6 tok/s]
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement

```
[retrieval 226 ms, confidence=high, best=0.835, threshold=0.81, language=en]
  0.835  canteen-payment  [Which payment methods does the canteen accept (cash, mobile money, other)?] DRAFT
  0.791  finance-payment-channels  [How do I submit proof of payment and get a receipt?]
  0.784  erp-fee-statement  [How do I pay and prove my payment?]
The sources do not provide information about the payment methods accepted at ICT University. [finance-payment-channels] suggests how to submit proof of payment, but do not mention what methods are accepted. Please contact the university for this information.

Sources:
  [finance-payment-channels] Payment channels and proof of payment (content/finance/finance-payment-channels.md, verified 2026-11-17)
[first token 2.7 s, total 12.3 s, prompt 522 tok at 246 tok/s, answer 47 tok at 4.9 tok/s]
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration

```
[retrieval 253 ms, confidence=high, best=0.914, threshold=0.81, language=en]
  0.914  erp-first-login  [How do I log in to the ERP for the first time?]
  0.875  erp-first-login  [What is my first password?]
  0.843  erp-course-registration  [How do I register courses on the ERP?]
To log in to the ERP for the first time, follow these steps:

1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

[erp-first-login]

For your first password, you need to contact the ERP support contact or the Registrar's office as the initial password is not published in this knowledge base. Change it the first time you log in by clicking your name at the top right, choosing Change Password, entering the current password and setting a new one with at least 8 characters mixing letters and numbers.

[erp-first-login]

Sources:
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
[first token 16.0 s, total 55.7 s, prompt 667 tok at 43 tok/s, answer 172 tok at 4.3 tok/s]
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login

```
[retrieval 286 ms, confidence=high, best=0.912, threshold=0.81, language=en]
  0.912  erp-password-reset  [How do I reset a forgotten ERP password?]
  0.905  erp-password-reset  [How do I change my password when I am logged in?]
  0.881  erp-first-login  [What is my first password?]
If you forgot your ERP password, you can reset it by following these steps:

- [erp-password-reset] Click on the "Forgot password?" option on the login page.
- Enter your email or matricule and click the link sent to you via email.
- Follow the instructions in the email to choose a new password.

Alternatively, if you are already logged in but need to change your password:

- [erp-password-reset] Click on your name at the top right corner of the page.
- Select "Change Password" from the dropdown menu.
- Enter your current password and set a new one with at least 8 characters including letters and numbers.
- Click "Update Password" to save your changes.

Sources:
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
[first token 2.8 s, total 34.0 s, prompt 707 tok at 304 tok/s, answer 144 tok at 4.6 tok/s]
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations

```
[retrieval 163 ms, confidence=high, best=0.859, threshold=0.81, language=en]
  0.809  about-academic-regulations  [What is required to sit end-of-semester examinations?]
  0.859  timetables-exams-files  [When are the exams?]
  0.802  about-academic-regulations  [What are the rules for online students and the Moodle platform?]
The exams for the first semester 2026/2027 are scheduled from Monday 25 January to Wednesday 3 February 2027, according to the official communique of 25 October 2026. [timetables-exams-files]

For reference, Continuous Assessment 1 was from 14 to 19 December 2026 and Continuous Assessment 2 was from 4 to 10 January 2027. [timetables-exams-files]

Sources:
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
[first token 0.6 s, total 25.6 s, prompt 661 tok at 3016 tok/s, answer 111 tok at 4.4 tok/s]
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement

```
[retrieval 296 ms, confidence=high, best=0.890, threshold=0.81, language=en]
  0.886  procedures-transcript  [What do I need before I can get a transcript?]
  0.890  procedures-transcript  [How do I request an official stamped transcript?]
  0.840  erp-fee-statement  [How do I view my fee statement on the ERP?]
[procedures-transcript] You need to ensure that you have paid all your outstanding fees before you can get an official transcript. Once your fees are settled, you can request a transcript by following these steps:

1. Under Requests and Services, choose a partial or full official transcript.
2. Choose the turnaround time (standard or express, if offered).
3. State the purpose for which you need the transcript.
4. The fee, if any, will be added to your My Fees page. You can view your current fees on [erp-fee-statement].
5. After submitting your request, the Registrar's Office will process it and you can track its status and reference number on their page.

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
[first token 9.5 s, total 41.4 s, prompt 692 tok at 76 tok/s, answer 142 tok at 4.5 tok/s]
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits

```
[retrieval 319 ms, confidence=high, best=0.874, threshold=0.81, language=en]
  0.874  procedures-resits  [How do I register for a resit and what does it cost?]
  0.872  procedures-resits  [What is a special resit?]
  0.865  procedures-resits  [Who is eligible for a resit?]
To resit a course you have failed, follow these steps:

1. Check if your course is eligible for a resit by paying the resit fee. The eligibility is determined once the resit fee is paid.
   [procedures-resits]

2. If your course is eligible, open Resit Registration in the ERP to see your resit courses and their associated resit fees.

3. Pay the resit fee using the payment channels available in the ERP.

4. Once the fee is paid, your lecturer will enter a new score for you out of 100, capped at 79.

5. If your course is not eligible for a resit (total score above 50), you can request a special resit by clicking Request on Resit Registration and adding a note to the Dean. The Dean's approval is needed, and if granted, a fresh mark will be given out of 100.

6. The cost of the resit fee is shown in the ERP for each course; it is not stated in the manual.

[procedures-resits] [procedures-resits] [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
[first token 3.4 s, total 59.9 s, prompt 692 tok at 241 tok/s, answer 236 tok at 4.2 tok/s]
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements

```
[retrieval 414 ms, confidence=high, best=0.868, threshold=0.81, language=en]
  0.868  admissions-masters-requirements  [What are the entry requirements for the Masters program?]
  0.834  web-maters-degree-entry-requirements  [NEW STUDENTS !]
  0.831  web-maters-degree-entry-requirements  []
To apply for a Master's degree at ICT University, you need to provide the following requirements:

- Complete our online application at the ICT University portal-sign-up [web-maters-degree-entry-requirements].
- Certified Scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution. [web-maters-degree-entry-requirements]
- Scanned copy of identification documents (birth certificate, National ID card, Passport) [web-maters-degree-entry-requirements]
- Three letters of recommendation [web-maters-degree-entry-requirements]
- Statement of Purpose [web-maters-degree-entry-requirements]
- Certified Scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (Non-refundable Application Fee) [admissions-masters-requirements]

The fees for applying to the Master's program at ICT University are $50 or 25,000 CFA. [admissions-masters-requirements]

Sources:
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
  [admissions-masters-requirements] Masters admission requirements and documents (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)
[first token 4.6 s, total 54.4 s, prompt 900 tok at 227 tok/s, answer 215 tok at 4.3 tok/s]
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview

```
[retrieval 187 ms, confidence=high, best=0.832, threshold=0.81, language=fr]
  0.832  procedures-course-registration  [How do I register for courses each semester?]
  0.822  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.822  transport-overview  [How does a student subscribe and who is the contact?] DRAFT
Pour vous inscrire aux cours, suivez ces étapes :

1. Accédez à l'ERP de l'ICTU (Course Registration).
2. Cochez les cours de votre programme et cliquez sur Register Selected.
3. Votre coordinateur de programme approuvera votre inscription.
4. Imprimez le formulaire de réinscription officiel.
5. À partir du 16 novembre 2026, vous devrez présenter un formulaire de réinscription valide, signé et étampé à vos enseignants avant d'assister aux cours.
6. Seuls les étudiants dont les noms figurent sur la liste des cours officiels peuvent assister.

[Voir les détails des étapes dans le document de l'ERP de la réinscription.]

Sources fournies au modèle (il ne les a pas citées ; vérifiez la réponse avec elles) :
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
[first token 5.3 s, total 42.1 s, prompt 566 tok at 114 tok/s, answer 169 tok at 4.6 tok/s]
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships

```
[retrieval 188 ms, confidence=high, best=0.820, threshold=0.81, language=fr]
  0.820  finance-fee-schedule  [How much is the tuition?]
  0.819  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.815  finance-scholarships  [Which scholarships or discounts exist and who qualifies?] DRAFT
Les frais de scolarité à l'Université Internationale des Technologies et des Communications (ICT University) sont de XAF 365,000 [finance-fee-schedule]. Les programmes et niveaux ne sont pas spécifiés dans les informations collectées jusqu'à présent, donc les frais peuvent varier entre les programmes Bachelor, Masters et PhD.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 4.0 s, total 19.5 s, prompt 520 tok at 141 tok/s, answer 77 tok at 5.0 tok/s]
```

### VAR-03 (campus, variant, fr)

> Où se trouve le bureau des finances ?

Expected: campus-office-directory; retrieved: about-contacts, web-faculty-of-bms, web-faculty-of-ict

```
[retrieval 226 ms, confidence=low, best=0.779, threshold=0.81, language=fr]
  0.779  about-contacts  [What is the official postal address of the university?]
  0.771  web-faculty-of-bms  [Mission Statement > Various BMS Programs > Banking and Finance]
  0.768  web-faculty-of-ict  []
Je n'ai pas cette information dans la base de connaissances de l'ICT University. Veuillez contacter directement l'université. Contacts officiels (document about-contacts, en anglais) :
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-01 (about, no-answer, en)

> What is the rector's personal phone number?

Expected: (no answer expected); retrieved: about-contacts, people-org-chart, procedures-complaints

```
[retrieval 201 ms, confidence=low, best=0.800, threshold=0.81, language=en]
  0.800  about-contacts  [What are the general phone number and email address?]
  0.773  people-org-chart  [How is the university organised (rector, deans, registrar, heads of department)?] DRAFT
  0.756  procedures-complaints  []
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-02 (finance, no-answer, en)

> What is my current fee balance?

Expected: (no answer expected); retrieved: erp-fee-statement, erp-fee-statement, finance-fee-notices

```
[retrieval 232 ms, confidence=high, best=0.848, threshold=0.81, language=en]
  0.838  erp-fee-statement  [How do I view my fee statement on the ERP?]
  0.833  erp-fee-statement  [How do I pay and prove my payment?]
  0.848  finance-fee-notices  [What fee changes or payment deadlines have been announced recently?] DRAFT STALE
To find out your current fee balance, you need to view your fee statement on the ERP. Here are the steps:

1. Open My Fees.
2. Your complete fee statement will be displayed, including tuition, resit fees, senior project fees, and other various fees.

However, I do not have specific information about your current fee balance as it is not documented yet [erp-fee-statement]. You would need to check your fee statement for the most accurate information.

Sources:
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
[first token 17.4 s, total 38.3 s, prompt 679 tok at 40 tok/s, answer 97 tok at 4.6 tok/s]
```

### NEG-03 (programs, no-answer, en)

> What were last year's exam questions for a given course?

Expected: (no answer expected); retrieved: people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files

```
[retrieval 226 ms, confidence=low, best=0.805, threshold=0.81, language=en]
  0.803  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
  0.805  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
  0.802  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-04 (procedures, no-answer, en)

> Will I pass my resit?

Expected: (no answer expected); retrieved: procedures-resits, procedures-resits, procedures-resits

```
[retrieval 187 ms, confidence=high, best=0.833, threshold=0.81, language=en]
  0.833  procedures-resits  [Who is eligible for a resit?]
  0.828  procedures-resits  [How is a resit graded?]
  0.816  procedures-resits  [How do I register for a resit and what does it cost?]
To determine if you will pass your resit, we need to consider the following points from the sources:

1. The sources do not provide specific information about whether you will pass or fail a resit directly. They only describe the eligibility criteria for resits and how they are graded.

[procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
[first token 2.4 s, total 16.1 s, prompt 672 tok at 322 tok/s, answer 64 tok at 4.7 tok/s]
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2

```
[retrieval 227 ms, confidence=low, best=0.791, threshold=0.81, language=en]
  0.791  about-contacts  [What is the official postal address of the university?]
  0.777  about-contacts  [What are the general phone number and email address?]
  0.784  web-home-2  [The ICT University > Recent Events > 15th ICT For Africa Conference 2024]
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

