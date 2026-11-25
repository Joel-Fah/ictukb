"""Print, per golden question that production does not cover, which document it needs, what is missing in that
document (unfilled sections, or an unconfigured Google Sheet), what to collect and from which office.

Sources: eval/golden_questions.yml, content/, sources/sheets.yml, docs/upload-checklist.csv,
docs/evaluation-latest.md (the production "Not yet covered" list). Usage: python docs/joelfah/scripts/coverage_gaps.py
"""

from __future__ import annotations

import csv
import glob
import json
import re
from collections import defaultdict

import yaml

golden = {q["id"]: q for q in yaml.safe_load(open("eval/golden_questions.yml", encoding="utf-8"))}
latest = open("docs/evaluation-latest.md", encoding="utf-8").read()
uncovered = re.findall(r"[A-Z]{3}-\d\d", latest.split("## Not yet covered", 1)[1])
sheets = {s["doc_id"]: s for s in yaml.safe_load(open("sources/sheets.yml", encoding="utf-8"))["sheets"]}
checklist = defaultdict(list)
for r in csv.DictReader(open("docs/upload-checklist.csv", encoding="utf-8")):
    checklist[r["document"]].append({"priority": r["priority"], "item": r["item"], "file": r["file_name"],
                                     "office": r["maintainer"]})
docs = {}
for path in glob.glob("content/**/*.md", recursive=True):
    if "_extracted" in path:
        continue
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^id: (\S+)$", text, re.M)
    if not m:
        continue
    sections = re.split(r"^## ", text, flags=re.M)[1:]
    unfilled = [s.split("\n", 1)[0].strip() for s in sections if "[[TO FILL]]" in s]
    status = re.search(r"^status: (\S+)$", text, re.M).group(1)
    docs[m.group(1)] = {"path": path, "status": status, "unfilled": unfilled}

out = []
for qid in uncovered:
    q = golden[qid]
    needs = []
    for d in q.get("expected_docs") or []:
        if d in docs:
            state = {"kind": "draft" if docs[d]["status"] != "verified" else "verified", "path": docs[d]["path"],
                     "unfilled": docs[d]["unfilled"]}
        elif d in sheets:
            state = {"kind": "sheet", "sheet_id_set": bool(sheets[d].get("sheet_id")),
                     "template": f"templates/sheets/{sheets[d]['name']}.csv"}
        else:
            state = {"kind": "absent"}
        needs.append({"doc": d, **state, "collect": checklist.get(d, [])})
    out.append({"id": qid, "priority": q["priority"], "category": q["category"], "question": q["question"],
                "needs": needs})
print(json.dumps(out, indent=1, ensure_ascii=False))
