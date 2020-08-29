Flask Postmark
==============

|Build| |Coverage| |Version| |Python versions| |Docs| |License|

This is a simple integration with `Postmark <https://postmarkapp.com/>`_ for Flask applications.

Installation
------------

Installing is simple with pip::

    $ pip install flask-postmark


Usage
-----

To send an email in your Flask application:

.. code-block:: python

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

Documentation
=============

You can view the documentation online at:

- https://flask-postmark.readthedocs.io/en/latest/

Or you can look at the docs/ directory in the repository.

.. |Build| image:: https://github.com/Stranger6667/flask-postmark/workflows/build/badge.svg
   :target: https://github.com/Stranger6667/flask-postmark/actions
.. |Coverage| image:: https://codecov.io/github/Stranger6667/flask-postmark/coverage.svg?branch=master
    :target: https://codecov.io/github/Stranger6667/flask-postmark?branch=master
.. |Version| image:: https://img.shields.io/pypi/v/flask-postmark.svg
   :target: https://pypi.org/project/flask-postmark/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/flask-postmark.svg
   :target: https://pypi.org/project/flask-postmark/
.. |Docs| image:: https://readthedocs.org/projects/flask-postmark/badge/?version=stable
   :target: https://flask-postmark.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status
.. |License| image:: https://img.shields.io/pypi/l/flask-postmark.svg
   :target: https://opensource.org/licenses/MIT
