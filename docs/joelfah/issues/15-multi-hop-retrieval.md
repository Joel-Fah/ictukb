# Multi-hop golden questions: one document fills the top 5 (MHP-01), and MHP-02 expects a document without the answer

## What happens

`docs/evaluation-latest.md` lists MHP-01, MHP-02 and MHP-03 as failures (multi-hop questions require every expected
document in the top 5). We reproduced MHP-01 and MHP-02 on a local index with a different embedding model (e5 via
`fastembed`), so they don't look model-specific:

| Question | Expected | Production (bge-m3) top 5 | Local (e5) top 5 |
|---|---|---|---|
| MHP-01 "I owe part of my fees and want a transcript. What do I need to do?" | finance-clearance, procedures-transcript | procedures-transcript ×2, erp-fee-statement, erp-support, finance-late-payment | procedures-transcript ×3, erp-fee-statement, finance-late-payment |
| MHP-02 "I failed a course. How do I resit, and what will it cost?" | procedures-resits, finance-fee-schedule | procedures-resits ×3, procedures-complaints, erp-course-registration | procedures-resits ×3, procedures-complaints ×2 |

(MHP-03 passes locally, where `finance-fee-schedule` is retrieved 4th; it fails in production.)

## Two different causes

### MHP-01: one document takes most of the top 5

Three chunks of `procedures-transcript` occupy three of the five slots, so `finance-clearance` never makes it.
`procedures-transcript` lists `finance-clearance` under `related` in its front matter, but its text never mentions
clearance (it says "The transcript is not available while you have outstanding fees"), and `finance-clearance` never
mentions transcripts, so neither half of the hybrid search links them.

Generation consequence (local, 5 runs): the answers correctly said "pay your outstanding fees first" but never
explained clearance.

*Options:*
1. **Search:** cap the number of chunks per document in the final top-k (e.g. at most 2), so other documents get a
   slot. That's a change in `src/ictkb/search.py`, so the infrastructure owner's call; happy to send a PR with a test
   if wanted.
2. **Content:** where the documents already establish the link, say it in the text (e.g. in `procedures-transcript`,
   name the clearance step and point to `finance-clearance`), so the keyword search can connect them. Only with the
   content owner's confirmation that this is how it works.

### MHP-02: the expected document doesn't contain resit fees

MHP-02 expects `finance-fee-schedule`, but that document doesn't mention resits. The resit fee is covered in
`procedures-resits` ("The amount of the resit fee is shown in the ERP for each course; it is not stated in the
manual"). So the question can never pass as written, even with perfect retrieval.

*Options:* change MHP-02's `expected_docs` to `[procedures-resits]` (with type `factual`), or keep it multi-hop and
add the resit fee to the fee schedule once an official source gives the amount.
