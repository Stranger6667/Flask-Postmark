# coding: utf-8
import pytest
from flask import Flask, json, request

from flask_postmark import Postmark


@pytest.fixture
def app(server_token, postmark_request):
    app = Flask(__name__)
    app.config["POSTMARK_SERVER_TOKEN"] = server_token
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
    postmark = Postmark(app)

    def make_response():
        return json.dumps(postmark_request.mock_calls[0][2]["json"])

    @app.route("/token", methods=["GET"])
    def token():
        return postmark.client.server_token

    @app.route("/send", methods=["POST"])
    def send():
        data = request.get_json()
        postmark.send(**data)
        return make_response()

    @app.route("/is_same_client", methods=["POST"])
    def is_same_client():
        return json.dumps(postmark.client is postmark.client)

    @app.route("/send_batch", methods=["POST"])
    def send_batch():
        data = request.get_json()
        postmark.send_batch(*data)
        return make_response()

    return app


@pytest.fixture
def server_token():
    return b"Foo"


@pytest.fixture
def test_client(app):
    return app.test_client()


@pytest.fixture
def post(test_client):
    def inner(url, data=None):
        response = test_client.post(
            url, data=json.dumps(data), content_type="application/json"
        )
        return json.loads(response.data)

    return inner
