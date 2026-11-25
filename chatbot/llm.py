"""Streaming chat with a local model through Ollama's HTTP API (httpx is already a repo dependency)."""

from __future__ import annotations

import json
from collections.abc import Iterator

import httpx

from .config import Config


class OllamaError(RuntimeError):
    pass


def is_looping(text: str, times: int = 3) -> bool:
    """True when the last `times` complete non-empty lines are identical (a small model stuck repeating itself)."""
    lines = [line.strip() for line in text.split("\n")[:-1] if line.strip()]  # [:-1] skips the unfinished line
    return len(lines) >= times and len(set(lines[-times:])) == 1


class OllamaChat:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.last_stats: dict = {}

    def check(self) -> None:
        """Fail early with a clear message if Ollama isn't running or the model isn't pulled."""
        try:
            tags = httpx.get(f"{self.cfg.ollama_url}/api/tags", timeout=5).json()
        except httpx.HTTPError as exc:
            raise OllamaError(f"Ollama is not reachable at {self.cfg.ollama_url} ({exc}). "
                              "Start it with: sudo systemctl start ollama") from exc
        names = {m["name"] for m in tags.get("models", [])}
        if self.cfg.model not in names and f"{self.cfg.model}:latest" not in names:
            raise OllamaError(f"Model {self.cfg.model} is not available. Pull it with: ollama pull {self.cfg.model}")

    def warm_up(self) -> None:
        """Load the model into memory now (an empty prompt only loads it), so the first question isn't slow."""
        httpx.post(f"{self.cfg.ollama_url}/api/generate",
                   json={"model": self.cfg.model, "keep_alive": self.cfg.keep_alive},
                   timeout=httpx.Timeout(300, connect=5)).raise_for_status()

    def stream(self, system: str, user: str) -> Iterator[str]:
        """Yield the answer piece by piece. Afterwards, last_stats holds Ollama's timing counters."""
        payload = {
            "model": self.cfg.model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "stream": True,
            "keep_alive": self.cfg.keep_alive,
            "options": {
                "temperature": self.cfg.temperature,
                "num_ctx": self.cfg.num_ctx,
                "repeat_penalty": self.cfg.repeat_penalty,
                "num_predict": self.cfg.max_answer_tokens,
            },
        }
        self.last_stats = {}
        with httpx.stream("POST", f"{self.cfg.ollama_url}/api/chat", json=payload,
                          timeout=httpx.Timeout(600, connect=5)) as response:
            if response.status_code != 200:
                raise OllamaError(f"Ollama returned {response.status_code}: {response.read().decode()[:300]}")
            for line in response.iter_lines():
                if not line:
                    continue
                event = json.loads(line)
                if "error" in event:
                    raise OllamaError(event["error"])
                piece = event.get("message", {}).get("content", "")
                if piece:
                    yield piece
                if event.get("done"):
                    self.last_stats = {k: event.get(k) for k in (
                        "prompt_eval_count", "prompt_eval_duration", "eval_count", "eval_duration", "load_duration",
                        "total_duration", "done_reason")}
