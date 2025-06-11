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


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

