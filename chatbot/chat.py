"""Terminal chat. Run from the repository root (ictkb reads .env from the current directory):

    python -m chatbot.chat                 interactive; commands: /quit, /sources, /debug
    python -m chatbot.chat "question" ...  answer each question and exit (add --debug for scores and timings)
"""

from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass, field

from .config import Config
from .llm import OllamaChat, OllamaError, is_looping
from .prompt import (
    SYSTEM_PROMPT,
    UNVERIFIED,
    ContactRedactor,
    build_context,
    build_user_message,
    cited_ids,
    detect_language,
    fallback_message,
    is_refusal,
    source_notes,
    unverified_facts,
)
from .retrieval import Passage, Retrieval, Retriever

HELP = "Ask a question about ICT University. Commands: /sources (last sources), /debug (toggle details), /quit"


@dataclass
class Turn:
    question: str
    language: str
    retrieval: Retrieval
    used_llm: bool = False
    answer: str = ""
    context_passages: list[Passage] = field(default_factory=list)
    cited: list[str] = field(default_factory=list)
    first_token_s: float | None = None
    total_s: float = 0.0
    stats: dict = field(default_factory=dict)
    stopped: str = ""  # "" | "loop" (repetition guard) | "length" (answer token cap)
    unverified: list[str] = field(default_factory=list)  # numbers/months in the answer that the sources don't contain
    redacted: list[str] = field(default_factory=list)  # emails/URLs the model wrote that the sources don't contain


REDACTED_NOTE = {
    "en": "Note: the model wrote a contact detail that is not in the knowledge base; it was removed. "
          "Use only the official contacts below or in the cited documents.",
    "fr": "Remarque : le modèle a écrit une coordonnée absente de la base de connaissances ; elle a été retirée. "
          "Utilisez uniquement les contacts officiels ci-dessous ou dans les documents cités.",
}


SOURCES_NOT_CITED = {
    "en": "Sources given to the model (it did not cite them; check the answer against them):",
    "fr": "Sources fournies au modèle (il ne les a pas citées ; vérifiez la réponse avec elles) :",
}

STOPPED = {
    "loop": {"en": "[answer stopped: the model started repeating itself]",
             "fr": "[réponse interrompue : le modèle se répétait]"},
    "length": {"en": "[answer cut at the length limit]", "fr": "[réponse coupée à la longueur maximale]"},
}


