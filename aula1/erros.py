a = 0
b = 10


try:
    b.upper
    print(b // a)
except AttributeError as err:
    print("Nao posso transformar numero em maisculo", str(err))
except ZeroDivisionError as err:
    print(err)
