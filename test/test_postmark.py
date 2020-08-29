# coding: utf-8
import pytest

from flask_postmark import Postmark


BODY = "<html><body><strong>Hello</strong> dear Postmark user.</body></html>"
SUBJECT = "Postmark test"
RECEIVER = "receiver@example.com"
SENDER = "sender@example.com"
DATA = {"From": SENDER, "To": RECEIVER, "Subject": SUBJECT, "HtmlBody": BODY}


def test_token(test_client, server_token):
    assert test_client.get("/token").data == server_token


def test_send(post):
    assert post("/send", DATA) == {
        "Attachments": [],
        "Bcc": None,
        "Cc": None,
        "From": SENDER,
        "Headers": [],
        "HtmlBody": BODY,
        "Metadata": None,
        "Tag": None,
        "TextBody": None,
        "To": RECEIVER,
        "TrackLinks": "None",
        "TrackOpens": None,
        "ReplyTo": None,
        "Subject": SUBJECT,
    }


def test_send_batch(post):
    data = post("/send_batch", [DATA, DATA])
    expected = {
        "Attachments": [],
        "From": SENDER,
        "Headers": [],
        "Subject": SUBJECT,
        "HtmlBody": BODY,
        "To": RECEIVER,
    }
    assert data == [expected, expected]


def test_is_same_client(post):
    assert post("/is_same_client", DATA) is True


def test_empty_app(app):
    assert len(app.teardown_appcontext_funcs) == 1
    postmark = Postmark()
    postmark.init_app(app)
    assert len(app.teardown_appcontext_funcs) == 2


def test_get_app(app):
    postmark = Postmark(app)
    assert postmark._get_app() is app


def test_no_context(app):
    postmark = Postmark(app)
    with pytest.raises(RuntimeError):
        postmark.client


def test_teardown(app):
    postmark = Postmark(app)
    assert postmark.teardown(None) is None
