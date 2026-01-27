lista = [1, 2, "árbol", 5, 1.5, 6, "a"]

menor = None
mayor = None

for x in lista:
    if type(x) is int:
        if menor is None and mayor is None:
            menor = mayor = x
        elif x < menor:
            menor = x
        elif x > mayor:
            mayor = x

print("Menor:", menor)
print("Mayor:", mayor)