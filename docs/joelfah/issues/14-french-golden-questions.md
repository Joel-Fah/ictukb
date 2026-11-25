# Proposal: 26 French golden questions (French retrieval is measurably weaker)

## Why

The golden set has 3 French questions out of 103 (VAR-01 to VAR-03), while many students ask in French. The content
is English-only, so French questions lose the keyword half of the hybrid search and rely on the multilingual
embeddings alone.

We measured it on a local staging index (e5 embeddings via `fastembed`, 110 documents, commit 2c9f3eb): 26 French
questions, each a translation of an answerable English golden question with the same `expected_docs`.

| | English | French |
|---|---|---|
| Expected document in the top 5 | **26/26** | **20/26** |
| Best similarity below 0.81 (our local e5 threshold, see #9) | 0 | 4 |

Missed in French but found in English: FR-01 "Comment postuler à ICT University ?" (ADM-01), FR-04 (ADM-06,
application fee), FR-11 (PRC-06, resit eligibility and cost), FR-14 (PRC-16, GPA), FR-18 (FIN-06, payment methods),
FR-24 (ERP-05, results). The per-question ranks are in
[french-vs-english-retrieval.md](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/reports/french-vs-english-retrieval.md).
Our numbers use e5, not the production bge-m3, so the production gap may differ; the golden questions would measure it.

## Proposal

Add these 26 questions to `eval/golden_questions.yml` (under `eval/`, so this needs the infrastructure owner's
approval; hence an issue first). They are questions only, with the English question's `expected_docs`, category and
priority; ids `FR-01` to `FR-26`, `type: variant`, `language: fr`. File ready to paste:
[golden-questions-fr.yml](https://github.com/Joel-Fah/ictukb/blob/local-chatbot/docs/joelfah/proposals/golden-questions-fr.yml).

| Id | Question | Mirrors |
|---|---|---|
| FR-01 | Comment postuler à ICT University ? | ADM-01 |
| FR-02 | Quels documents faut-il fournir pour une candidature en Bachelor ? | ADM-02 |
| FR-03 | Quelles sont les conditions d'admission en Master ? | ADM-03 |
| FR-04 | Y a-t-il des frais de dossier, et combien coûtent-ils ? | ADM-06 |
| FR-05 | Puis-je être transféré depuis une autre université ? | ADM-07 |
| FR-06 | Quelles formations propose ICT University ? | PRG-01 |
| FR-07 | Combien de temps dure le Master ? | PRG-06 |
| FR-08 | Quelle est la date limite d'inscription aux cours ? | PRC-02 |
| FR-09 | Que se passe-t-il si je rate l'inscription aux cours ? | PRC-03 |
| FR-10 | Puis-je ajouter ou supprimer un cours après mon inscription ? | PRC-04 |
| FR-11 | Qui peut passer un rattrapage, et combien cela coûte-t-il ? | PRC-06 |
| FR-12 | Comment demander un relevé de notes officiel ? | PRC-08 |
| FR-13 | Comment faire une réclamation sur une note ? | PRC-14 |
| FR-14 | Comment ma moyenne (GPA) est-elle calculée, et quel est le barème de notation ? | PRC-16 |
| FR-15 | Quel est le taux de présence minimum exigé ? | PRC-17 |
| FR-16 | Puis-je payer mes frais de scolarité en plusieurs tranches ? | FIN-04 |
| FR-17 | Quelles sont les dates et les montants des tranches ? | FIN-05 |
| FR-18 | Quels moyens de paiement sont acceptés ? | FIN-06 |
| FR-19 | Que se passe-t-il si je paie en retard ? | FIN-07 |
| FR-20 | Qu'est-ce que le quitus financier (financial clearance) et comment l'obtenir ? | FIN-08 |
| FR-21 | Qu'est-ce que l'ERP et que puis-je y faire ? | ERP-01 |
| FR-22 | Comment me connecter à l'ERP pour la première fois ? | ERP-02 |
| FR-23 | J'ai oublié mon mot de passe ERP. Que dois-je faire ? | ERP-03 |
| FR-24 | Où puis-je voir mes résultats sur l'ERP ? | ERP-05 |
| FR-25 | Où se trouve l'université ? | CMP-01 |
| FR-26 | Quand ont lieu les examens ? | TTB-03 |

Native French speakers may want to adjust the wording to how students actually ask (e.g. "rattrapage",
"quitus"); the ids and `expected_docs` stay the same.

## Possible follow-up (content)

Question-style headings in French for the most asked topics (a French heading line next to the English one) would
help the keyword half of the search. That's a content decision for the category owners; we can measure the effect
with these questions once they're in the set.
