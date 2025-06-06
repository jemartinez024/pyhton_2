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