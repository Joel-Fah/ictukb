#!/bin/bash
# Offline acceptance test: Wi-Fi off, then search, chatbot and web page must still work. Wi-Fi is always
# switched back on (trap), even if a step fails or times out.
# Usage (from anywhere): bash docs/joelfah/scripts/offline_test.sh   (needs the database up; uses ~2 GB RAM, ~2 min)
# Do NOT use "nmcli networking off": it also takes down the Docker bridge network (failure 37).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE/../../.." || exit 1
. .venv/bin/activate
export FASTEMBED_CACHE_PATH=$HOME/.cache/fastembed
LOG=chatbot/reports/offline-test.log
WEB=""

restore() {
  [ -n "$WEB" ] && kill "$WEB" 2>/dev/null
  nmcli radio wifi on; for i in $(seq 30); do ip route | grep -q default && break; sleep 1; done
  echo "[$(date +%T)] Wi-Fi back on: $(nmcli radio wifi), $(ip route | grep -c default) default route(s)"
}
trap restore EXIT
exec > >(tee "$LOG") 2>&1

echo "# Offline test, $(date)"
nmcli radio wifi off
sleep 3
echo "[$(date +%T)] Wi-Fi: $(nmcli radio wifi)"

echo; echo "## 0. Proof that there is no network"
ip -4 -br addr | grep -E "^(wlp|enp|br-)"
ip route | grep -q default && ip route | grep default || echo "no default route"
curl -s -m 5 -o /dev/null https://github.com && echo "HTTPS TO GITHUB WORKS: NOT OFFLINE" || echo "https://github.com unreachable (expected)"
curl -s -m 5 -o /dev/null https://1.1.1.1 && echo "HTTPS TO 1.1.1.1 WORKS: NOT OFFLINE" || echo "https://1.1.1.1 unreachable (expected)"
curl -s -m 5 -o /dev/null https://huggingface.co && echo "HUGGING FACE REACHABLE: NOT OFFLINE" || echo "https://huggingface.co unreachable (expected)"

echo; echo "## 1. Knowledge-base search (ictkb search: e5 embeddings + PostgreSQL)"
start=$(date +%s)
timeout 120 ictkb search "How do I register for courses?" 2>&1 | head -12
echo "exit ${PIPESTATUS[0]}, $(( $(date +%s) - start )) s"

echo; echo "## 2. Chatbot: two golden questions with qwen2.5:3b (one answerable, one off-topic)"
start=$(date +%s)
timeout 220 python -u -m chatbot.eval_generation --label offline --ids PRC-02 NEG-01
echo "exit $?, $(( $(date +%s) - start )) s"

echo; echo "## 3. Web page: one question through POST /api/ask"
python -m chatbot.web --port 8766 > /dev/null 2>&1 &
WEB=$!
for i in $(seq 60); do curl -s -m 2 http://127.0.0.1:8766/api/info > /dev/null && break; sleep 1; done
start=$(date +%s)
timeout 120 curl -s -N -H 'Content-Type: application/json' -d '{"question":"How do I reset my ERP password?"}' \
  http://127.0.0.1:8766/api/ask | python3 -I "$HERE/parse_events.py"
echo "$(( $(date +%s) - start )) s"
kill "$WEB" 2>/dev/null; WEB=""
echo; echo "[$(date +%T)] all steps done; switching Wi-Fi back on"
