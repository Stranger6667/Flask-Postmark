# coding: utf-8
import pytest
from flask import json
from flask_postmark import Postmark


BODY = '<html><body><strong>Hello</strong> dear Postmark user.</body></html>'
SUBJECT = 'Postmark test'
RECEIVER = 'receiver@example.com'
SENDER = 'sender@example.com'
DATA = {
    'From': SENDER,
    'To': RECEIVER,
    'Subject': SUBJECT,
    'HtmlBody': BODY
}


class TestPostmark:

    @pytest.fixture(autouse=True)
    def setup(self, test_client):
        self.client = test_client

    def post(self, url, data=None):
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        return json.loads(response.data)

    def test_token(self, server_token):
        assert self.client.get('/token').data == server_token

    def test_send(self):
        assert self.post('/send', DATA) == {
            'Attachments': [], 'Bcc': None, 'Cc': None, 'From': SENDER,
            'Headers': [], 'HtmlBody': BODY, 'Tag': None,
            'TextBody': None, 'To': RECEIVER, 'TrackLinks': 'None', 'TrackOpens': None,
            'ReplyTo': None, 'Subject': SUBJECT
        }

    def test_send_batch(self):
        data = self.post('/send_batch', [DATA, DATA])
        expected = {
            'Attachments': [], 'From': SENDER, 'Headers': [], 'Subject': SUBJECT, 'HtmlBody': BODY, 'To': RECEIVER
        }
        assert data == [expected, expected]

    def test_empty_app(self, app):
        assert len(app.teardown_appcontext_funcs) == 1
        postmark = Postmark()
        postmark.init_app(app)
        assert len(app.teardown_appcontext_funcs) == 2
