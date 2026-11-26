"""Builds docs/joelfah/verdict-review.md: each question once, the passages the models saw, and both answers with
Claude's verdict, so a human can confirm or change each verdict. Run from the repo root with the venv active."""

import csv
import re
from pathlib import Path

from ictkb.db import connect

R = Path("chatbot/reports")
PAIRS = [  # (title, 3B report, 7B report, headings taken from this report)
    ("The 20 evaluation questions", "final", "qwen7b", "qwen7b"),
    ("The two list questions (asked of both models on 2026-11-26)", "qwen3b-lists", "qwen7b-lists", "qwen7b-lists"),
]
LINE = re.compile(r"^\s+(\d\.\d{3})\s+(\S+)\s+\[(.*)\](.*)$")


def rows(label):
    return {r["id"]: r for r in csv.DictReader(open(R / f"generation-{label}.csv", newline=""))}


def retrieved_headings(label):
    """{question id: [(similarity, doc_id, heading, flags)]} from the report's retrieval lines."""
    out, qid = {}, None
    for line in (R / f"generation-{label}.md").read_text().splitlines():
        m = re.match(r"^### (\S+) \(", line)
        if m:
            qid = m.group(1)
            out[qid] = []
        m = LINE.match(line)
        if m and qid:
            out[qid].append((m.group(1), m.group(2), m.group(3), m.group(4).strip()))
    return out


def verdict_text(r):
    note = r["verdict_note"].replace("[checked against sources by Claude; confirm] ", "")
    return f"**{r['verdict']}**: {note}"


def quote(text):
    return "\n".join("> " + l if l.strip() else ">" for l in text.strip().splitlines())


conn = connect()
chunk = {}
for r in conn.execute("select document_id, heading_path, content from chunks"):
    chunk[(r["document_id"], r["heading_path"] or "")] = r["content"]

md = ["# Verdict review", "",
      "Confirm or change Claude's verdict on each model answer. These verdicts are the basis of every quality number "
      "in [models.md](models.md) and [BENCHMARKS](../../chatbot/BENCHMARKS.md).", "",
      "**How:** read each question's sources, then both answers. On each `Your verdict:` line write **ok** if you agree, "
      "or your verdict (*correct*, *partial*, *wrong*, *refused*) and a few words why. Tip: open the preview "
      "(Ctrl+Shift+V) next to this file to read, and edit here.", "",
      "**Verdict scale:** *correct* = every fact matches the sources; *partial* = facts right but incomplete, a "
      "condition dropped, or a minor unsupported detail; *wrong* = a wrong or invented fact, or another topic; "
      "*refused* = says it doesn't know. For the no-answer questions (NEG-), a refusal is the right outcome.", ""]
count = 0
for title, a_label, b_label, h_label in PAIRS:
    a, b, heads = rows(a_label), rows(b_label), retrieved_headings(h_label)
    md += ["---", "", f"## {title}", ""]
    skipped = [k for k in a if a[k]["used_llm"] == "False" and b[k]["used_llm"] == "False"]
    for qid, ra in a.items():
        if qid in skipped:
            continue
        rb = b[qid]
        md += [f"### {qid}: {ra['question']}", "",
               f"*{ra['category']}, {ra['type']}, {ra['language']}* · expected documents: "
               f"{ra['expected_docs'] or '(none: no answer expected)'}", "",
               "<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>", ""]
        for sim, doc, heading, flags in heads.get(qid, []):
            text = chunk.get((doc, heading), "(passage text not found in the database)")
            text = text.split("\n\n", 1)[-1]  # drop the "Title | Heading" line repeated at the top of each chunk
            md += [f"**{doc}** › {heading} · similarity {sim}{' · ' + flags if flags else ''}", "", quote(text), ""]
        md += ["</details>", ""]
        for label, r in (("3B", ra), ("7B", rb)):
            count += 1
            md += [f"**{label} answer** (cited: {r['cited'] or 'nothing'})", "", quote(r["answer"]), "",
                   f"Claude: {verdict_text(r)}", "", f"Your verdict ({label} {qid}): ", ""]
    if skipped:
        md += [f"*Not listed: {', '.join(skipped)}. The model wasn't called (below the similarity threshold or "
               "only unfilled drafts), so the code refused in both runs; there is nothing to judge.*", ""]

Path("docs/joelfah/verdict-review.md").write_text("\n".join(md))
print(f"{count} answers to review")
