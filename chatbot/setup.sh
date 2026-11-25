#!/usr/bin/env bash
# One-time setup of the local ICT University assistant. Safe to run again: every step skips what is already done.
#
#   ./chatbot/setup.sh            set up everything (first run downloads about 4 GB: e5 2.2 GB, qwen2.5:3b 1.9 GB)
#   ./chatbot/setup.sh --crawl    also (re)read the university website into the index (needs the network)
#
# It never uses sudo and never overwrites an existing .env. System installs (Docker, Ollama) are left to you, with
# the exact command printed when something is missing.
set -euo pipefail
cd "$(dirname "$0")/.."

MODEL="${CHAT_MODEL:-qwen2.5:3b}"
export FASTEMBED_CACHE_PATH="${FASTEMBED_CACHE_PATH:-$HOME/.cache/fastembed}"  # fastembed's default is /tmp (wiped at boot)
export ADMIN_TOKEN="${ADMIN_TOKEN:-}"  # silences docker compose's warning about the whatsapp service's variable
COMPOSE=(docker compose -f docker/docker-compose.yml)
CRAWL=0
for arg in "$@"; do
  case "$arg" in
    --crawl) CRAWL=1 ;;
    -h|--help) sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $arg (see --help)" >&2; exit 2 ;;
  esac
done

step() { printf '\n\033[1m== %s\033[0m\n' "$1"; }
fail() { printf '\033[31merror:\033[0m %s\n' "$1" >&2; exit 1; }

step "1/7 Checking prerequisites"
python3 -c 'import sys; sys.exit(sys.version_info < (3, 11))' || fail "Python 3.11 or newer is needed (found $(python3 --version))."
command -v docker >/dev/null || fail "Docker is not installed. See https://docs.docker.com/engine/install/"
if ! docker info >/dev/null 2>&1; then
  if docker context show 2>/dev/null | grep -q desktop; then
    fail "Docker points at Docker Desktop, which isn't running. Use the system engine: docker context use default"
  fi
  fail "Docker is installed but not usable by $USER. Run: sudo usermod -aG docker $USER, then log out and back in."
fi
command -v ollama >/dev/null || fail "Ollama is not installed. Run: curl -fsSL https://ollama.com/install.sh | sh"
curl -fsS http://127.0.0.1:11434/api/tags >/dev/null || fail "Ollama is not running. Run: sudo systemctl enable --now ollama"
echo "Python $(python3 -c 'import platform; print(platform.python_version())'), $(docker --version), ollama $(ollama --version 2>/dev/null | awk '{print $NF}')"

step "2/7 Python environment (.venv)"
[ -d .venv ] || python3 -m venv .venv
# shellcheck disable=SC1091
. .venv/bin/activate
PIP_LOG=.venv/setup-pip.log
{ pip install -q --upgrade pip && pip install -q -e ".[dev,local-embeddings]"; } >"$PIP_LOG" 2>&1 \
  || { tail -20 "$PIP_LOG" >&2; fail "pip install failed (full log: $PIP_LOG)"; }   # the repo's own extras only
echo "installed: $(pip show fastembed 2>/dev/null | awk '/^Version/{print "fastembed " $2}')"

step "3/7 Configuration (.env)"
if [ -f .env ]; then
  provider=$(grep -E '^EMBEDDING_PROVIDER=' .env | tail -1 | cut -d= -f2)
  [ "$provider" = "fastembed" ] || fail ".env exists with EMBEDDING_PROVIDER=${provider:-<unset>}. The local assistant needs EMBEDDING_PROVIDER=fastembed (compare with chatbot/env.template). Not changed."
  echo ".env already exists and uses fastembed: kept as is."
else
  cp chatbot/env.template .env
  echo "created .env from chatbot/env.template"
fi

step "4/7 Database (PostgreSQL + pgvector in Docker)"
"${COMPOSE[@]}" up -d db
for _ in $(seq 1 30); do
  "${COMPOSE[@]}" exec -T db pg_isready -U ictkb -q && break
  sleep 2
done
"${COMPOSE[@]}" exec -T db pg_isready -U ictkb -q || fail "the database did not become ready; see: ${COMPOSE[*]} logs db"
ictkb migrate

step "5/7 Knowledge base index (first run downloads the e5 model, about 2.2 GB, into $FASTEMBED_CACHE_PATH)"
ictkb validate
ictkb index
if [ "$CRAWL" = 1 ]; then
  ictkb crawl
else
  echo "(website pages not re-read; add --crawl to include them)"
fi

step "6/7 Chat model ($MODEL)"
if ollama list | awk 'NR>1{print $1}' | grep -qx "$MODEL"; then
  echo "$MODEL already pulled"
else
  ollama pull "$MODEL"
fi

step "7/7 Self-test"
python -m pytest -q chatbot/tests
ictkb search "How do I register for courses?" --top-k 3

printf '\n\033[1mDone.\033[0m Start the assistant with:\n  ./chatbot/run.sh          (terminal)\n  ./chatbot/run.sh --web    (browser, http://127.0.0.1:8765)\n'
