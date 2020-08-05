import views
from flask import Flask


def create_app():
    """"Função principal que retorna um aplicativo"""
    app = Flask(__name__)
    views.init_app(app)
    return app
