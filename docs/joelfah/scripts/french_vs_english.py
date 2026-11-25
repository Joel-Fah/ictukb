"""Retrieval for each proposed French golden question vs its English twin (rank of the first expected document).

Usage (repo root, venv, FASTEMBED_CACHE_PATH exported): python docs/joelfah/scripts/french_vs_english.py
"""

from __future__ import annotations

import re

import yaml

from ictkb.config import get_settings
from ictkb.db import connect
from ictkb.embedding import get_embedder
from ictkb.evaluation import matches
from ictkb.search import search

PROPOSAL = "docs/joelfah/proposals/golden-questions-fr.yml"


def rank(conn, embedder, question: str, expected: list[str]) -> tuple[int | None, float]:
    out = search(conn, embedder, question, 5)
    best = max((r["similarity"] for r in out.results), default=0.0)
    for i, r in enumerate(out.results, 1):
        if any(matches(e, r["document"]["id"]) for e in expected):
            return i, best
    return None, best


def main() -> None:
    english = {q["id"]: q for q in yaml.safe_load(open(get_settings().root / "eval" / "golden_questions.yml"))}
    text = open(PROPOSAL, encoding="utf-8").read()
    french = yaml.safe_load(text)
    twins = re.findall(r"# mirrors (\S+)", text)
    embedder = get_embedder()
    rows, hits = [], {"en": 0, "fr": 0}
    with connect() as conn:
        for fq, sid in zip(french, twins, strict=True):
            eq = english[sid]
            er, es = rank(conn, embedder, eq["question"], eq["expected_docs"])
            fr, fs = rank(conn, embedder, fq["question"], fq["expected_docs"])
            hits["en"] += er is not None
            hits["fr"] += fr is not None
            rows.append(f"| {fq['id']} / {sid} | {er or '-'} | {fr or '-'} | {es:.3f} | {fs:.3f} |")
    n = len(french)
    print("| French / English | Rank EN | Rank FR | Best sim. EN | Best sim. FR |\n|---|---|---|---|---|")
    print("\n".join(rows))
    print(f"\nhit@5: English {hits['en']}/{n}, French {hits['fr']}/{n}")


if __name__ == "__main__":
    main()
