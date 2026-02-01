Qué es Python

Lenguaje interpretado, de alto nivel y multiparadigma. Se lee casi como inglés y sirve para muchas cosas: web, datos, IA, automatización.

Ventajas: gratuito, multiplataforma, gran biblioteca estándar y muchas librerías externas (p. ej. Pandas, Django, TensorFlow).

Instalación y PyCharm

Instalar Python: descarga desde python.org e instala. En macOS/Linux suele venir preinstalado.

Modos de uso: modo interactivo (escribes línea a línea) o ejecutar scripts .py.

PyCharm (Community): IDE recomendado. Crea proyectos con Virtualenv para aislar dependencias.

Conceptos básicos y ejemplos

Tipos de datos: int, float, complex, str, bool, list, tuple, dict, set, range.

Casting: convertir tipos con int(), float(), str().

Entrada y salida: input() siempre devuelve str; print() muestra por pantalla.

Variables y constantes: no se declaran; se asignan. Convención: constantes en mayúsculas (MI_CONST = 3).

Ejemplo rápido

op1 = int(input("Operando 1: "))
op2 = int(input("Operando 2: "))
print("Suma:", op1 + op2)
print("Multiplicación:", op1 * op2)

Errores y control

Errores comunes: SyntaxError (mala sintaxis), TypeError (operaciones entre tipos incompatibles).

Manejo de errores: usa try, except, else, finally para capturar y tratar excepciones.

Ejemplo

try:
    x = int(input("Número: "))
except ValueError:
    print("Eso no es un número")
finally:
    print("Fin")

Estructuras, funciones y archivos

Condicionales: if, elif, else. Indentación obligatoria.

Bucles: for (itera secuencias) y while.

Funciones: def nombre(params): y return.

Módulos y paquetes: import modulo o from modulo import func.

Ficheros: open("archivo.txt", "r/w/a"), read(), write(), close(); mejor usar with open(...) as f:.

Operadores clave

Aritméticos: + - * / % ** //

Asignación: =, +=, -=, *=, /=

Comparación: ==, !=, >, <, >=, <=

Lógicos: and, or, not

Pertenencia e identidad: in, not in, is, is not

Bit a bit: &, |, ^, ~, <<, >>

Instala Python y PyCharm. Practica con print y input.

Aprende tipos, casting y errores. Eso evita los fallos más comunes.

Usa funciones, módulos y ficheros para organizar tu código.

Práctica: escribe pequeños programas (suma, conversión decimal→binario, leer/escribir ficheros) y repite.

Conceptos básicos en Python: Operadores

En Python, podemos encontrarnos con varios tipos de operadores:

Operadores aritméticos

Operadores de asignación

Operador

Ejemplo

Equivalente

=

X = 1

X = 1

+=

x += 1

X = X + 1

-=

x -= 1

X = X - 1

*=

x *= 1

X = x * 1

/=

x /= 1

x = x / 1

%=

x %= 1

x = x % 1

//=

x //= 1

x = x // 1

**=

x **= 1

x = x ** 1

Operadores de comparación

Operador

Nombre

Ejemplo

==

Igual que

x == y

!=

Distinto de

x != y

Operadores lógicos

Operador

Descripción

Ejemplo

and

Verdadero si ambos operandos son verdaderos

x < 1 and x < 3

or

Verdadero si al menos uno es verdadero

x < 1 or x < 3

not

Niega el valor del operando

not(x < 1)

Operadores de identidad

Operador

Descripción

Ejemplo

is

Verdadero si ambas variables son el mismo objeto

x is y

is not

Verdadero si no son el mismo objeto

x is not y

Operadores de pertenencia

Operador

Descripción

Ejemplo

in

Verdadero si un objeto está presente en otro

x in y

not in

Verdadero si un objeto no está presente

x not in y

Operadores bit a bit

Operador

Nombre

Descripción

&

AND

Devuelve 1 si ambos bits son 1

|

OR

Devuelve 1 si al menos uno de los bits es 1

^

XOR

Devuelve 1 si solo uno de los bits es 1

~

NOT

Invierte todos los bits (complemento a uno)

<<

Desplazamiento a izquierda

Desplaza bits a la izquierda, rellenando con ceros por la derecha

>>

Desplazamiento a derecha

Rellena con ceros por la derecha (normalmente rellena con el bit de signo)

