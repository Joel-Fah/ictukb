"""Web server tests with a fake assistant: no database, no model. Run: python -m pytest chatbot/tests"""

import http.client
import json
import threading
from http.server import ThreadingHTTPServer

import pytest

from chatbot.chat import Turn
from chatbot.retrieval import Passage, Retrieval
from chatbot.web import make_handler


class FakeAssistant:
    def answer(self, question, out, debug=False):
        p = Passage(doc_id="finance-installments", title="Paying tuition in installments", heading="Can I?",
                    text="...", category="finance", source="content/finance/finance-installments.md",
                    last_verified="2026-11-18", stale=False, status="verified", similarity=0.88)
        out.write("Yes, in three installments ")
        out.write("[finance-installments].\n")
        out.write("\nSources:\n  [finance-installments] Paying tuition in installments\n")
        turn = Turn(question, "en", Retrieval("high", 0.88, 0.81, [p], 0.1), used_llm=True,
                    answer="Yes, in three installments [finance-installments].", context_passages=[p],
                    cited=["finance-installments"], first_token_s=1.0, total_s=2.0)
        return turn


@pytest.fixture()
def server():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(FakeAssistant(), {"model": "fake", "threshold": 0.81,
                                                                              "top_k": 4}))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield srv.server_address[1]
    srv.shutdown()
    srv.server_close()


def request(port, method, path, body=None, headers=None):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    conn.request(method, path, body=body, headers=headers or {})
    res = conn.getresponse()
    return res.status, res.read().decode("utf-8")


def test_page_and_info(server):
    status, html = request(server, "GET", "/")
    assert status == 200 and "<title>ICT University Assistant</title>" in html and "https://" not in html.split("<script>")[0]
    status, info = request(server, "GET", "/api/info")
    assert status == 200 and json.loads(info)["model"] == "fake"


def test_ask_streams_text_then_done(server):
    status, body = request(server, "POST", "/api/ask", json.dumps({"question": "Can I pay in installments?"}),
                           {"Content-Type": "application/json"})
    events = [json.loads(line) for line in body.splitlines()]
    assert status == 200
    assert "".join(e["v"] for e in events if e["t"] == "text").startswith("Yes, in three installments")
    done = events[-1]
    assert done["t"] == "done" and done["turn"]["cited"][0]["id"] == "finance-installments"
    assert done["turn"]["passages"][0]["used"] is True and "text" not in done["turn"]["passages"][0]


@pytest.mark.parametrize("body,headers,expected", [
    (json.dumps({"question": "x"}), {"Content-Type": "text/plain"}, 415),  # cross-site forms can't send JSON
    (json.dumps({"question": ""}), {"Content-Type": "application/json"}, 400),
    (json.dumps({"question": "x" * 501}), {"Content-Type": "application/json"}, 400),
    ("not json", {"Content-Type": "application/json"}, 400),
])
def test_ask_rejects_bad_requests(server, body, headers, expected):
    status, _ = request(server, "POST", "/api/ask", body, headers)
    assert status == expected


def test_other_host_names_are_refused(server):
    # A site resolving its own name to 127.0.0.1 (DNS rebinding) must not reach the API.
    status, _ = request(server, "GET", "/", headers={"Host": "evil.example:8765"})
    assert status == 403
    status, _ = request(server, "POST", "/api/ask", json.dumps({"question": "x"}),
                        {"Content-Type": "application/json", "Host": "evil.example"})
    assert status == 403
