Flask Postmark
==============

This is a simple integration with `Postmark <https://postmarkapp.com/>`_ for Flask applications.

.. image:: https://travis-ci.org/Stranger6667/Flask-Postmark.png?branch=master
   :target: https://travis-ci.org/Stranger6667/Flask-Postmark

.. image:: https://codecov.io/github/Stranger6667/Flask-Postmark/coverage.svg?branch=master
   :target: https://codecov.io/github/Stranger6667/Flask-Postmark?branch=master
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/flask-postmark/badge/?version=stable
   :target: http://flask-postmark.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/Flask-Postmark.svg
    :target: https://pypi.python.org/pypi/Flask-Postmark
    :alt: Latest PyPI version

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

    app.config['POSTMARK_SERVER_TOKEN'] = '<replace with your server token>'

    postmark = Postmark(app)

    @app.route('/send', methods=['POST'])
    def send():
        postmark.send(
            From='sender@example.com',
            To='receiver@example.com',
            Subject='Postmark test',
            HtmlBody='<html><body><strong>Hello</strong> dear Postmark user.</body></html>'
        )
        return b'OK'

Documentation
=============

You can view the documentation online at:

- https://flask-postmark.readthedocs.io/en/latest/

Or you can look at the docs/ directory in the repository.
