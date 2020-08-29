.. Flask-Postmark documentation master file, created by
   sphinx-quickstart on Mon May 15 14:27:50 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-Postmark's documentation!
==========================================

This is a simple integration with `Postmark <https://postmarkapp.com/>`_ for Flask applications.

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
            HtmlBody="""
                <html>
                <body>
                <strong>Hello</strong> dear Postmark user.
                </body>
                </html>""",
        )
        return b"OK"

.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
