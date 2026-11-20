from typing import Any

from flask import Flask, current_app, g, has_app_context
from postmarker.core import PostmarkClient


class Postmark:
    def __init__(self, app: Flask | None = None) -> None:
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.extensions["postmark"] = self
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception: BaseException | None) -> None:
        client = g.pop("postmark_client", None)
        if client is not None:
            client.session.close()

    @property
    def client(self) -> PostmarkClient:
        if not has_app_context():
            raise RuntimeError("Working outside of application context")
        client: PostmarkClient | None = g.get("postmark_client")
        if client is None:
            client = g.postmark_client = PostmarkClient.from_config(current_app.config, is_uppercase=True)
        return client

    def send(self, *args: Any, **kwargs: Any) -> Any:
        return self.client.emails.send(*args, **kwargs)

    def send_batch(self, *args: Any, **kwargs: Any) -> list[Any]:
        return self.client.emails.send_batch(*args, **kwargs)
