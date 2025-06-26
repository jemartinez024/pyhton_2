"""4.4.5 ¿Dónde estoy ahora?
Ya sabes cómo crear directorios y cómo moverte entre ellos.

A veces, cuando tienes una estructura de directorio muy grande en la que navegas, es posible que no sepas en qué directorio estás trabajando actualmente.


Como probablemente habrás adivinado, el módulo os proporciona una función que devuelve información sobre el directorio de trabajo actual. Se llama getcwd.

Mira el código en el editor para ver cómo usarlo en la práctica.
"""

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

"""En el ejemplo, creamos el directorio my_first_directory y el directorio my_second_directory dentro de él. En el siguiente paso, cambiamos el directorio de trabajo actual al directorio my_first_directory y luego mostramos el directorio de trabajo actual (primera línea del resultado).

A continuación, vamos al directorio my_second_directory y nuevamente mostramos el directorio de trabajo actual (segunda línea del resultado). Como puedes ver, la función getcwd devuelve la ruta absoluta a los directorios.

NOTA: En sistemas tipo Unix, el equivalente de la función getcwd es el comando pwd, que imprime el nombre del directorio de trabajo actual."""