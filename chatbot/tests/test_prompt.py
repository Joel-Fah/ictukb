"""Unit tests for the parts of the chatbot that need neither the database nor the model.

Run from the repository root: python -m pytest chatbot/tests
"""

from chatbot.prompt import (
    MISSING,
    build_context,
    cited_ids,
    detect_language,
    fallback_message,
    source_notes,
    truncate,
)
from chatbot.retrieval import Passage, body_of


def passage(doc_id: str, text: str = "Some text.", status: str = "verified", stale: bool = False) -> Passage:
    return Passage(doc_id=doc_id, title=f"Title {doc_id}", heading="How?", text=text, category="finance",
                   source=f"content/finance/{doc_id}.md", last_verified="2026-11-18", stale=stale, status=status,
                   similarity=0.85)


def test_detect_language():
    assert detect_language("How do I register for courses?") == "en"
    assert detect_language("Comment payer les frais de scolarité ?") == "fr"
    assert detect_language("Quels sont les programmes de master ?") == "fr"
    assert detect_language("What is the application fee?") == "en"


def test_truncate_cuts_at_a_word():
    assert truncate("short", 10) == "short"
    out = truncate("one two three four five", 12)
    assert out.endswith(" …") and len(out) <= 14 and "thr" not in out


def test_context_replaces_placeholder_and_respects_limits():
    ps = [passage("a", "Fee is [[TO FILL]] FCFA."), passage("b", "x " * 2000), passage("c")]
    context, used = build_context(ps, max_chunk_chars=300, max_context_chars=600)
    assert "[[TO FILL]]" not in context and MISSING in context
    assert [p.doc_id for p in used] == ["a", "b"]  # blocks of about 135 + 400 chars; c (about 110) no longer fits
    assert len(context) <= 600


def test_first_passage_always_kept():
    context, used = build_context([passage("a", "y " * 5000)], max_chunk_chars=5000, max_context_chars=100)
    assert len(used) == 1


def test_draft_status_is_visible_to_the_model():
    context, _ = build_context([passage("a", status="draft")], 500, 2000)
    assert 'status="draft, not yet verified"' in context


def test_cited_ids_only_known_and_in_order():
    ps = [passage("finance-fee-schedule"), passage("erp-fee-statement")]
    answer = "Pay at the bank [erp-fee-statement]. Fees are listed [finance-fee-schedule, erp-fee-statement] [made-up]."
    assert cited_ids(answer, ps) == ["erp-fee-statement", "finance-fee-schedule"]
    assert cited_ids("No citation here.", ps) == []


def test_fallback_uses_contacts_from_the_document():
    contacts = {
        "What are the general phone number and email address?": "General: admin@example.edu.",
        "How do I contact the admissions office?": "Admissions: admissions@example.edu.",
        "What is the official postal address of the university?": "P.O. Box 1.",
    }
    en = fallback_message("en", contacts, {"finance"})
    assert "admin@example.edu" in en and "admissions@" not in en and "P.O. Box" not in en
    fr = fallback_message("fr", contacts, {"admissions"})
    assert fr.startswith("Je n'ai pas") and "admissions@example.edu" in fr
    assert "not in the index" in fallback_message("en", {}, set())


def test_source_notes_for_draft_and_stale():
    ps = [passage("a", status="draft"), passage("b", stale=True), passage("c")]
    notes = source_notes("en", ps, ["a", "b", "c"])
    assert len(notes) == 2 and "draft" in notes[0] and "2026-11-18" in notes[1]


def test_body_of_drops_the_title_line():
    assert body_of("Title | How?\n\nThe answer.") == "The answer."
    assert body_of("only one line") == "only one line"


def test_links_and_images_are_reduced_to_text():
    from chatbot.prompt import clean

    raw = "Docs below. [SEE OUR PROGRAMS](https://ictuniversity.org/x/) ![logo](https://x/y.png) [[TO FILL]] FCFA"
    out = clean(raw)
    assert out == f"Docs below. SEE OUR PROGRAMS  {MISSING} FCFA"
    assert "[finance-fee-schedule]" in clean("see [finance-fee-schedule]")  # citations are not links: untouched


def test_relative_cutoff_drops_weak_passages():
    strong, weak = passage("a"), passage("b")
    strong.similarity, weak.similarity = 0.88, 0.82
    _, used = build_context([strong, weak], 1000, 5000, relative_cutoff=0.05)
    assert [p.doc_id for p in used] == ["a"]
    _, used = build_context([strong, weak], 1000, 5000)  # default: no cutoff
    assert len(used) == 2


