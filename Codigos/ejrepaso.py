# 🟦 1. Programa que solicita la edad y dice si es mayor o menor de edad  
*(Tema 11: uso de `input()`, casting a `int`, `if`, `print()`)*

```python
edad = int(input("¿Cuál es su edad? "))

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print("Programa finalizado")
```

---

# 🟦 2. Imprimir números del 0 al 100 divisibles por 5  
*(Tema 12: uso de `for` + `range()`)*

```python
for x in range(0, 101):
    if x % 5 == 0:
        print(x)
```

---

# 🟦 3. Bucle while que cuenta del 1 al 5  
*(Tema 12: bucle `while` y mensaje final)*

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

print("La ejecución ha terminado")
```

---

# 🟦 4. Recorrer una lista e imprimir sus elementos  
*(Tema 12: bucle `for` sobre secuencias)*

```python
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    print(n)
```

---

# 🟦 5. Caso práctico 1: Número entero mayor y menor de una lista  
*(Tema 12: detección de enteros, control de `None`, comparación segura)*

```python
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
```

---

# 🟦 6. Caso práctico 2: Conversión de decimal a binario usando ficheros  
*(Tema 12: funciones, ficheros, bucles, casting)*

### Función para convertir decimal a binario (sin `bin()`)

```python
def ConvertirBin(decimal):
    binario = ''

    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return str(decimal) + binario
```

### Lectura del fichero `decimal.txt`

```python
fich = open("decimal.txt", "r")
dec = fich.read()
fich.close()
```

### Conversión

```python
binario = ConvertirBin(int(dec))
```

### Escritura en `binario.txt`

```python
fich = open("binario.txt", "w")
fich.write(binario)
fich.close()
```

---
