# coding: utf-8
from flask import _app_ctx_stack as stack, current_app

from postmarker._compat import get_args
from postmarker.core import PostmarkClient


class Postmark(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)

    def get_postmark_client(self):
        kwargs = dict(
            (arg, current_app.config[('POSTMARK_' + arg).upper()])
            for arg in get_args(PostmarkClient)
            if ('POSTMARK_' + arg).upper() in current_app.config
        )
        return PostmarkClient(**kwargs)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'postmark_client'):
            ctx.postmark_client.session.close()

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'postmark_client'):
                ctx.postmark_client = self.get_postmark_client()
            return ctx.postmark_client

    def send(self, *args, **kwargs):
        return self.client.emails.send(*args, **kwargs)

    def send_batch(self, *args, **kwargs):
        return self.client.emails.send_batch(*args, **kwargs)
