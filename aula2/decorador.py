from datetime import datetime

def grava_arquivo():
    data = datetime.now().strftime("%d/%/%Y - %H:%M")
    with open('logs.txt', 'a') as file:
        file.write("email enviado " + data)

def verifica(function):
    def wrapper():
        grava_arquivo()
        function()
    return wrapper

def imprime_ola():
    print("Olá mundo")

@verifica
def envia_email(endereco):
    print(f"email enviado para {endereco}")

if __name__ == "__main__":
    verifica(imprime_ola())

