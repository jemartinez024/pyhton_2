"""4.2.8 Flujos o streams pre-abiertos
Dijimos anteriormente que cualquier operación del stream debe estar precedida por la invocación de la función open(). Hay tres excepciones bien definidas a esta regla.

Cuando comienza nuestro programa, los tres streams ya están abiertos y no requieren ninguna preparación adicional. Además, tu programa puede usar estos streams explícitamente si tienes cuidado de importar el módulo sys:


import sys
 

Porque ahí es donde se coloca la declaración de estos streams.

Los nombres de los streams son: sys.stdin, sys.stdout, y sys.stderr.

Vamos a analizarlos:

sys.stdin
stdin (significa entrada estándar).
El stream stdin normalmente se asocia con el teclado, se abre previamente para la lectura y se considera como la fuente de datos principal para los programas en ejecución.
La función bien conocida input() lee datos de stdin por default.

sys.stdout
stdout (significa salida estándar)
El stream stdout normalmente está asociado con la pantalla, preabierta para escritura, considerada como el objetivo principal para la salida de datos por el programa en ejecución.
La función bien conocida print() envía los datos al stream stdout.

sys.stderr
stderr (significa salida de error estándar)
El stream stderr normalmente está asociado con la pantalla, preabierta para escribir, considerada como el lugar principal donde el programa en ejecución debe enviar información sobre los errores encontrados durante su trabajo.
No hemos presentado ningún método para enviar datos a este stream (lo haremos pronto, lo prometemos).
La separación de stdout (resultados útiles producidos por el programa) de stderr (mensajes de error, indudablemente útiles pero no proporcionan resultados) ofrece la posibilidad de redirigir estos dos tipos de información a los diferentes objetivos. Una discusión más extensa sobre este tema está más allá del alcance de nuestro curso. El manual del sistema operativo proporcionará más información sobre estos temas.
"""

"""
4.2.9 Cerrando los flujos (streams)
La última operación realizada en un stream (esto no incluye a los streams stdin, stdout, y stderr pues no lo requieren) debe ser cerrarlo.

Esa acción se realiza mediante un método invocado desde dentro del objeto del stream: stream.close().

El nombre de la función es fácil de entender close(), es decir cerrar.
La función no espera argumentos; el stream no necesita estar abierto.
La función no devuelve nada pero genera una excepción IOError en caso de un error.
La mayoría de los desarrolladores creen que la función close() siempre tiene éxito y, por lo tanto, no hay necesidad de verificar si ha realizado su tarea correctamente.

Esta creencia está solo parcialmente justificada. Si el stream se abrió para escribir y luego se realizó una serie de operaciones de escritura, puede ocurrir que los datos enviados al stream aún no se hayan transferido al dispositivo físico (debido a los mecanismos de cache o buffer).

Dado que el cierre del stream obliga a los bufers a descargarse, es posible que dichas descargas fallen y, por lo tanto, close() falle también.
Ya hemos mencionado fallas causadas por funciones que operan con los streams, pero no mencionamos nada sobre cómo podemos identificar exactamente la causa de la falla.

La posibilidad de hacer un diagnóstico existe y es proporcionada por uno de los componentes de excepción de los streams. Hablaremos acerca de ellos a continuación."""