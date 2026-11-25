"""Generation evaluation: run retrieval + the local model on golden questions and record what happened.

Run from the repository root (venv active, Ollama running):

    python -m chatbot.eval_generation --label baseline
    CHAT_MODEL=qwen2.5:1.5b python -m chatbot.eval_generation --label qwen1.5b
    CHAT_TOP_K=3 python -m chatbot.eval_generation --label topk3

Writes chatbot/reports/generation-<label>.csv (one row per question, with an empty `verdict` column to fill by
hand against the source documents: correct / partial / wrong / refused) and generation-<label>.md (summary, the
settings used, and every displayed answer).

Automatic columns are proxies, not verdicts: "expected doc retrieved" and "expected doc cited" say whether the right
document was found and used, not whether the answer is right.
"""

from __future__ import annotations

import argparse
import csv
import io
import statistics
import sys
import time
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from .chat import Assistant
from .config import Config
from .prompt import is_refusal

# 20 golden questions: 9 P0 across categories, 3 multi-hop, the 3 French variants, the 5 no-answer questions.
DEFAULT_IDS = [
    "ADM-01", "PRC-02", "PRC-09", "FIN-01", "FIN-05", "FIN-06", "ERP-02", "ERP-03", "TTB-03",
    "MHP-01", "MHP-02", "MHP-03",
    "VAR-01", "VAR-02", "VAR-03",
    "NEG-01", "NEG-02", "NEG-03", "NEG-04", "NEG-05",
]
REPORTS = Path(__file__).resolve().parent / "reports"
FIELDS = [
    "id", "category", "type", "language", "question", "expected_docs", "retrieved", "expected_retrieved",
    "confidence", "best_similarity", "used_llm", "cited", "expected_cited", "refused", "unverified", "redacted",
    "stopped", "first_token_s", "total_s", "prompt_tokens", "answer_tokens", "answer_tok_per_s", "answer",
    "verdict", "verdict_note",
]


class _Tee(io.StringIO):
    """Keeps a copy of the displayed answer for the report and, with --live, also prints it as it is written, so the
    run can be followed with `tail -f` on the log."""

    def __init__(self, live: bool) -> None:
        super().__init__()
        self.live = live

    def write(self, text: str) -> int:
        if self.live:
            sys.stdout.write(text)
            sys.stdout.flush()
        return super().write(text)


def _matches(expected: list[str], doc_ids: list[str]) -> bool:
    from ictkb.evaluation import matches

    return any(matches(e, d) for e in expected for d in doc_ids)


def run(ids: list[str], label: str, live: bool = False) -> Path:
    from ictkb.config import get_settings
    from ictkb.evaluation import load_golden

    golden = {q["id"]: q for q in load_golden(get_settings().root / "eval" / "golden_questions.yml")}
    missing = [i for i in ids if i not in golden]
    if missing:
        raise SystemExit(f"unknown golden ids: {missing}")
    cfg = Config.from_env()
    assistant = Assistant(cfg)
    rows, transcripts = [], []
    for n, qid in enumerate(ids, 1):
        q = golden[qid]
        expected = q.get("expected_docs") or []
        if live:
            print(f"\n===== [{n}/{len(ids)}] {qid} ({q['category']}, {q['language']}): {q['question']}", flush=True)
        buf = _Tee(live)
        started = time.perf_counter()
        turn = assistant.answer(q["question"], out=buf, debug=live)
        wall = time.perf_counter() - started
        retrieved = [p.doc_id for p in turn.retrieval.passages]
        s = turn.stats
        answer_tps = (s.get("eval_count") or 0) / ((s.get("eval_duration") or 1) / 1e9) if s else 0.0
        rows.append({
            "id": qid, "category": q["category"], "type": q["type"], "language": q["language"],
            "question": q["question"], "expected_docs": " ".join(expected), "retrieved": " ".join(retrieved),
            "expected_retrieved": _matches(expected, retrieved) if expected else "",
            "confidence": turn.retrieval.confidence, "best_similarity": round(turn.retrieval.best_similarity, 3),
            "used_llm": turn.used_llm, "cited": " ".join(turn.cited),
            "expected_cited": _matches(expected, turn.cited) if expected else "",
            "refused": (not turn.used_llm) or is_refusal(turn.answer),
            "unverified": " ".join(turn.unverified), "redacted": " ".join(turn.redacted), "stopped": turn.stopped,
            "first_token_s": round(turn.first_token_s, 1) if turn.first_token_s else "",
            "total_s": round(wall, 1), "prompt_tokens": s.get("prompt_eval_count", "") if s else "",
            "answer_tokens": s.get("eval_count", "") if s else "", "answer_tok_per_s": round(answer_tps, 1),
            "answer": turn.answer, "verdict": "", "verdict_note": "",
        })
        transcripts.append(f"### {qid} ({q['category']}, {q['type']}, {q['language']})\n\n> {q['question']}\n\n"
                           f"Expected: {', '.join(expected) or '(no answer expected)'}; retrieved: {', '.join(retrieved)}"
                           f"\n\n```\n{buf.getvalue().strip()}\n```\n")
        print(f"[{n}/{len(ids)}] {qid} {wall:.0f}s refused={rows[-1]['refused']} cited={turn.cited}", flush=True)

    REPORTS.mkdir(exist_ok=True)
    csv_path = REPORTS / f"generation-{label}.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    md_path = REPORTS / f"generation-{label}.md"
    md_path.write_text(_markdown(label, cfg, assistant, rows, transcripts), encoding="utf-8")
    return md_path


