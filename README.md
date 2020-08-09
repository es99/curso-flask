# curso-flask
Repositório Curso Flask Codeshow

###Aula 1

Básico sobre Python

###Aula 2 - Parte 1
- Funções
- Decoradores
- Object (Python data model)

###Aula 3
- Divulgação de materiais de links
- Teoria sobre o protocolo HTTP
- Teoria sobre webserver e wsgi (revisar)
- Criando um wsgi simples
- requirements.txt / requirements-dev.txt
- Instalação do módulo flask, criação de uma instância da classe Flask
- Hello World com Flask
- Básico sobre debug
->export FLASK_ENV=development; Utilizando o PIN; flask routes; flask shell

###Aula 4 Pt1
- Factory pattern (Criação de uma função principal que pode
ser chamada em modo lazy, ou seja, podemos especificar a sua ordem de execução;
Será modularizar nossa aplicação de forma a ir montando as extensões por etapas).
- Contextos (Explicando a ordem em que as partes da aplicação devem ser configuradas
e executadas).
- Estudar: Factory patterns

###Aula 4 Pt2
- Configurando a estrutura para iniciar o desenvolvimento da aplicação
- Estudar: TDD Pytest (Testes com python); Setup-Tools (Criar uma aplicação instalável), fazer com
que o Python insira a aplicação "delivery.app" no syspath do mesmo.

###Aula 5
FLASK_APP=delivery/app.py -> Indica o local ao Flask onde a aplicação está localizada.
Tornando a aplicação instalável.
Parte 2: Finalizando a estrutura da aplicação com criação dos diretórios das extensões;
Construção do primeiro template, básico de Jinja e criação de um template básico.

###Aula 6
