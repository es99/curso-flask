from loja.modelos import Categoria, Produto

cadeira = Produto('Cadeira', categoria=Categoria('Moveis'))
teclado = Produto('Teclado', categoria=Categoria('Eletronicos'))

print(cadeira.nome, cadeira.categoria)
print(teclado.nome, teclado.categoria)