def _summary(rows: list[dict]) -> list[tuple[str, str]]:
    answerable = [r for r in rows if r["expected_docs"]]
    negative = [r for r in rows if not r["expected_docs"]]
    llm = [r for r in rows if r["used_llm"]]

    def pct(part: int, whole: int) -> str:
        return f"{part}/{whole} ({part / whole:.0%})" if whole else "-"

    def med(key: str) -> str:
        values = [float(r[key]) for r in llm if r[key] != ""]
        return f"{statistics.median(values):.1f}" if values else "-"

    return [
        ("Questions", str(len(rows))),
        ("Answerable: expected document retrieved (top-k)", pct(sum(r["expected_retrieved"] is True for r in answerable),
                                                               len(answerable))),
        ("Answerable: expected document cited", pct(sum(r["expected_cited"] is True for r in answerable), len(answerable))),
        ("Answerable: refused (false refusal if the document was retrieved)",
         pct(sum(r["refused"] for r in answerable), len(answerable))),
        ("No-answer: refused (correct)", pct(sum(r["refused"] for r in negative), len(negative))),
        ("Answers with unverified figures/dates", pct(sum(bool(r["unverified"]) for r in llm), len(llm))),
        ("Answers with removed contact details", pct(sum(bool(r["redacted"]) for r in llm), len(llm))),
        ("Answers stopped (loop or length cap)", pct(sum(bool(r["stopped"]) for r in llm), len(llm))),
        ("Model called", pct(len(llm), len(rows))),
        ("Median first token (s), model answers", med("first_token_s")),
        ("Median total time (s), model answers", med("total_s")),
        ("Median answer speed (tokens/s)", med("answer_tok_per_s")),
    ]


def _markdown(label: str, cfg: Config, assistant: Assistant, rows: list[dict], transcripts: list[str]) -> str:
    settings = {k: v for k, v in asdict(cfg).items()}
    settings["min_similarity (effective)"] = assistant.retriever.threshold
    lines = [f"# Generation evaluation: {label}", "", f"Run {datetime.now():%Y-%m-%d %H:%M}.", "", "## Settings", "",
             "| Setting | Value |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in settings.items()]
    lines += ["", "## Summary (automatic proxies; verdicts are filled by hand in the CSV)", "", "| Measure | Value |",
              "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in _summary(rows)]
    lines += ["", "## Per question", "", "| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | "
              "First token (s) | Total (s) | Verdict |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['id']} | {r['language']} | {r['expected_retrieved']} | {r['expected_cited']} | {r['refused']} | "
                     f"{r['unverified'] or ''} | {r['first_token_s']} | {r['total_s']} | {r['verdict']} |")
    lines += ["", "## Answers as displayed", ""] + transcripts
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--label", required=True, help="name of this configuration, used in the report file names")
    parser.add_argument("--ids", nargs="*", default=DEFAULT_IDS, help="golden question ids (default: 20 chosen ids)")
    parser.add_argument("--live", action="store_true",
                        help="print each answer as it is written, with retrieval scores and timings (for tail -f)")
    args = parser.parse_args()
    print(f"wrote {run(args.ids, args.label, args.live)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
