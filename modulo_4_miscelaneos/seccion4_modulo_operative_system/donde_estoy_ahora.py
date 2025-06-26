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
    