def test_loop_detection():
    from chatbot.llm import is_looping

    line = "- Les programmes sont dispensés en anglais ou français.\n"
    assert is_looping("Intro\n" + line * 3)
    assert not is_looping("Intro\n" + line * 2)
    assert not is_looping("1. a\n2. b\n3. c\n")
    assert not is_looping(line * 2 + line.strip())  # third copy unfinished: not yet


# Context and answers below are taken from acceptance run 2 (docs/joelfah/reports/phase2-acceptance-run2.txt).
INSTALLMENTS_CONTEXT = (
    "Yes. Tuition is paid in three installments: the first installment is 50% of the tuition, the second 30% and the "
    "third 20%. With a complete tuition of XAF 365,000 this is XAF 182,500, then XAF 109,500, then XAF 73,000. "
    "... (fees control resumed on Monday 9 November 2026), and that the payment period for the second installment is "
    "20 to 30 November 2026."
)


def test_invented_date_is_flagged():
    from chatbot.prompt import unverified_facts

    answer = ("- First installment of XAF 182,500 (50% of total tuition)\n- Second installment of XAF 109,500\n"
              "The payment period for the second installment is from November 20th to December 3rd [finance-installments].")
    assert unverified_facts(answer, INSTALLMENTS_CONTEXT) == ["3", "december"]


def test_correct_french_answer_is_not_flagged():
    from chatbot.prompt import unverified_facts

    answer = ("1. Le premier versement est 50% du total des frais, soit XAF 182 500.\n"
              "2. Le deuxième versement est de 30%, soit XAF 109.500.\n"
              "Le deuxième versement est dû entre les 20 et 30 novembre 2026 (lundi 9 novembre 2026).")
    assert unverified_facts(answer, INSTALLMENTS_CONTEXT) == []


def test_numbers_from_doc_ids_question_and_list_markers_are_ignored():
    from chatbot.prompt import unverified_facts

    answer = "1. See [web-academic-calendar-2026-2027].\n2. It may change in Year 4."
    assert unverified_facts(answer, "calendar text", question="What happens in Year 4?") == []


def test_garbled_citation_still_counts():
    ps = [passage("finance-installments"), passage("finance-scholarships")]
    assert cited_ids('[Venteurs "finance-installments"]', ps) == ["finance-installments"]
    assert cited_ids("see finance-installments-extra", ps) == []  # a longer id is not a mention


def test_invented_email_is_flagged_but_copied_one_is_not():
    from chatbot.prompt import unverified_facts

    context = "The Admissions Office email is admissions@ictuniversity.edu.cm. Apply at https://studentportal.example/."
    answer = ("I do not have that information. You can contact the Finance office at finance@ictuniversity.edu.cm "
              "[finance-fee-schedule].")  # run 3, Q9: the address exists nowhere in the knowledge base
    assert unverified_facts(answer, context) == ["finance@ictuniversity.edu.cm"]
    assert unverified_facts("Write to admissions@ictuniversity.edu.cm.", context) == []
    assert unverified_facts("Go to https://other.example/apply", context) == ["https://other.example/apply"]


def test_refusal_detection():
    from chatbot.prompt import is_refusal

    assert is_refusal("I do not have that information. Please contact the Finance office.")
    assert is_refusal("According to the sources provided, there is no specific information about the opening times.")
    assert is_refusal("Je n'ai pas cette information dans la base.")
    assert not is_refusal("Le deuxième versement est dû entre le 20 et le 30 novembre 2026.")
    assert not is_refusal("Yes, you can pay your fees in installments.")


def test_french_message_keeps_names_in_english():
    from chatbot.prompt import build_user_message

    assert "do not translate" in build_user_message("Quels masters ?", "ctx", "fr")
    assert "do not translate" not in build_user_message("Which masters?", "ctx", "en")


def test_redactor_removes_invented_email_even_when_split_across_pieces():
    from chatbot.prompt import REMOVED, ContactRedactor

    r = ContactRedactor("Write to admissions@ictuniversity.edu.cm.", "en")
    pieces = ["Contact the Finance office at fin", "ance@ictuni", "versity.edu.cm to ", "find out. Or admissions@",
              "ictuniversity.edu.cm."]
    shown = "".join(r.feed(p) for p in pieces) + r.flush()
    assert "finance@" not in shown and REMOVED["en"] + " to find out." in shown
    assert "admissions@ictuniversity.edu.cm." in shown
    assert r.removed == ["finance@ictuniversity.edu.cm"]


def test_redactor_holds_back_only_the_current_word():
    from chatbot.prompt import ContactRedactor

    r = ContactRedactor("", "en")
    assert r.feed("Yes, you can pay in") == "Yes, you can pay "
    assert r.feed("stallments.") == ""
    assert r.flush() == "installments."
