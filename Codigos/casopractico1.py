lista = [1, 2, "árbol", 5, 1.5, 6, "a"]

enteros = []

for elemento in lista:
    if type(elemento) == int:
        enteros.append(elemento)

mayor = max(enteros)
menor = min(enteros)

print("Enteros encontrados:", enteros)
print("Mayor entero:", mayor)
print("Menor entero:", menor)
