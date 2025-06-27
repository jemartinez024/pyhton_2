"""
4.4.9 RESUMEN DE SECCIÓN
1. La función uname devuelve un objeto que contiene información sobre el sistema operativo actual. El objeto tiene los siguientes atributos:

systemname (almacena el nombre del sistema operativo)
nodename (almacena el nombre de la máquina en la red)
release (almacena el release o actualización del sistema operativo)
version (almacena la versión del sistema operativo)
machine (almacena el identificador de hardware, por ejemplo, x86_64)
2. El atributo name disponible en el módulo os te permite distinguir el sistema operativo. Devuelve uno de los siguientes tres valores:

posix (obtendrás este nombre si usas Unix)
nt (obtendrás este nombre si usas Windows)
java (obtendrá este nombre si tu código está escrito en algo como Jython)
3. La función mkdir crea un directorio en la ruta pasada como argumento. La ruta puede ser relativa o absoluta, por ejemplo:

import os
 
os.mkdir("hello") # la ruta relativa
os.mkdir("/home/python/hello") # la ruta absoluta
 
Nota: Si el directorio existe, una excepción FileExistsError será generada. Además de la función mkdir, el módulo os proporciona la función makedirs, que te permite crear recursivamente todos los directorios en una ruta.

4. El resultado de la función listdir() es una lista que contiene los nombres de los archivos y directorios que se encuentran en la ruta pasada como argumento.

Es importante recordar que la función listdiromite las entradas '.' y '..', que se muestran, por ejemplo, cuando se utiliza el comando ls -a en sistemas Unix. Si no se pasa la ruta, el resultado se devolverá para el directorio de trabajo actual.

5. Para moverte entre directorios, puedes usar una función llamada chdir(), que cambia el directorio de trabajo actual a la ruta especificada. Como argumento, toma cualquier ruta relativa o absoluta.

Si deseas averiguar cuál es el directorio de trabajo actual, puedes usar la función getcwd(), que devuelve la ruta actual.

6. Para eliminar un directorio, puedes usar la función rmdir(), pero para eliminar un directorio y sus subdirectorios, emplea la función removedirs().

7. Tanto en Unix como en Windows, puedes usar la función system, que ejecuta el comando que se le pasa como cadena, por ejemplo:


import os
 
returned_value = os.system("mkdir hello")
 
La función system en Windows devuelve el valor devuelto por el shell después de ejecutar el comando dado, mientras que en Unix devuelve el estado de salida del proceso."""