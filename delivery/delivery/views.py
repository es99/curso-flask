from flask import Flask

def init_app(app: Flask):

    @app.route('/')
    def index():
        return "Criando minha primeira rota, parabéns!!!"