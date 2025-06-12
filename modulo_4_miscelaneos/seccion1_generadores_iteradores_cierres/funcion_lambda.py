"""4.1.5 La función lambda
La función lambda es un concepto tomado de las matemáticas, más específicamente, de una parte llamada el Cálculo Lambda, pero estos dos fenómenos no son iguales.

Los matemáticos usan el Cálculo Lambda en sistemas formales conectados con: la lógica, la recursividad o la demostrabilidad de teoremas. Los programadores usan la función lambda para simplificar el código, hacerlo más claro y fácil de entender.

Una función lambda es una función sin nombre (también puedes llamarla una función anónima). Por supuesto, tal afirmación plantea inmediatamente la pregunta: ¿cómo se usa algo que no se puede identificar?

Afortunadamente, no es un problema, ya que se puede mandar llamar dicha función si realmente se necesita, pero, en muchos casos la función lambda puede existir y funcionar mientras permanece completamente de incógnito.

La declaración de la función lambda no se parece a una declaración de función normal; compruébalo tu mismo:

lambda parameters: expression"""


"""Tal cláusula devuelve el valor de la expresión al tomar en cuenta el valor del argumento lambda actual.

Como de costumbre, un ejemplo será útil. Nuestro ejemplo usa tres funciones lambda, pero con nombres. Analízalo cuidadosamente:


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
 

Vamos a analizarlo:

La primer lambda es una función anónima sin parámetros que siempre devuelve un 2. Como se ha asignado a una variable llamada two, podemos decir que la función ya no es anónima, y se puede usar su nombre para invocarla.

La segunda es una función anónima de un parámetro que devuelve el valor de su argumento al cuadrado. Se ha nombrado sqr.

La tercer lambda toma dos parámetros y devuelve el valor del primero elevado al segundo. El nombre de la variable que lleva la lambda habla por si mismo. No se utiliza pow para evitar confusiones con la función incorporada del mismo nombre y el mismo propósito.

El programa produce el siguiente resultado:

Output
4 4
1 1
0 0
1 1
4 4

Este ejemplo es lo suficientemente claro como para mostrar como se declaran las funciones lambda y cómo se comportan, pero no dice nada acerca de por que son necesarias y para qué se usan, ya que se pueden reemplazar con funciones de Python de rutina.

¿Dónde está el beneficio?"""

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# El beneficio de las funciones lambda es que pueden ser utilizadas en contextos donde se requiere una función pequeña y rápida, sin necesidad de definir una función completa con un nombre. Esto es especialmente útil en funciones de orden superior como `map()`, `filter()`, y `sorted()`, donde se necesita una función simple para aplicar a cada elemento de una colección.
# Por ejemplo, si quisiéramos usar `sqr` y `pwr` directamente en una función como `map`, podríamos hacerlo sin necesidad de definir una función completa:

"""4.1.6 ¿Cómo usar lambdas y para qué?
La parte más interesante de usar lambdas aparece cuando puedes usarlas en su forma pura: como partes anónimas de código destinadas a evaluar un resultado.

Imagina que necesitamos una función (la nombraremos print_function) que imprime los valores de una (otra) función dada para un conjunto de argumentos seleccionados.

Queremos que print_function sea universal, debería aceptar un conjunto de argumentos incluidos en una lista y una función a ser evaluada, ambos como argumentos; no queremos codificar nada.

Mira el ejemplo en el editor. Así es como hemos implementado la idea."""

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

"""Analicémoslo. La función print_function() toma dos parámetros:

El primero, una lista de argumentos para los que queremos imprimir los resultados.
El segundo, una función que debe invocarse tantas veces como el número de valores que se recopilan dentro del primer parámetro.
Nota: También hemos definido una función llamada poly(), esta es la función cuyos valores vamos a imprimir. El cálculo que realiza la función no es muy sofisticado: es el polinomio (de ahí su nombre) de la forma:

f(x) = 2x2 - 4x + 2

El nombre de la función se pasa a print_function() junto con un conjunto de cinco argumentos diferentes, el conjunto está construido con una cláusula de comprensión de la lista.

El código imprime las siguientes líneas:

Output
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2

¿Podemos evitar definir la función poly(), ya que no la vamos a usar más de una vez? Si, podemos: este es el beneficio que puede aportar una función lambda.


Mira el ejemplo de abajo. ¿Puedes ver la diferencia?

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
 

La función print_function() se ha mantenido exactamente igual, pero no hay una función poly(). Ya no la necesitamos, ya que el polinomio ahora está directamente dentro de la invocación de la función print_function() en forma de una lambda definida de la siguiente manera:


lambda x: 2 * x**2 - 4 * x + 2
 

El código se ha vuelto más corto, más claro y más legible.

Permítenos mostrarte otro lugar donde las lambdas pueden ser útiles. Comenzaremos con una descripción de map(), una función integrada de Python. Su nombre no es demasiado descriptivo, su idea es simple y la función en sí es muy utilizable."""