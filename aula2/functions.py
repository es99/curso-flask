maiusculo = False

def ola(name, cpf, idade=0, maiusculo=False, *args, **kwargs):
    print(args)
    print(kwargs)
    if maiusculo:
        msg = f"Olá, {name}".upper()
    else:
        msg= f"Olá, {name}, {cpf}, {idade}"

    print(msg)

def exibe_dicionario(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} -> {v}")

def atributos(forca=" ", agilidade=" ", destreza=" "):
    print(
        "forca: {}\n"
        "agi: {}\n"
        "dex: {}".format(forca, agilidade, destreza)
    )

def soma(a: int, b: int) -> int:
    return a + b

def mensagem(func1, func2):
    func1()
    print("Ola vc esta no codeshow")
    func2()

def header():
    print("## Inicio")

def footer():
    print("## Fim")


if __name__ == "__main__":
   mensagem(header, footer)
