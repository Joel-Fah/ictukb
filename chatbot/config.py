"""Chatbot settings. Every default lives here and can be overridden by an environment variable.

The knowledge-base settings (DATABASE_URL, EMBEDDING_PROVIDER, MIN_SIMILARITY, KB_ENV) are read by ictkb from .env;
these are the chatbot's own settings.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# fastembed caches models in /tmp by default, which is emptied at boot (2.2 GB re-download, no offline use).
# This must run before fastembed is imported, which happens when the retriever loads the embedder.
os.environ.setdefault("FASTEMBED_CACHE_PATH", str(Path.home() / ".cache" / "fastembed"))


def _get(name: str, default, cast=str):
    raw = os.environ.get(name, "").strip()
    return cast(raw) if raw else default


@dataclass(frozen=True)
class Config:
    ollama_url: str  # OLLAMA_URL
    model: str  # CHAT_MODEL
    top_k: int  # CHAT_TOP_K: passages retrieved per question
    max_chunk_chars: int  # CHAT_MAX_CHUNK_CHARS: each passage is cut to this length
    max_context_chars: int  # CHAT_MAX_CONTEXT_CHARS: all passages together
    min_similarity: float | None  # CHAT_MIN_SIMILARITY; None = MIN_SIMILARITY from .env (ictkb settings)
    relative_cutoff: float  # CHAT_RELATIVE_CUTOFF: drop passages scoring this much below the best one
    num_ctx: int  # CHAT_NUM_CTX: model context window in tokens
    temperature: float  # CHAT_TEMPERATURE
    repeat_penalty: float  # CHAT_REPEAT_PENALTY: discourages the model from repeating itself
    max_answer_tokens: int  # CHAT_MAX_ANSWER_TOKENS: hard cap on answer length
    seed: int  # CHAT_SEED: fixed sampling seed, so the same question and passages give the same answer
    keep_alive: str  # CHAT_KEEP_ALIVE: how long Ollama keeps the model loaded between questions

    @classmethod
    def from_env(cls) -> Config:
        return cls(
            ollama_url=_get("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/"),
            model=_get("CHAT_MODEL", "qwen2.5:3b"),
            top_k=_get("CHAT_TOP_K", 4, int),
            max_chunk_chars=_get("CHAT_MAX_CHUNK_CHARS", 1200, int),
            max_context_chars=_get("CHAT_MAX_CONTEXT_CHARS", 4000, int),
            min_similarity=_get("CHAT_MIN_SIMILARITY", None, float),
            relative_cutoff=_get("CHAT_RELATIVE_CUTOFF", 0.05, float),
            num_ctx=_get("CHAT_NUM_CTX", 4096, int),
            temperature=_get("CHAT_TEMPERATURE", 0.1, float),
            repeat_penalty=_get("CHAT_REPEAT_PENALTY", 1.05, float),  # Qwen 2.5's own default; 1.15 corrupted dates
            max_answer_tokens=_get("CHAT_MAX_ANSWER_TOKENS", 400, int),
            # Without a seed, 14 of 20 answers changed between two runs with identical passages (Phase 3).
            seed=_get("CHAT_SEED", 42, int),
            keep_alive=_get("CHAT_KEEP_ALIVE", "30m"),
        )
