"""4.1.3 Cómo construir un generador
Cómo construir un generador:
Permítenos mostrarte el nuevo generador en acción.

Así es como podemos usarlo:


def fun(n):
    for i in range(n):
        yield i
 
 
for v in fun(5):
    print(v)
 

¿Puedes adivinar la salida?


0
1
2
3
4"""


"""def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)"""

"""Listas por comprensión

Los generadores también se pueden usar con listas por comprensión, justo como aquí:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = [x for x in powers_of_2(5)]
print(t)

Output:
[1, 2, 4, 8, 16]

"""
"""Ejecuta el ejemplo y verifica la salida.


La función list()

La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = list(powers_of_2(3))
print(t)

Nuevamente, intenta predecir el resultado y ejecuta el código para verificar tus predicciones.
 
output:
[1, 2, 4] 

"""

"""El operador in

Además, el contexto creado por el operador in también te permite usar un generador.

El ejemplo muestra cómo hacerlo:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4):
        print(i)
 

¿Cuál es la salida del código? Ejecuta el programa y verifica.

"""
"""El generador de números Fibonacci

Ahora veamos un generador de números de la serie Fibonacci, asegurandonos que se vea mucho mejor que la versión orientada a objetos basada en la implementación directa del protocolo iterador.

Aquí está:


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
 
fibs = list(fibonacci(10))
print(fibs)
 

Adivina la salida (una lista) producida por el generador y ejecuta el código para verificar si tenías razón."""

# Output:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]