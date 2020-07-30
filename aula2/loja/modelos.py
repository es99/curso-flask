class Categoria:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

    def __repr__(self):
        return f"{self.nome} - {self.categoria}"