class Assistant:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.llm = OllamaChat(cfg)
        self.llm.check()
        print(f"Loading the embedding model and {cfg.model} …", file=sys.stderr, flush=True)
        self.retriever = Retriever(cfg)
        self.contacts = self.retriever.contacts()
        self.llm.warm_up()

    def answer(self, question: str, out=sys.stdout, debug: bool = False) -> Turn:
        started = time.perf_counter()
        language = detect_language(question)
        turn = Turn(question, language, self.retriever.retrieve(question))
        r = turn.retrieval
        if debug:
            print(f"[retrieval {r.seconds * 1000:.0f} ms, confidence={r.confidence}, best={r.best_similarity:.3f}, "
                  f"threshold={r.threshold:.2f}, language={language}]", file=out)
            for p in r.passages:
                flags = " DRAFT" if p.status != "verified" else ""
                flags += " STALE" if p.stale else ""
                print(f"  {p.similarity:.3f}  {p.doc_id}  [{p.heading}]{flags}", file=out)

        categories = {p.category for p in r.passages[:2]}
        if r.confidence != "high":
            # Below the threshold the model is not called at all: a refusal can't be wrong.
            turn.answer = fallback_message(language, self.contacts, categories)
            print(turn.answer, file=out)
            turn.total_s = time.perf_counter() - started
            return turn

        context, turn.context_passages = build_context(r.passages, self.cfg.max_chunk_chars, self.cfg.max_context_chars,
                                                       self.cfg.relative_cutoff)
        if not turn.context_passages:
            # Every relevant passage is an unfilled placeholder: nothing to answer from, so don't ask the model.
            turn.answer = fallback_message(language, self.contacts, categories)
            print(turn.answer, file=out)
            turn.total_s = time.perf_counter() - started
            return turn
        user = build_user_message(question, context, language)
        turn.used_llm = True
        pieces: list[str] = []
        redactor = ContactRedactor(context, language)
        stream = self.llm.stream(SYSTEM_PROMPT, user)
        for piece in stream:
            if turn.first_token_s is None:
                turn.first_token_s = time.perf_counter() - started
            pieces.append(piece)
            print(redactor.feed(piece), end="", flush=True, file=out)
            if "\n" in piece and is_looping("".join(pieces)):
                stream.close()  # closes the HTTP stream, which makes Ollama stop generating
                turn.stopped = "loop"
                break
        print(redactor.flush(), file=out)
        turn.answer = "".join(pieces)
        turn.stats = self.llm.last_stats
        if turn.stats.get("done_reason") == "length":
            turn.stopped = "length"
        if turn.stopped:
            print(STOPPED[turn.stopped][language], file=out)
        turn.cited = cited_ids(turn.answer, turn.context_passages)
        turn.redacted = redactor.removed
        turn.unverified = [x for x in unverified_facts(turn.answer, context, question) if x not in turn.redacted]
        if turn.redacted:
            print("\n" + REDACTED_NOTE[language], file=out)
        if turn.unverified:
            print("\n" + UNVERIFIED[language].format(items=", ".join(turn.unverified)), file=out)

        if is_refusal(turn.answer) and not turn.cited:
            print("\n" + fallback_message(language, self.contacts, categories), file=out)
        else:
            # Cited sources; if the model cited nothing, list what it was given so the answer can still be checked.
            shown = turn.cited or list(dict.fromkeys(p.doc_id for p in turn.context_passages))
            print("\n" + ("Sources:" if turn.cited else SOURCES_NOT_CITED[language]), file=out)
            by_id = {p.doc_id: p for p in turn.context_passages}
            for doc_id in shown:
                p = by_id[doc_id]
                print(f"  [{doc_id}] {p.title} ({p.source}, verified {p.last_verified})", file=out)
            for note in source_notes(language, turn.context_passages, shown):
                print(note, file=out)
            if is_refusal(turn.answer):
                print("\n" + fallback_message(language, self.contacts, categories), file=out)

        turn.total_s = time.perf_counter() - started
        if debug:
            s = turn.stats
            tps = (s.get("eval_count") or 0) / ((s.get("eval_duration") or 1) / 1e9)
            pps = (s.get("prompt_eval_count") or 0) / ((s.get("prompt_eval_duration") or 1) / 1e9)
            print(f"[first token {turn.first_token_s or 0:.1f} s, total {turn.total_s:.1f} s, "
                  f"prompt {s.get('prompt_eval_count')} tok at {pps:.0f} tok/s, "
                  f"answer {s.get('eval_count')} tok at {tps:.1f} tok/s]", file=out)
        return turn


def print_sources(turn: Turn | None) -> None:
    if turn is None:
        print("No question asked yet.")
        return
    for p in turn.retrieval.passages:
        used = "used " if p in turn.context_passages else "      "
        print(f"{used}{p.similarity:.3f}  [{p.doc_id}] {p.title} > {p.heading}\n"
              f"        {p.source}  verified {p.last_verified}  status={p.status}{'  STALE' if p.stale else ''}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ICT University assistant (local)")
    parser.add_argument("questions", nargs="*", help="answer these questions and exit")
    parser.add_argument("--debug", action="store_true", help="show retrieved passages, scores and timings")
    args = parser.parse_args(argv)

    try:
        assistant = Assistant(Config.from_env())
    except (OllamaError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.questions:
        for q in args.questions:
            print(f"\n> {q}")
            assistant.answer(q, debug=args.debug)
        return 0

    print(HELP)
    debug, last = args.debug, None
    while True:
        try:
            question = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not question:
            continue
        if question in ("/quit", "/exit"):
            return 0
        if question == "/debug":
            debug = not debug
            print(f"debug {'on' if debug else 'off'}")
            continue
        if question == "/sources":
            print_sources(last)
            continue
        if question.startswith("/"):
            print(HELP)
            continue
        try:
            last = assistant.answer(question, debug=debug)
        except OllamaError as exc:
            print(f"error: {exc}")
        except KeyboardInterrupt:
            print("\n(interrupted)")


if __name__ == "__main__":
    raise SystemExit(main())
