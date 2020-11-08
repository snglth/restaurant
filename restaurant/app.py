import os

from flask import Flask


def make_app():
    app = Flask(__name__)
    app.jinja_env.globals["CAFE_NAME"] = os.environ["CAFE_NAME"]
    return app


app = make_app()
