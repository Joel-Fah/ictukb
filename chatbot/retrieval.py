"""Retrieval, in-process: calls ictkb.search.search() directly (no API server, one copy of e5 in memory)."""

from __future__ import annotations

import time
from dataclasses import dataclass

import psycopg

from .config import Config

LOCAL_PROVIDERS = {"fastembed"}
CONTACTS_DOC = "about-contacts"


@dataclass
class Passage:
    doc_id: str
    title: str
    heading: str
    text: str
    category: str
    source: str  # website URL, or the file path in content/
    last_verified: str
    stale: bool
    status: str  # verified | draft
    similarity: float


@dataclass
class Retrieval:
    confidence: str  # high | low | none
    best_similarity: float
    threshold: float
    passages: list[Passage]
    seconds: float


def body_of(chunk: str) -> str:
    """Chunks start with a 'title | heading' line, then a blank line; return what follows."""
    _, _, rest = chunk.partition("\n")
    return rest.strip() or chunk.strip()


class Retriever:
    def __init__(self, cfg: Config) -> None:
        from ictkb.config import get_settings
        from ictkb.embedding import get_embedder

        settings = get_settings()
        if settings.embedding_provider.lower() not in LOCAL_PROVIDERS:
            raise RuntimeError(
                f"EMBEDDING_PROVIDER={settings.embedding_provider} calls a cloud service; this chatbot is local-only. "
                "Set EMBEDDING_PROVIDER=fastembed in .env (see docs/joelfah/01-local-setup.md)."
            )
        self.cfg = cfg
        self.threshold = cfg.min_similarity if cfg.min_similarity is not None else settings.min_similarity
        self.embedder = get_embedder()  # loads e5 (a few seconds, about 1.6 GB of RAM)
        self.conn = self._connect()
        self.embedder.embed_query("warm-up")  # the first ONNX call is slow; pay it at start-up

    @staticmethod
    def _connect() -> psycopg.Connection:
        from ictkb.db import connect

        return connect(autocommit=True)

    def _search(self, question: str):
        from ictkb.search import search

        try:
            return search(self.conn, self.embedder, question, self.cfg.top_k)
        except psycopg.OperationalError:  # database restarted: reconnect once
            self.conn = self._connect()
            return search(self.conn, self.embedder, question, self.cfg.top_k)

    def retrieve(self, question: str) -> Retrieval:
        started = time.perf_counter()
        outcome = self._search(question)
        passages = []
        for r in outcome.results:
            d = r["document"]
            passages.append(Passage(
                doc_id=d["id"], title=d["title"], heading=r["heading_path"] or "", text=body_of(r["text"]),
                category=d["category"], source=d["source_url"] or f"content/{d['category']}/{d['id']}.md",
                last_verified=d["last_verified"], stale=d["stale"], status=d["status"], similarity=r["similarity"],
            ))
        best = max((p.similarity for p in passages), default=0.0)
        confidence = "none" if not passages else ("high" if best >= self.threshold else "low")
        return Retrieval(confidence, best, self.threshold, passages, time.perf_counter() - started)

    def contacts(self) -> dict[str, str]:
        """Sections of the about-contacts document, by heading, read from the index (never from memory)."""
        rows = self.conn.execute(
            "SELECT heading_path, content FROM chunks WHERE document_id = %s ORDER BY chunk_index", (CONTACTS_DOC,)
        ).fetchall()
        return {r["heading_path"]: body_of(r["content"]) for r in rows}
