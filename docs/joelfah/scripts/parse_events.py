"""Reads the newline-delimited JSON events of POST /api/ask from stdin and prints a short summary (offline_test.sh)."""
import json, sys
ev = [json.loads(line) for line in sys.stdin if line.strip()]
texts = [e for e in ev if e["t"] == "text"]
print("events:", " ".join(e["t"] for e in ev if e["t"] != "text"), f"(+{len(texts)} text pieces)")
print("answer:", "".join(e["v"] for e in texts).strip())
turn = ev[-1].get("turn", {}) if ev else {}
print("status:", turn.get("status"), "| sources:", [s["id"] for s in turn.get("sources", [])],
      "| total:", turn.get("metrics", {}).get("total_s"), "s")
