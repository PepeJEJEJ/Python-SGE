a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

if a > 10 or b > 10:
    print("Alguno de los dos es mayor que 10")
elif a // 2 == 0:
    if b // 2 == 0:
        print("Los 2 son pares")
    else:
        print("Al menos uno es par")