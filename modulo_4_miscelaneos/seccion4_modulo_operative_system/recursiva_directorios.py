"""4.4.4 Creación recursiva de directorios
La función mkdir es muy útil, pero ¿qué sucede si necesitas crear otro directorio dentro del directorio que acabas de crear? Por supuesto, puedes ir al directorio creado y crear otro directorio dentro de él, pero afortunadamente el módulo os proporciona una función llamada makedirs, que facilita esta tarea.

La función makedirs permite la creación recursiva de directorios, lo que significa que se crearán todos los directorios de la ruta. Veamos el código en el editor y veamos cómo es en la práctica."""

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())

"""New Component Title
El código debería producir el siguiente resultado:

Output
['my_second_directory']
El código crea dos directorios. El primero de ellos se crea en el directorio de trabajo actual, mientras que el segundo en el directorio my_first_directory.

No tienes que ir al directorio my_first_directory para crear el directorio my_second_directory, porque la función makedirs hace esto por ti. En el ejemplo anterior, vamos al directorio my_first_directory para mostrar que el comando makedirs crea el subdirectorio my_second_directory.

Para moverte entre directorios, puedes usar una función llamada chdir, que cambia el directorio de trabajo actual a la ruta especificada. Como argumento, toma cualquier ruta relativa o absoluta. En nuestro ejemplo, le pasamos el nombre del primer directorio.

NOTA: El equivalente de la función makedirs en sistemas Unix es el comando mkdir con el indicador -p, mientras que en Windows, simplemente el comando mkdir con la ruta:

New Component Title
Sistemas tipo Unix:
mkdir -p my_first_directory/my_second_directory
Windows:
mkdir my_first_directory/my_second_directory"""
