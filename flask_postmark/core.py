# coding: utf-8
from flask import _app_ctx_stack as stack, current_app

from postmarker.core import PostmarkClient


class Postmark(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions['postmark'] = self
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'postmark_client'):
            ctx.postmark_client.session.close()

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'postmark_client'):
                ctx.postmark_client = PostmarkClient.from_config(current_app.config, is_uppercase=True)
            return ctx.postmark_client

    def send(self, *args, **kwargs):
        return self.client.emails.send(*args, **kwargs)

    def send_batch(self, *args, **kwargs):
        return self.client.emails.send_batch(*args, **kwargs)
