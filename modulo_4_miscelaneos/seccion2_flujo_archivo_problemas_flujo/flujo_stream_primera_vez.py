"""4.2.7 Abriendo el flujo (stream) por primera vez
Imagina que queremos desarrollar un programa que lea el contenido del archivo de texto llamado: C:\Users\User\Desktop\file.txt.

¿Cómo abrir ese archivo para leerlo? Aquí está el fragmento del código:


try:
    stream = open("C:\Users\User\Desktopile.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


 

¿Que está pasando aqui?

Hemos abierto el bloque try-except ya que queremos manejar los errores de tiempo de ejecución suavemente.
Se emplea la función open() para intentar abrir el archivo especificado (ten en cuenta la forma en que hemos especificado el nombre del archivo).
El modo de apertura se define como texto para leer (como texto es la configuración predeterminada, podemos omitir la t en la cadena de modo).
En caso de éxito obtenemos un objeto de la función open() y lo asignamos a la variable del stream.
Si open() falla, manejamos la excepción imprimiendo la información completa del error (es bueno saber qué sucedió exactamente)."""