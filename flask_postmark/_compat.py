# coding: utf-8
try:
    from flask import _app_ctx_stack as stack  # noqa
except ImportError:
    from flask import _request_ctx_stack as stack  # noqa
