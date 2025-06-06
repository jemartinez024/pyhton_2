"""3.6.1 Más acerca de excepciones
El discutir sobre la programación orientada a objetos ofrece una muy buena oportunidad para volver a las excepciones. La naturaleza orientada a objetos de las excepciones de Python las convierte en una herramienta muy flexible, capaz de adaptarse a necesidades específicas, incluso aquellas que aún no conoces.

Antes de adentrarnos en el lado orientado a objetos de las excepciones, queremos mostrarte algunos aspectos sintácticos y semánticos de la forma en que Python trata el bloque try-except, ya que ofrece un poco más de lo que hemos presentado hasta ahora.

La primera característica que queremos analizar aquí es un bloque adicional que se puede colocar dentro (o más bien, directamente detrás) del bloque try-except: es la parte del código que comienza con else, justo como el ejemplo en el editor."""


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n


print(reciprocal(2))
print(reciprocal(0))


"""Un código etiquetado de esta manera se ejecuta cuando (y solo cuando) no se ha generado ninguna excepción dentro de la parte del try:. Podemos decir que este bloque se ejecuta después del try:, ya sea el que comienza con except (no olvides que puede haber más de un bloque de este tipo) o la que comienza con else.

Nota: el bloque else: debe ubicarse después del último bloque except.

El código de ejemplo produce el siguiente resultado:

Output
Todo salió bien
0.5
División fallida
None

El try-except se puede extender de una manera más - agregando una parte encabezada por la palabra clave reservada finally (debe ser el último bloque del código diseñado para manejar excepciones).

Nota: estas dos variantes (else y finally) no son dependientes entre si, y pueden coexistir u ocurrir de manera independiente.

El bloque finally siempre se ejecuta (finaliza la ejecución del bloque try-except, de ahí su nombre), sin importar lo que sucedió antes, incluso cuando se genera una excepción, sin importar si esta se ha manejado o no.

Observa el código en el editor."""

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es momento de decir adiós")
        return n


print(reciprocal(2))
print(reciprocal(0))