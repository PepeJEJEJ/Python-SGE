a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

if a > b:
    print(str(a)+' Es mayor que '+str(b))
elif a < b:
    if a < b:
        print(str(b) + ' Es mayor que ' + str(a))
    else:
        print("ambos son iguales")