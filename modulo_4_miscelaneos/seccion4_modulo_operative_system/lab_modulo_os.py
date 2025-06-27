"""4.4.8   LAB   El módulo os
No hace falta decir que los sistemas operativos te permiten buscar archivos y directorios. Mientras estudiabas esta parte del curso, se aprendió sobre las funciones del módulo os, que tiene todo lo que se necesita para escribir un programa que buscará directorios en una ubicación determinada.

Para facilitar tu tarea, hemos preparado una estructura de directorio de prueba para ti:

Tu programa debe cumplir con los siguientes requisitos:

Escribe una función o método llamado find que tome dos argumentos llamados path y dir. El argumento path debe aceptar una ruta relativa o absoluta a un directorio donde debe comenzar la búsqueda, mientras que el argumento dir debe ser el nombre de un directorio en el que deseas encontrar la ruta dada. Tu programa debería mostrar las rutas absolutas si encuentra un directorio con el nombre dado.
La búsqueda en el directorio debe realizarse de forma recursiva. Esto significa que la búsqueda también debe incluir todos los subdirectorios en la ruta dada.
Entrada de muestra:

path="./tree", dir="python"

"""
import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # No procesa un archivo que no es un directorio.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
    
