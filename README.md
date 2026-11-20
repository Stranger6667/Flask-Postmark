# Flask-Postmark

[![Build](https://github.com/Stranger6667/Flask-Postmark/actions/workflows/build.yml/badge.svg)](https://github.com/Stranger6667/Flask-Postmark/actions/workflows/build.yml)
[![Coverage](https://codecov.io/github/Stranger6667/Flask-Postmark/coverage.svg?branch=master)](https://codecov.io/github/Stranger6667/Flask-Postmark?branch=master)
[![Version](https://img.shields.io/pypi/v/flask-postmark.svg)](https://pypi.org/project/flask-postmark/)
[![Python versions](https://img.shields.io/pypi/pyversions/flask-postmark.svg)](https://pypi.org/project/flask-postmark/)
[![License](https://img.shields.io/pypi/l/flask-postmark.svg)](https://opensource.org/licenses/MIT)

[Postmark](https://postmarkapp.com/) integration for Flask, built on [Postmarker](https://github.com/Stranger6667/postmarker).

## Installation

```
pip install flask-postmark
```

## Usage

```python
from flask import Flask
from flask_postmark import Postmark

app = Flask(__name__)
app.config["POSTMARK_SERVER_TOKEN"] = "<replace with your server token>"

postmark = Postmark(app)


@app.route("/send", methods=["POST"])
def send():
    postmark.send(
        From="sender@example.com",
        To="receiver@example.com",
        Subject="Postmark test",
        HtmlBody="<html><body><strong>Hello</strong> dear Postmark user.</body></html>",
    )
    return b"OK"
```

With the application factory pattern, create the extension once and bind it later with `postmark.init_app(app)`.

`postmark.send` and `postmark.send_batch` wrap `client.emails.send` and `client.emails.send_batch`.
For the rest of the Postmark API, use `postmark.client`: a `postmarker.core.PostmarkClient` created once per application context and closed when the context ends.
Using it outside an application context raises `RuntimeError`.

## Configuration

Each `POSTMARK_*` key in `app.config` is passed to the matching `PostmarkClient` argument:

| Key | `PostmarkClient` argument |
|---|---|
| `POSTMARK_SERVER_TOKEN` | `server_token` |
| `POSTMARK_ACCOUNT_TOKEN` | `account_token` |
| `POSTMARK_VERBOSITY` | `verbosity` |
| `POSTMARK_MAX_RETRIES` | `max_retries` |
| `POSTMARK_TIMEOUT` | `timeout` |
| `POSTMARK_LOGS_STREAM` | `logs_stream` |
| `POSTMARK_ROOT_API_URL` | `root_api_url` |
| `POSTMARK_INLINE_CSS` | `inline_css` (needs the `postmarker[css-inline]` extra) |

At least one of `POSTMARK_SERVER_TOKEN` and `POSTMARK_ACCOUNT_TOKEN` is required.
See the [Postmarker documentation](https://postmarker.readthedocs.io/en/stable/) for what each argument does.
