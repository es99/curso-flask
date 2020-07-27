from datetime import datetime

def grava_arquivo():
    data = datetime.now().strftime("%d/%/%Y - %H:%M")
    with open('logs.txt', 'a') as file:
        file.write("email enviado " + data)

def verifica(function):
    def wrapper(end):
        grava_arquivo()
        function(end)
    return wrapper

@verifica
def envia_email(endereco):
    print(f"email enviado para {endereco}")

if __name__ == "__main__":
    envia_email('engels@gmail.com')

