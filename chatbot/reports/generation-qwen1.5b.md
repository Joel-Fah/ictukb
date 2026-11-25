# Generation evaluation: qwen1.5b

Run 2026-11-25 20:27.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:1.5b |
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
| Answerable: expected document cited | 1/15 (7%) |
| Answerable: refused (false refusal if the document was retrieved) | 1/15 (7%) |
| No-answer: refused (correct) | 3/5 (60%) |
| Answers with unverified figures/dates | 0/16 (0%) |
| Answers with removed contact details | 0/16 (0%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 17.1 |
| Median total time (s), model answers | 33.0 |
| Median answer speed (tokens/s) | 6.5 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | False | False |  | 35.2 | 92.9 |  |
| PRC-02 | en | True | True | False |  | 32.9 | 42.1 |  |
| PRC-09 | en | True | False | False |  | 14.8 | 24.7 |  |
| FIN-01 | en | True | False | False |  | 19.6 | 27.6 |  |
| FIN-05 | en | True | False | False |  | 28.3 | 43.4 |  |
| FIN-06 | en | True | False | False |  | 11.4 | 13.7 |  |
| ERP-02 | en | True | False | False |  | 12.2 | 22.4 |  |
| ERP-03 | en | True | False | False |  | 15.4 | 33.4 |  |
| TTB-03 | en | True | False | False |  | 13.4 | 24.0 |  |
| MHP-01 | en | True | False | False |  | 8.2 | 28.1 |  |
| MHP-02 | en | True | False | False |  | 21.4 | 35.5 |  |
| MHP-03 | en | True | False | False |  | 26.1 | 59.8 |  |
| VAR-01 | fr | True | False | False |  | 15.1 | 40.4 |  |
| VAR-02 | fr | True | False | False |  | 14.1 | 32.6 |  |
| VAR-03 | fr | False | False | True |  |  | 0.3 |  |
| NEG-01 | en |  |  | True |  |  | 0.4 |  |
| NEG-02 | en |  |  | False |  | 21.6 | 32.4 |  |
| NEG-03 | en |  |  | True |  |  | 0.9 |  |
| NEG-04 | en |  |  | False |  | 18.8 | 39.0 |  |
| NEG-05 | en |  |  | True |  |  | 0.4 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: https://studentportal.ictuniversity.edu.cm/portal-sign-up/ (the "Apply now" buttons of the website lead there; the ERP login page also offers "Apply for admission", a bilingual public form).
2. Provide the documents required for your level (see the Bachelor and Masters requirements documents). Masters applicants also upload the receipt of the application fee.
3. For transfer and Top-Up students, the documents go to the Department of Transcript and Verification (transcript.verification@ictuniversity.edu.cm), which checks their authenticity; the Deans of the faculties evaluate which credits can be transferred; the Admissions Office (admissions@ictuniversity.edu.cm) then admits the student into the program.
4. Follow your application with "Check my application" on the ERP login page, using the reference number you received.
5. The admission letter is sent once Finance has verified the application fee.

To apply for a Masters degree program at the ICT University, both in Information Communication and Technology (ICT) and in Business Management and Sustainability (BMS), please ensure you provide the following documents:

1. Complete our online application at the ICT University portal-sign-up
2. Certified Scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
3. Scanned copy of identification documents (birth certificate, National ID card, Passport)
4. Three letters or recommendations
5. Statement of Purpose
6. Certified Scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (Non-refundable Application Fee).

Sources given to the model (it did not cite them; check the answer against them):
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
  [web-home-2] Home (https://ictuniversity.org/, verified 2026-11-25)
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
The course registration deadline is on Monday 23 November 2026 [finance-fee-schedule]. From that date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline. [procedures-course-registration]

Sources:
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript, finance-refunds

```
A transcript takes approximately 2-3 business days to process and can be requested through the ERP system. The fee for obtaining an official transcript is not specified in the ERP manual but is added to your My Fees account upon submission.

The cost and processing time for a refund are not documented yet, so it cannot be determined from the sources provided.

Sources given to the model (it did not cite them; check the answer against them):
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
  [finance-refunds] Refund policy (content/finance/finance-refunds.md, verified 2026-11-17)
Note: [finance-refunds] is a draft that has not been verified yet; check with the office.
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files, admissions-fee

```
The complete tuition for the Bachelor program is XAF 365,000 (Central African francs). The specific fee schedule for other programs such as Masters and PhD is not specified in the information collected so far.

Sources given to the model (it did not cite them; check the answer against them):
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [admissions-fee] Application fee (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files, about-academic-calendar

```
The first installment is 50% of the tuition fee, which is XAF 182,500. The second installment is 30% of the tuition fee, which is XAF 109,500. The third installment is 20% of the tuition fee, which is XAF 73,000.

The payment period for the second installment is 20 to 30 November 2026.

Sources given to the model (it did not cite them; check the answer against them):
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [about-academic-calendar] Academic calendar for the current year (content/about/about-academic-calendar.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement, finance-payment-channels

```
The canteen accepts cash and mobile money payment methods [canteen-payment].

Sources:
  [canteen-payment] Canteen payment methods (content/canteen/canteen-payment.md, verified 2026-11-17)
Note: [canteen-payment] is a draft that has not been verified yet; check with the office.
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration, erp-first-login

```
1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

Sources given to the model (it did not cite them; check the answer against them):
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login, erp-first-login

```
To reset your forgotten ERP password:

1. Go to the login page and click "Forgot password?".
2. Enter your email or matricule and click "Send me a link".
3. Check your inbox for an email with a secure link. Click on it to reset your password.

To change your password when logged in:

1. Click your name at the top right, choose "Change Password", enter your current password, new password twice, and click "Update Password".

If you need help contacting ERP support or the Registrar's office, please contact them directly.

Sources given to the model (it did not cite them; check the answer against them):
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations, about-academic-regulations

```
The first semester 2026/2027 examinations are scheduled from Monday 25 January to Wednesday 3 February 2027. Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 from 4 to 10 January 2027.

Sources given to the model (it did not cite them; check the answer against them):
  [about-academic-regulations] Academic regulations (grading, attendance, exams, conduct) (content/about/about-academic-regulations.md, verified 2026-11-17)
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript

```
You need to pay off your outstanding fees before you can request a transcript. Once you have paid, follow these steps:

1. Go to the ERP (Electronic Records Processing) system.
2. Select "Requests and Services" from the left menu.
3. Choose either "Partial Official Transcript" or "Full Official Transcript."
4. Specify the purpose of the transcript.
5. Submit the request.
6. The fee, if any, will be added to your My Fees account.
7. The Registrar's Office processes the request, and you can track its status on the page.

You can also download/ print the official layout of the transcript from the Transcript page in the ERP.

Sources given to the model (it did not cite them; check the answer against them):
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-complaints

```
To resit a course that you have failed, follow these steps:

1. Open Resit Registration in the ERP.
2. List your resit courses with the resit fee and payment status.
3. Pay the resit fee using the payment channels document.
4. Once the fee is paid, your lecturer will enter the resit score.

The amount of the resit fee is shown in the ERP for each course; it is not stated in the manual.

Sources given to the model (it did not cite them; check the answer against them):
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
  [procedures-complaints] Complaints (grades and services) (content/procedures/procedures-complaints.md, verified 2026-11-17)
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements, finance-fee-schedule

```
To apply for a Master's degree program at ICT University, you need to provide the following documents:

1. Complete our online application on the student portal (https://studentportal.ictuniversity.edu.cm/portal-sign-up/).
2. A certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
3. A scanned copy of identification documents (birth certificate, national ID card, or passport).
4. Three letters of recommendation.
5. A statement of purpose.
6. A certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (non-refundable application fee).

The complete tuition is XAF 365,000 (Central African francs). The specific program and level it applies to are not specified in the information collected so far; fees may differ between Bachelor, Masters, and PhD programs.

Sources given to the model (it did not cite them; check the answer against them):
  [admissions-masters-requirements] Masters admission requirements and documents (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview, erp-course-registration

```
Pour s'inscrire aux cours à l'ICT University, suivez ces étapes :

1. Connectez-vous à l'ERP (Course Registration).
2. Tirez une liste des cours de votre programme et cliquez sur "Register Selected".
3. Votre coordonnateur de programme approuvera la registration.
4. Imprimez le formulaire officiel de la formation.
5. Commencez à présenter le formulaire officiel de la formation à vos enseignants avant d'assister aux cours.

Il est nécessaire de payer au moins 50% du tarif semestriel pour pouvoir vous inscrire. Pour vérifier votre paiement, assurez-vous que vous avez payé et que vous avez uploadé le récépissé bancaire dans vos frais personnels.

Sources fournies au modèle (il ne les a pas citées ; vérifiez la réponse avec elles) :
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
  [finance-scholarships] Scholarships and discounts (content/finance/finance-scholarships.md, verified 2026-11-17)
  [transport-overview] University bus service (content/transport/transport-overview.md, verified 2026-11-17)
  [erp-course-registration] Registering courses on the ERP (content/erp/erp-course-registration.md, verified 2026-11-17)
Remarque : [finance-scholarships] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
Remarque : [transport-overview] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
Les frais de scolarité à l'ICT University (Yaoundé, Cameroun) sont évalués à XAF 365,000 (Central African francs). Cependant, les programmes et niveaux spécifiques pour lesquels ces frais s'appliquent ne sont pas précisés dans les informations recueillies jusqu'à présent. Les frais peuvent varier entre programmes de Bachelor, Master et Doctorat.

Sources fournies au modèle (il ne les a pas citées ; vérifiez la réponse avec elles) :
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
  [finance-scholarships] Scholarships and discounts (content/finance/finance-scholarships.md, verified 2026-11-17)
  [campus-directions] How to reach the university (content/campus/campus-directions.md, verified 2026-11-17)
Remarque : [finance-scholarships] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
Remarque : [campus-directions] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
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
To view your current fee balance, open My Fees on the ERP. It will show your complete fee statement including tuition, resit fees, senior project fees, and other fees such as application, student union, infirmary, graduation, bus, additional course, late registration, transcript, fines, and wallet balance.

Sources given to the model (it did not cite them; check the answer against them):
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
  [finance-fee-notices] Current fee and deadline notices (content/finance/finance-fee-notices.md, verified 2026-11-17)
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
Note: [finance-fee-notices] is a draft that has not been verified yet; check with the office.
Note: [finance-fee-notices] was last verified on 2026-11-17 and may be out of date.
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
To pass your resit, you need to achieve a score that is capped at 79 (grade B+, 3.5 points). The resit fee must be paid before the resit can be entered into your record. Ensure you have the correct resit course and fee amount listed in the ERP for payment. Once the resit fee is paid, your lecturer will enter the resit score, which will then be added to your current course mark. If you meet these criteria, you should pass your resit.

Sources given to the model (it did not cite them; check the answer against them):
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2, campus-location

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

