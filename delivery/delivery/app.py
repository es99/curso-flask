from flask import Flask, render_template, request
from delivery.ext import site
from delivery.ext import config
from delivery.ext import toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app

if __name__ == "__main__":
    pass