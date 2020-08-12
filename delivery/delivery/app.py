from flask import Flask, render_template, request
from delivery.ext import site
from delivery.ext import config
from delivery.ext import toolbar
from delivery.ext import db
from delivery.ext import cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app

if __name__ == "__main__":
    pass