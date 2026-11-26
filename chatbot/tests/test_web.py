"""Web server tests with a fake assistant: no database, no model. Run: python -m pytest chatbot/tests"""

import http.client
import json
import threading
import time
from http.server import ThreadingHTTPServer

import pytest

from chatbot.chat import Turn
from chatbot.retrieval import Passage, Retrieval
from chatbot.web import behaviour, make_handler

PASSAGE = Passage(doc_id="finance-installments", title="Paying tuition in installments", heading="Can I?", text="...",
                  category="finance", source="content/finance/finance-installments.md", last_verified="2026-11-18",
                  stale=False, status="verified", similarity=0.88)


def make_turn(**kw) -> Turn:
    base = dict(question="q", language="en", retrieval=Retrieval("high", 0.88, 0.81, [PASSAGE], 0.1), used_llm=True,
                answer="Yes, in three installments [finance-installments].", context_passages=[PASSAGE],
                cited=["finance-installments"], sources_shown=["finance-installments"], first_token_s=1.0, total_s=2.0,
                stats={"eval_count": 20, "eval_duration": 4_000_000_000})
    base.update(kw)
    return Turn(**base)


class FakeAssistant:
    def answer(self, question, out, debug=False, footer=None, on_retrieval=None):
        turn = make_turn(question=question)
        if on_retrieval:
            on_retrieval(turn)
        out.write("Yes, in three installments ")
        out.write("[finance-installments].\n")
        print("\nSources:\n  [finance-installments] Paying tuition in installments", file=footer or out)
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
    assert status == 200 and "<title>ICT University Assistant</title>" in html
    assert 'href="http' not in html and 'src="http' not in html  # nothing loaded from the internet
    status, info = request(server, "GET", "/api/info")
    assert status == 200 and json.loads(info)["model"] == "fake"


def test_ask_streams_retrieval_text_then_structured_done(server):
    status, body = request(server, "POST", "/api/ask", json.dumps({"question": "Can I pay in installments?"}),
                           {"Content-Type": "application/json"})
    events = [json.loads(line) for line in body.splitlines()]
    assert status == 200
    assert events[0]["t"] == "retrieval" and events[0]["passages"] == 1 and events[0]["fallback"] == ""
    text = "".join(e["v"] for e in events if e["t"] == "text")
    assert text.startswith("Yes, in three installments") and "Sources:" not in text  # footer is not streamed
    turn = events[-1]["turn"]
    assert events[-1]["t"] == "done" and turn["status"] == "grounded" and turn["reasons"] == []
    assert turn["sources"][0]["url"].endswith("content/finance/finance-installments.md") and turn["sources"][0]["cited"]
    assert turn["metrics"]["answer_tok_s"] == 5.0 and turn["metrics"]["retrieval_ms"] == 100
    assert "text" not in turn["passages"][0]


def test_behaviour_states():
    assert behaviour(make_turn())[0] == "grounded"
    status, reasons = behaviour(make_turn(unverified=["december"], redacted=["x@y.z"]))
    assert status == "check" and any("december" in r for r in reasons) and any("removed" in r for r in reasons)
    assert behaviour(make_turn(cited=[], sources_shown=["finance-installments"]))[0] == "check"
    draft = Passage(**{**PASSAGE.__dict__, "status": "draft"})
    assert behaviour(make_turn(context_passages=[draft]))[0] == "check"
    assert behaviour(make_turn(fallback="threshold", used_llm=False))[0] == "not_found"
    assert behaviour(make_turn(fallback="placeholders", used_llm=False))[0] == "not_found"
    assert behaviour(make_turn(answer="I do not have that information.", cited=[]))[0] == "not_found"
    # Seen live: a refusal that also invented an address; the removal must still be reported.
    status, reasons = behaviour(make_turn(answer="I do not have that information.", redacted=["finance@x.cm"]))
    assert status == "not_found" and any("removed" in r for r in reasons)
    # Failure 36 (seen with qwen2.5:7b): a full answer that notes one missing detail is an answer to check, not "not found".
    gap = ("Tuition is paid in three installments: 50%, 30% and 20% of the tuition, that is XAF 182,500, XAF 109,500 and "
           "XAF 73,000 [finance-installments]. The second installment is paid from 20 to 30 November 2026. The dates of "
           "the first and third installments are not provided in the sources.")
    status, reasons = behaviour(make_turn(answer=gap))
    assert status == "check" and any("some details are not in the sources" in r for r in reasons)


def test_second_question_is_told_it_is_queued():
    release = threading.Event()

    class SlowAssistant(FakeAssistant):
        def answer(self, question, out, **kw):
            if question == "first":
                release.wait(5)
            return super().answer(question, out, **kw)

    srv = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(SlowAssistant(), {}))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    port = srv.server_address[1]
    body = lambda q: json.dumps({"question": q})  # noqa: E731
    hdr = {"Content-Type": "application/json"}
    first = threading.Thread(target=request, args=(port, "POST", "/api/ask", body("first"), hdr))
    first.start()
    time.sleep(0.3)  # let the first question take the lock
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    conn.request("POST", "/api/ask", body=body("second"), headers=hdr)
    res = conn.getresponse()
    assert json.loads(res.readline())["t"] == "queued"
    release.set()
    events = [json.loads(line) for line in res.read().decode().splitlines()]
    assert events[-1]["t"] == "done"
    first.join(5)
    srv.shutdown()
    srv.server_close()


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
