"""Minimal local web page for the assistant (standard library only, works offline).

    python -m chatbot.web [--port 8765]        or   ./chatbot/run.sh --web

Serves http://127.0.0.1:<port>/ on the loopback interface only. The page streams each answer as it is written. It
uses the same pipeline as the terminal chat (chat.Assistant), so every safeguard applies: similarity threshold,
contact redaction, number/date check, draft/stale notes.

API: POST /api/ask with JSON {"question": "..."} returns newline-delimited JSON events:
    {"t": "text", "v": "..."}   a piece of the displayed answer (answer text, then sources and notes)
    {"t": "done", "turn": {...}} confidence, cited sources, flags and timings
    {"t": "error", "v": "..."}
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

MAX_QUESTION_CHARS = 500
ALLOWED_HOSTS = {"127.0.0.1", "localhost"}
PAGE = Path(__file__).with_name("web_page.html")


class EventWriter:
    """File-like object for Assistant.answer(out=...): every write becomes a {"t": "text"} event on the response."""

    def __init__(self, wfile) -> None:
        self.wfile = wfile

    def send(self, event: dict) -> None:
        self.wfile.write((json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8"))
        self.wfile.flush()

    def write(self, text: str) -> int:
        if text:
            self.send({"t": "text", "v": text})
        return len(text)

    def flush(self) -> None:
        pass


def turn_summary(turn) -> dict:
    """What the page shows under an answer: never the passages' full text, only references and measurements."""
    by_id = {p.doc_id: p for p in turn.retrieval.passages}
    return {
        "confidence": turn.retrieval.confidence,
        "best_similarity": round(turn.retrieval.best_similarity, 3),
        "threshold": turn.retrieval.threshold,
        "language": turn.language,
        "used_llm": turn.used_llm,
        "cited": [{"id": d, "title": by_id[d].title, "source": by_id[d].source, "last_verified": by_id[d].last_verified,
                   "status": by_id[d].status, "stale": by_id[d].stale} for d in turn.cited if d in by_id],
        "passages": [{"id": p.doc_id, "heading": p.heading, "similarity": round(p.similarity, 3),
                      "used": p in turn.context_passages} for p in turn.retrieval.passages],
        "unverified": turn.unverified,
        "redacted": len(turn.redacted),
        "stopped": turn.stopped,
        "first_token_s": round(turn.first_token_s, 1) if turn.first_token_s else None,
        "total_s": round(turn.total_s, 1),
    }


def make_handler(assistant, info: dict):
    lock = threading.Lock()  # one question at a time: the embedder, the DB connection and Ollama are shared

    class Handler(BaseHTTPRequestHandler):
        server_version = "ictu-assistant"

        def log_message(self, fmt: str, *args) -> None:  # quieter than the default (no client address)
            sys.stderr.write("web: " + (fmt % args) + "\n")

        def _host_ok(self) -> bool:
            host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]")
            return host in ALLOWED_HOSTS  # rejects other host names pointing at 127.0.0.1 (DNS rebinding)

        def _json(self, status: int, body: dict) -> None:
            data = json.dumps(body).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:  # noqa: N802 (http.server naming)
            if not self._host_ok():
                return self._json(HTTPStatus.FORBIDDEN, {"error": "use http://127.0.0.1"})
            if self.path in ("/", "/index.html"):
                data = PAGE.read_bytes()
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Content-Security-Policy",
                                 "default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline'")
                self.end_headers()
                self.wfile.write(data)
            elif self.path == "/api/info":
                self._json(HTTPStatus.OK, info)
            else:
                self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})

        def do_POST(self) -> None:  # noqa: N802
            if not self._host_ok():
                return self._json(HTTPStatus.FORBIDDEN, {"error": "use http://127.0.0.1"})
            if self.path != "/api/ask":
                return self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            # JSON only: a cross-site page can't send this content type without a CORS preflight, which we never accept.
            if not (self.headers.get("Content-Type") or "").startswith("application/json"):
                return self._json(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, {"error": "send application/json"})
            try:
                length = int(self.headers.get("Content-Length") or 0)
                question = str(json.loads(self.rfile.read(min(length, 10_000)) or b"{}").get("question", "")).strip()
            except (ValueError, AttributeError):
                return self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid JSON"})
            if not question or len(question) > MAX_QUESTION_CHARS:
                return self._json(HTTPStatus.BAD_REQUEST, {"error": f"ask a question of 1 to {MAX_QUESTION_CHARS} characters"})

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()  # HTTP/1.0: no length, the body ends when the connection closes, so it can stream
            writer = EventWriter(self.wfile)
            try:
                with lock:
                    turn = assistant.answer(question, out=writer)
                writer.send({"t": "done", "turn": turn_summary(turn)})
            except (BrokenPipeError, ConnectionResetError):
                pass  # the page was closed mid-answer
            except Exception as exc:  # noqa: BLE001 (report any failure to the page instead of a silent cut)
                try:
                    writer.send({"t": "error", "v": f"{type(exc).__name__}: {exc}"})
                except OSError:
                    pass

    return Handler


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local web page for the ICT University assistant")
    parser.add_argument("--port", type=int, default=int(os.environ.get("CHAT_WEB_PORT", "8765")))
    args = parser.parse_args(argv)

    from .chat import Assistant
    from .config import Config
    from .llm import OllamaError

    cfg = Config.from_env()
    try:
        assistant = Assistant(cfg)
    except (OllamaError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    info = {"model": cfg.model, "threshold": assistant.retriever.threshold, "top_k": cfg.top_k}
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(assistant, info))
    print(f"ICT University assistant: http://127.0.0.1:{args.port}  (local only; Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
