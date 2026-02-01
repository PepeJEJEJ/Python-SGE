#Escribe un programa en Python que pida al usuario su edad y muestre un mensaje indicando
# si es mayor o menor de edad.
#Requisitos:
#Pedir la edad por teclado.
#Convertirla a número.
#Mostrar:
# "Eres mayor de edad" si tiene 18 o más.
# "Eres menor de edad" si tiene menos de 18.

edad = int(input("¿Tu edad? "))
if edad<18:
    print("eres menor de edad")
elif edad>18:
    print("eres mayor de edad")