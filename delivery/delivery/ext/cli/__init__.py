import click
from delivery.ext.db import db

def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()


    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuarios")
