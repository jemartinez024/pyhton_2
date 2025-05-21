"""2.7.1 Excepciones
Python 3 define 63 excepciones integradas, y todas ellas forman una jerarquía en forma de árbol, aunque el árbol es un poco extraño ya que su raíz se encuentra en la parte superior.

Algunas de las excepciones integradas son más generales (incluyen otras excepciones) mientras que otras son completamente concretas (solo se representan a sí mismas). Podemos decir que cuanto más cerca de la raíz se encuentra una excepción, más general (abstracta) es. A su vez, las excepciones ubicadas en los extremos del árbol (podemos llamarlas hojas) son concretas.

Observa la figura:"""

"""Muestra una pequeña sección del árbol completo de excepciones. Comencemos examinando el árbol desde la hoja ZeroDivisionError.

Nota:

ZeroDivisionError es un caso especial de una clase de excepción más general llamada ArithmeticError.
ArithmeticError es un caso especial de una clase de excepción más general llamada solo Exception.
Exception es un caso especial de una clase más general llamada BaseException.
Podemos describirlo de la siguiente manera (observa la dirección de las flechas; siempre apuntan a la entidad más general):

BaseException
↑
Exception
↑
ArithmeticError
↑
ZeroDivisionError


Te mostraremos el funcionamiento esta generalización. Comencemos con un código realmente simple.

Observa el código en el editor. Es un ejemplo simple para comenzar. Ejecútalo."""

"""try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuupsss...")

print("FIN.")"""

"""try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")
 
print("FIN.")"""


"""try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre cero!")
except ArithmeticError:
    print("¡Problema Aritmético!")

print("FIN.")"""

"""La primera coincidencia es la que contiene ZeroDivisionError. Significa que la consola mostrará:

¡División entre cero!
FIN.
Output
¿Cambiará algo si intercambiamos los dos bloques except? Justo como aquí abajo:


try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre cero!")
 
print("FIN.")
 

El cambio es radical: la salida del código es ahora:

¡Problema aritmético!
FIN.
Output
¿Por qué, si la excepción planteada es la misma que anteriormente?

La excepción es la misma, pero la excepción más general ahora aparece primero: también capturará todas las divisiones entre cero. También significa que no hay posibilidad de que alguna excepción llegue a ZeroDivisionError. Ahora es completamente inalcanzable.

Recuerda:

¡El orden de las excepciones importa!
No coloques excepciones más generales antes que otras más concretas.
Esto hará que el último sea inalcanzable e inútil.
Además, hará que el código sea desordenado e inconsistente.
Python no generará ningún mensaje de error con respecto a este problema.
Si deseas manejar dos o más excepciones de la misma manera, puedes usar la siguiente sintaxis:

try:
    :
except (exc1, exc2):
    :
 
Simplemente tienes que poner todos los nombres de las excepciones empleadas en una lista separada por comas y no olvidar los paréntesis.


Si una excepción es generada dentro de una función, puede ser manejada:

Dentro de la función.
Fuera de la función.
Comencemos con la primera variante: observa el código en el editor."""

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

bad_fun(0)

print("FIN.")