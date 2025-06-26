"""
4.3.12 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Qué se espera del método readlines() cuando el stream está asociado con un archivo vacío?

Ocultar
Una lista vacía (una lista de longitud cero).

Pregunta 2: ¿Qué se pretende hacer con el siguiente código?

for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')
 
Ocultar
Copia el contenido del archivo file hacia la consola, ignorando las vocales.

Pregunta 3: Vas a procesar un mapa de bits almacenado en un archivo llamado image.png y quieres leer su contenido como un todo en una variable bytearray llamada image. Agrega una línea al siguiente código para lograr este objetivo.

try:
    stream = open("image.png", "rb")
    # Inserta una línea aquí.
    stream.close()
except IOError:
    print("fallido")
else:
    print("exitoso")
 
Ocultar
image = bytearray(stream.read())
    """