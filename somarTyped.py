def somar(*numeros):
    print(type(numeros))
    return sum(numeros)

print(somar(1, 2))
print(somar(1, 2, 3, 4))
