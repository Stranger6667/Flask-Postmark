from typing import Any, List, Optional

from flask import Flask
from flask import _app_ctx_stack as stack  # type: ignore
from flask import current_app
from postmarker.core import PostmarkClient


class Postmark:
    app = None

    def __init__(self, app: Optional[Flask] = None) -> None:
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.extensions["postmark"] = self
        app.teardown_appcontext(self.teardown)

    def _get_app(self) -> Flask:
        if not current_app and self.app:
            return self.app
        return current_app

    def teardown(self, exception: Any) -> None:
        ctx = stack.top
        if hasattr(ctx, "postmark_client"):
            ctx.postmark_client.session.close()

    @property
    def client(self) -> PostmarkClient:
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, "postmark_client"):
                app = self._get_app()
                ctx.postmark_client = PostmarkClient.from_config(app.config, is_uppercase=True)
            return ctx.postmark_client
        raise RuntimeError("Context stack is empty")

    def send(self, *args: Any, **kwargs: Any) -> Any:
        return self.client.emails.send(*args, **kwargs)

    def send_batch(self, *args: Any, **kwargs: Any) -> List:
        return self.client.emails.send_batch(*args, **kwargs)
