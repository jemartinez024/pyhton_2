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

"""def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

bad_fun(0)

print("FIN.")"""


"""def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que ocurrió? ¡Se generó una excepción!")

print("FIN.")"""


"""El problema tiene que ser resuelto por el invocador (o por el invocador del invocador, y así sucesivamente).

La salida del programa es:

¿Que ocurrió? ¡Se generó una excepción!
FIN.
Output
Nota: la excepción generada puede cruzar la función y los límites del módulo, y viajar a través de la cadena de invocación buscando una cláusula except capaz de manejarla.

Si no existe tal cláusula, la excepción no se controla y Python resuelve el problema de la manera estándar, terminando el código y emitiendo un mensaje de diagnóstico.

Ahora vamos a suspender esta discusión, ya que queremos presentarte una nueva instrucción de Python.

La instrucción raise genera la excepción especificada denominada exc como si se hubiera generado de forma normal (natural):


raise exc

Nota: raise es una palabra clave reservada.

La instrucción te permite:

Simular excepciones reales (por ejemplo, para probar tu estrategia de manejo de excepciones).
Parcialmente manejar una excepción y hacer que otra parte del código sea responsable de completar el manejo.
Observa el código en el editor. Así es como puedes usarlo en la práctica."""

"""def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")"""

"""La salida del programa permanece sin cambios.

De esta forma, puede probar tu rutina de manejo de excepciones sin obligar al código a hacer cosas peligrosas.

La instrucción raise también se puede utilizar de la siguiente manera (toma en cuenta la ausencia del nombre de la excepción):


raise
 
Existe una seria restricción: esta variante de la instrucción raise puede ser utilizada solamente dentro del bloque except; usarla en cualquier otro contexto causa un error.

La instrucción volverá a generar la misma excepción que se maneja actualmente.


Gracias a esto, puedes distribuir el manejo de excepciones entre diferentes partes del código.

Observa el código en el editor. Ejecútalo, lo veremos en acción."""

"""def bad_fun(n):
    try:
        return n / 1
    except:
        print("¡Lo hice otra vez!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")"""

"""La excepción ZeroDivisionError es generada dos veces:

Primero, dentro del try debido a que se intentó realizar una división entre cero.
Segundo, dentro de la parte except por la instrucción raise.
En efecto, la salida del código es:

¡Lo hice otra vez!
¡Ya veo!
FIN.
Output
Ahora es un buen momento para mostrarte otra instrucción de Python, llamada assert (afirmar). Esta es una palabra clave reservada.


assert expression
 
¿Cómo funciona?

Se evalúa la expresión.
Si la expresión se evalúa como True (Verdadera), o un valor numérico distinto de cero, o una cadena no vacía, o cualquier otro valor diferente de None, no hará nada más.
De lo contrario, automáticamente e inmediatamente se genera una excepción llamada AssertionError (en este caso, decimos que la afirmación ha fallado).
¿Cómo puede ser utilizada?

Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes (por ejemplo, dentro de una función utilizada por otra persona).
El generar una excepción AssertionError asegura que tu código no produzca resultados no válidos y muestra claramente la naturaleza de la falla.
Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.
Si las excepciones y la validación de datos son como conducir con cuidado, la aserción puede desempeñar el papel de una bolsa de aire.


Veamos a la instrucción assert en acción. Observa el código en el editor. Ejecútalo."""

import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)