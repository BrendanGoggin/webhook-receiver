#!/usr/bin/env python3

import json
import logging

import web
from wsgilog import WsgiLog

urls = ("/.*", "hooks")


class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(self, application, tostream=True, toprint=True)


app = web.application(urls, globals())


def log_webhook(method: str) -> str:
    """Log all relevent webhook info."""
    logger = logging.getLogger(__name__)
    METHODS_WHERE_DATA_IS_IN_INPUT = [
        "GET",
    ]
    if method in METHODS_WHERE_DATA_IS_IN_INPUT:
        formatted_data = web.input()
    else:
        formatted_data = web.data()
    if isinstance(formatted_data, bytes):
        try:
            formatted_data = formatted_data.decode("utf-8")
        except UnicodeDecodeError:
            pass
    try:
        formatted_data = json.dumps(formatted_data, indent=2)
    except (UnicodeDecodeError, TypeError):
        pass
    webhook_received_msg = (
        f"WEBHOOK RECEIVED: HTTP {method.upper()} {web.url()} data={formatted_data}"
    )
    logger.info(webhook_received_msg)
    print(f"print: {webhook_received_msg}")
    return webhook_received_msg


class hooks:
    def CONNECT(self):
        return log_webhook(method="CONNECT")

    def GET(self):
        return log_webhook(method="GET")

    def DELETE(self):
        return log_webhook(method="DELETE")

    def HEAD(self):
        return log_webhook(method="HEAD")

    def OPTIONS(self):
        return log_webhook(method="OPTIONS")

    def PATCH(self):
        return log_webhook(method="PATCH")

    def PUT(self):
        return log_webhook(method="PUT")

    def POST(self):
        return log_webhook(method="POST")

    def TRACE(self):
        return log_webhook(method="TRACE")


if __name__ == "__main__":
    app.run(Log)
