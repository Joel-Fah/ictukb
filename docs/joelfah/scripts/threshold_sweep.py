"""Measure the best similarity per golden question on the configured index and sweep MIN_SIMILARITY values.

Usage (repo root, venv active, FASTEMBED_CACHE_PATH exported):
    python docs/joelfah/scripts/threshold_sweep.py [0.80 0.81 0.82 ...]

"Answerable" = questions with expected_docs whose expected document is in the top 5; "no-answer" = questions with
no expected_docs. A good threshold keeps the first above it and the second below it.
"""

from __future__ import annotations

import sys

from ictkb.config import get_settings
from ictkb.db import connect
from ictkb.embedding import get_embedder
from ictkb.evaluation import load_golden, matches
from ictkb.search import search

DEFAULT_THRESHOLDS = [0.80, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86]


def main() -> int:
    thresholds = [float(x) for x in sys.argv[1:]] or DEFAULT_THRESHOLDS
    golden = load_golden(get_settings().root / "eval" / "golden_questions.yml")
    embedder = get_embedder()
    answerable: list[tuple[str, float]] = []
    no_answer: list[tuple[str, float]] = []
    with connect() as conn:
        for q in golden:
            outcome = search(conn, embedder, q["question"], 5)
            best = max((r["similarity"] for r in outcome.results), default=0.0)
            expected = q.get("expected_docs") or []
            if not expected:
                no_answer.append((q["id"], best))
            elif any(matches(e, r["document"]["id"]) for r in outcome.results for e in expected):
                answerable.append((q["id"], best))

    scores = sorted(s for _, s in answerable)
    print(f"answerable and retrieved: n={len(scores)}  min={scores[0]:.3f}  median={scores[len(scores) // 2]:.3f}")
    print("no-answer: " + ", ".join(f"{i}={s:.3f}" for i, s in sorted(no_answer, key=lambda x: -x[1])))
    print("\nthreshold | answerable kept | no-answer refused")
    for t in thresholds:
        kept = sum(s >= t for _, s in answerable)
        refused = sum(s < t for _, s in no_answer)
        print(f"  {t:.2f}    | {kept:3}/{len(answerable)} ({kept / len(answerable):.0%}) | {refused}/{len(no_answer)}")
    lowest = sorted(answerable, key=lambda x: x[1])[:8]
    print("\nlowest answerable: " + ", ".join(f"{i}={s:.3f}" for i, s in lowest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
