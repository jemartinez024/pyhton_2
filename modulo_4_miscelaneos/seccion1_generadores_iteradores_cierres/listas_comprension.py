"""4.1.4 Más acerca de listas por comprensión
Debes poder recordar las reglas que rigen la creación y el uso de un fenómeno de Python llamado listas por comprensión: una forma simple de crear listas y sus contenidos.

En caso de que lo necesites, te proporcionamos un recordatorio en el editor."""


list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)
#
# La salida es la misma:

"""Existen dos partes dentro del código, ambas crean una lista que contiene algunas de las primeras potencias naturales de diez.

La primer parte utiliza una forma rutinaria del bucle for, mientras que la segunda hace uso de listas por comprensión y construye la lista en el momento, sin necesidad de un bucle o cualquier otro código.

Pareciera que la lista se crea dentro de sí misma; esto es falso, ya que Python tiene que realizar casi las mismas operaciones que en la primera parte, pero el segundo formalismo es simplemente más elegante y le evita al lector cualquier detalle innecesario.

El ejemplo genera dos líneas idénticas que contienen el siguiente texto:

Output
[1, 10, 100, 1000, 10000, 100000]
[1, 10, 100, 1000, 10000, 100000]

Ejecuta el código para verificar si tenemos razón."""


"""Hay una sintaxis muy interesante que queremos mostrarte ahora. Su usabilidad no se limita a listas por comprensión, pero hay que reconocer que las comprensiones son el entorno ideal para ello.

Es una expresión condicional: una forma de seleccionar uno de dos valores diferentes en función del resultado de una expresión Booleana.

Observa:

expression_one if condition else expression_two

Puede parecer un poco sorprendente a primera vista, pero hay que tener en cuenta que no es una instrucción condicional. Además, no es una instrucción en lo absoluto. Es un operador.

El valor que proporciona es expression_one cuando la condición es True, y expression_two de lo contrario.

Un buen ejemplo te dirá más. Mira el código en el editor."""


the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

"""El código llena una lista con 1s y 0s, si el índice de un elemento particular es impar, el elemento se establece a 0, y a 1 de lo contrario.

¿Simple? Quizás no a primera vista. ¿Elegante? Indiscutiblemente.

¿Se puede usar el mismo truco dentro de una comprensión de lista? Sí, por supuesto.

Observa el ejemplo en el editor."""

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

"""Compacto y elegante - estas dos palabras vienen a la mente al mirar el código.

Entonces, ¿qué tienen en común, generadores y listas por comprensión? ¿Hay alguna conexión entre ellos? Si. Una conexión algo suelta, pero inequívoca.

Solo un cambio puede convertir cualquier comprensión en un generador.


Listas por comprensión versus generadores

Ahora observa el código a continuación y ve si puedes encontrar el detalle que convierte una comprensión de lista en un generador:"""


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

