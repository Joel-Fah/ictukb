# Upstream issue drafts (Egbemichel/ictukb)

Each file is one issue: the first `# ` line is the title, the rest is the body. Post with:

```bash
f=docs/joelfah/issues/01-local-setup-needs-admin-token.md
gh issue create -R Egbemichel/ictukb --title "$(head -1 "$f" | sed 's/^# //')" --body "$(tail -n +3 "$f")"
```

| # | File | Area | Needs infra-owner approval to fix | Status |
|---|---|---|---|---|
| 01 | [01-local-setup-needs-admin-token.md](01-local-setup-needs-admin-token.md) | README / `.env.example` | No (docs) | posted: [#2](https://github.com/Egbemichel/ictukb/issues/2) |
| 02 | [02-fastembed-cache-in-tmp.md](02-fastembed-cache-in-tmp.md) | `src/` | Yes | posted: [#3](https://github.com/Egbemichel/ictukb/issues/3) |
| 03 | [03-min-similarity-per-provider.md](03-min-similarity-per-provider.md) | config / docs | No (docs) | posted: [#9](https://github.com/Egbemichel/ictukb/issues/9) |
| 04 | [04-fastapi-missing-answer-verification.md](04-fastapi-missing-answer-verification.md) | `src/` or docs | Depends on option | posted: [#4](https://github.com/Egbemichel/ictukb/issues/4) |
| 05 | [05-compose-db-port-exposed.md](05-compose-db-port-exposed.md) | `docker/` | Yes | posted: [#5](https://github.com/Egbemichel/ictukb/issues/5) |
| 06 | [06-docs-still-say-cohere.md](06-docs-still-say-cohere.md) | `docs/` | No (docs) | posted: [#6](https://github.com/Egbemichel/ictukb/issues/6) |

### Phase 4: knowledge-base content and evaluation

| # | File | Area | Template | Covers | Status |
|---|---|---|---|---|---|
| 07 | [07-sheets-not-configured.md](07-sheets-not-configured.md) | `sources/sheets.yml` (infra) | none | 14 uncovered golden questions waiting for 8 unconfigured Google Sheets | posted: [#10](https://github.com/Egbemichel/ictukb/issues/10) |
| 08 | [08-missing-campus.md](08-missing-campus.md) | content: campus | missing-info | CMP-02, CMP-07, CMP-08 | posted: [#11](https://github.com/Egbemichel/ictukb/issues/11) |
| 09 | [09-missing-canteen.md](09-missing-canteen.md) | content: canteen | missing-info | CAN-02, CAN-04, VAR-05 (+ heading note) | posted: [#12](https://github.com/Egbemichel/ictukb/issues/12) |
| 10 | [10-missing-transport.md](10-missing-transport.md) | content: transport | missing-info | TRN-01, TRN-03 | posted: [#13](https://github.com/Egbemichel/ictukb/issues/13) |
| 11 | [11-missing-student-life.md](11-missing-student-life.md) | content: student life | missing-info | STL-02, STL-03, STL-04, STL-06 | posted: [#14](https://github.com/Egbemichel/ictukb/issues/14) |
| 12 | [12-missing-programs.md](12-missing-programs.md) | content: programs, admissions, procedures, finance, erp, people | missing-info | ADM-04, ADM-08, PRG-03, PRG-07, PRG-08, PRC-11, FIN-09, ERP-08, PPL-03 | posted: [#15](https://github.com/Egbemichel/ictukb/issues/15) |
| 13 | [13-content-structure-findings.md](13-content-structure-findings.md) | content (all) + CONTRIBUTING | none | 4 writing patterns behind wrong answers, with evidence | posted: [#16](https://github.com/Egbemichel/ictukb/issues/16) |
| 14 | [14-french-golden-questions.md](14-french-golden-questions.md) | `eval/` (infra) | none | 26 French golden questions; French hit@5 20/26 vs English 26/26 | posted: [#17](https://github.com/Egbemichel/ictukb/issues/17) |
| 15 | [15-multi-hop-retrieval.md](15-multi-hop-retrieval.md) | `src/` (infra) + content + `eval/` | none | MHP-01 (one document fills the top 5), MHP-02 (expected document lacks the answer) | posted: [#18](https://github.com/Egbemichel/ictukb/issues/18) |

Together, 07-12 cover all 35 "Not yet covered" golden questions of `docs/evaluation-latest.md` (MHP-04 and VAR-03
via 07). They were generated from the repo's own files by
[../scripts/coverage_gaps.py](../scripts/coverage_gaps.py); they add no facts about the university.

The templates' labels (`missing-info`) can only be set by the maintainers, so each body follows the template's
fields instead.

## Pull requests

| PR | Branch | Fixes | Status |
|---|---|---|---|
| [#7](https://github.com/Egbemichel/ictukb/pull/7) | `docs/embedding-provider-refs` | #6 | open |
| [#8](https://github.com/Egbemichel/ictukb/pull/8) | `docs/readme-local-embeddings` | #2 (docs part) | open |

Both add the same `contributors.yml` entry; when one merges, the other's identical change should merge cleanly.
