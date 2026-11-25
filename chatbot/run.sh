#!/usr/bin/env bash
# Start the local ICT University assistant (after ./chatbot/setup.sh).
#
#   ./chatbot/run.sh                    terminal chat
#   ./chatbot/run.sh --web [--port N]   web page on http://127.0.0.1:8765 (local only)
#   ./chatbot/run.sh "question" ...     answer and exit
set -euo pipefail
cd "$(dirname "$0")/.."

[ -d .venv ] && [ -f .env ] || { echo "Not set up yet: run ./chatbot/setup.sh first." >&2; exit 1; }
# shellcheck disable=SC1091
. .venv/bin/activate
export FASTEMBED_CACHE_PATH="${FASTEMBED_CACHE_PATH:-$HOME/.cache/fastembed}"
export ADMIN_TOKEN="${ADMIN_TOKEN:-}"
COMPOSE=(docker compose -f docker/docker-compose.yml)

if ! "${COMPOSE[@]}" exec -T db pg_isready -U ictkb -q 2>/dev/null; then
  echo "starting the database …" >&2
  "${COMPOSE[@]}" up -d db >/dev/null 2>&1 || { echo "error: could not start the database (is Docker usable? see setup.sh)" >&2; exit 1; }
  for _ in $(seq 1 30); do "${COMPOSE[@]}" exec -T db pg_isready -U ictkb -q 2>/dev/null && break; sleep 2; done
fi
curl -fsS http://127.0.0.1:11434/api/tags >/dev/null 2>&1 || { echo "error: Ollama is not running. Run: sudo systemctl start ollama" >&2; exit 1; }

if [ "${1:-}" = "--web" ]; then
  shift
  exec python -m chatbot.web "$@"
fi
exec python -m chatbot.chat "$@"
