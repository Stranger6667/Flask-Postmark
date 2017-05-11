Flask Postmark
==============

This is a simple integration with `Postmark <https://postmarkapp.com/>`_ for Flask applications.

.. image:: https://travis-ci.org/Stranger6667/Flask-Postmark.png?branch=master
   :target: https://travis-ci.org/Stranger6667/Flask-Postmark


Installation
------------

Installing is simple with pip::

    $ pip install flask-postmark


Usage
-----

To send an email in your Flask application::

.. code-block:: python

    from flask import Flask
    from flask_postmark import Postmark


    app = Flask(__name__)

    app.config['POSTMARK_SERVER_TOKEN'] = '<replace with your server token>'

    postmark = Postmark(app)
