def soma_tudo(*args):
    soma = 0
    for num in args:
        soma += num
    return soma



if __name__ == "__main__":
    numeros = [x for x in range(1, 11)]
    total = soma_tudo(*numeros)
    print(total)
    print(type(total))