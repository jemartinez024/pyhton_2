"""
4.2.12 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cómo codificas el valor del argumento mode de una función open() si vas a crear un nuevo archivo de texto para llenarlo con solo un artículo?

Ocultar
"wt" o "w"

Pregunta 2: ¿Cuál es el significado del valor representado por errno.EACCES?

Ocultar
Permiso denegado: no se permite acceder al contenido del archivo.

Pregunta 3: ¿Cuál es el resultado esperado del siguiente código, suponiendo que el archivo llamado file no existe?

import errno
 
try:
    stream = open("file", "rb")
     print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")
 
Ocultar
ausente"""