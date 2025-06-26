"""4.4.6 Eliminando directorios en Python
El módulo os también te permite eliminar directorios. Te da la opción de borrar un solo directorio o un directorio con sus subdirectorios. Para eliminar un solo directorio, puedes usar una función llamada rmdir, que toma la ruta como argumento. Mira el código en el editor."""

import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())


"""El ejemplo anterior es realmente simple. Primero, se crea el directorio my_first_directory y luego se elimina usando la función rmdir. La función listdir se utiliza como prueba de que el directorio se ha eliminado correctamente. En este caso, devuelve una lista vacía. Al eliminar un directorio, asegúrate de que exista y esté vacío; de lo contrario, se generará una excepción.

New Component Title
Para eliminar un directorio y sus subdirectorios, puedes utilizar la función removedirs, que requiere que se especifique una ruta que contenga todos los directorios que deben eliminarse:


import os
 
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
 

Al igual que con la función rmdir, si uno de los directorios no existe o no está vacío, se generará una excepción.

NOTA: Tanto en Windows como en Unix, hay un comando llamado rmdir, que, al igual que la función rmdir, elimina directorios. Además, ambos sistemas tienen comandos para eliminar un directorio y su contenido. En Unix, este es el comando rm con el indicador -r."""