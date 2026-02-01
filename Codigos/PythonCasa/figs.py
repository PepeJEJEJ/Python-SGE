import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(0)  # velocidad máxima

# Función que dibuja cuadrados concéntricos rotados
def cuadrados_concentricos_rotados(cantidad, tamaño_inicial, incremento, rotacion):
    for i in range(cantidad):
        tortuga.penup()
        tortuga.goto(0, 0)
        tortuga.setheading(rotacion * i)  # rotar cada cuadrado
        tortuga.forward(tamaño_inicial + i * incremento)
        tortuga.right(90)
        tortuga.pendown()

        for _ in range(4):
            tortuga.forward(tamaño_inicial + i * incremento)
            tortuga.right(90)

# 🟡 Pedir al usuario cuántas veces quiere repetir
veces = int(input("¿Cuántos cuadrados quieres que se dibujen? "))

# Llamar a la función con ese número
cuadrados_concentricos_rotados(cantidad=veces, tamaño_inicial=20, incremento=10, rotacion=10)

ventana.exitonclick()
