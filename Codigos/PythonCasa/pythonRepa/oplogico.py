numero = int(input("¿Cuál es su numero? "))

if numero > 10 and numero < 20:
    print("el numero es mayor que 10 y menor que 20")
elif numero < 5 or numero > 50:
    print("el numero es menor que 5 o mayor que 50")
elif not(numero == 0):
    print("el numero no es 0")
else:
    print()
print("listo")