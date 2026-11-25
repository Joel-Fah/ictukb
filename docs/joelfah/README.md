# Local-first ICT University assistant: project journal

This folder records how we built a chatbot that answers questions about ICT University (admissions, programs, fees,
registration, ERP, campus, transport, student life) **entirely on a student laptop**: no cloud service, no paid key,
no GPU. It documents what we did, why we did it, how each part works, and what we measured, including the
problems we hit.

Author: Joel-Fah. Work happens on the `local-chatbot` branch of our fork of
[Egbemichel/ictukb](https://github.com/Egbemichel/ictukb), the shared ICT University knowledge base.

## Contents

**Start here:** [journey.md](journey.md), the overview: process, challenges, trade-offs, lessons.

| Page | What it covers | Status |
|---|---|---|
| [journey.md](journey.md) | The whole story in one page | updated each phase |
| [failure-log.md](failure-log.md) | Every failure and hallucination observed: what, why, fix, status | updated each phase |
| [00-inspection.md](00-inspection.md) | Phase 0: the laptop, the repo, and the three design choices | done |
| [01-local-setup.md](01-local-setup.md) | Phase 1: the knowledge base running locally (database, embeddings, index, website crawl) | done |
| [02-chatbot.md](02-chatbot.md) | Phase 2: the terminal chatbot, how it answers, 4 rounds of testing and fixes | done |
| [03-evaluation.md](03-evaluation.md) | Phase 3: 5 evaluation runs, model and setting comparisons, weakest areas, measurement noise | done |
| [04-contributions.md](04-contributions.md) | Phase 4: what we sent upstream, what we prepared, and why no content was filled | issues posted |
| [05-packaging-and-web.md](05-packaging-and-web.md) | Phase 5: two-command setup, the local web page, how they were tested | done |
| [issues/](issues/README.md) | Issues and pull requests we sent to the shared knowledge base | ongoing |
| [reports/](reports/) | Raw transcripts and evaluation reports (Phases 1-2; Phase 3 reports are in `chatbot/reports/`) | |
| [scripts/](scripts/) | Small measurement scripts (threshold sweep) | |

## The idea in one picture

```
              one-time setup                                    every question
 ┌──────────────────────────────────────────┐   ┌────────────────────────────────────────────────┐
 content/*.md ──┐                                question ──► embed (e5) ──┐
                ├─► split into chunks ─► embed ─► PostgreSQL + pgvector ◄──┘ hybrid search
 website pages ─┘     (by heading)       (e5)      (vectors + keywords)        │ top 3-4 chunks
                                                                            ▼
                                            rules + chunks + question ─► small local LLM (Ollama)
                                                                            │
                                            answer + sources + "may be out of date" warning
                                            or "I don't know, contact <office>"
```

This pattern is called **retrieval-augmented generation (RAG)**: the language model doesn't answer from what it
memorised in training (which knows nothing reliable about ICT University). It answers only from passages we
retrieve from the school's own documents, and it cites them.

## Words used in this journal

| Term | Meaning here |
|---|---|
| **Knowledge base** | The Markdown files in `content/` (one per topic, with front matter such as `status`, `last_verified`), plus pages crawled from the university website. |
| **Chunk** | A piece of a document, cut at Markdown headings (at most about 380 tokens). Each chunk starts with the document title and heading path, e.g. "How do I register for courses each semester?", so it makes sense on its own. |
| **Embedding** | A list of 1024 numbers that represents the meaning of a text. Texts with similar meaning get similar vectors, even with different words or languages (English/French). |
| **e5** | `intfloat/multilingual-e5-large`, the embedding model we run locally (through `fastembed` and ONNX Runtime). |
| **Cosine similarity** | How close two embeddings are (1.0 = same direction). The search reports the similarity of the best chunk. |
| **pgvector** | A PostgreSQL extension that stores embeddings and finds the nearest ones. |
| **Hybrid search** | The repo combines two rankings, vector similarity and keyword match (PostgreSQL full-text search), using reciprocal rank fusion. Keywords catch exact terms like "ERP" or a course code; vectors catch paraphrases. |
| **Confidence** | `high` if the best chunk's similarity reaches `MIN_SIMILARITY`, otherwise `low`/`none`. The chatbot only calls the language model on `high`. |
| **LLM** | The language model that writes the answer. We use a small quantised one (`qwen2.5:3b`, about 2 GB) through **Ollama**, a local model server. |
| **Quantised** | Model weights stored with fewer bits (here about 4 bits), so the model fits in RAM and runs on a CPU, with a small loss of quality. |
| **Staging / production** | Production indexes only `status: verified` documents; staging also indexes drafts. Locally we use staging. |

## Ground rules we follow

- Answers come only from retrieved text; no facts about the school from general knowledge.
- Content we contribute must come from a named official source, or the `[[TO FILL]]` placeholder stays.
- No personal phone numbers or emails, no secrets, `.env` is never committed.
- Shared infrastructure (`src/`, `db/`, `docker/`, `.github/`, `schema/`, `eval/`) is changed only after an issue
  and the infrastructure owner's approval. Our code lives in `chatbot/`.
