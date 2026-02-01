import turtle
ventana = turtle.Screen()
tortuga = turtle.Turtle()
def figura(lados):
 for i in range(lados):
  tortuga.forward(100)
  tortuga.left(360/lados)
lados = input("Introduce el número de lados de la figura: ")
figura(int(lados))
ventana.exitonclick()