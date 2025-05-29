"""
3.3.4 RESUMEN DE SECCIÓN
1. Una variable de instancia es una propiedad cuya existencia depende de la creación de un objeto. Cada objeto puede tener un conjunto diferente de variables de instancia.

Además, se pueden agregar y quitar libremente de los objetos durante su vida útil. Todas las variables de instancia de objeto se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada objeto por separado.


2. Una variable de instancia puede ser privada cuando su nombre comienza con __, pero no olvides que dicha propiedad aún es accesible desde fuera de la clase usando un nombre modificado construido como _ClassName__PrivatePropertyName.


3. Una variable de clase es una propiedad que existe exactamente en una copia y no necesita ningún objeto creado para ser accesible. Estas variables no se muestran como contenido de __dict__.

Todas las variables de clase pertenecientes a una clase se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada clase por separado.


4. Una función llamada hasattr() se puede utilizar para determinar si algún objeto o clase contiene cierta propiedad especificada.

Por ejemplo:


class Sample:
    gamma = 0 # Variable de clase.
    def __init__(self):
 
        self.alpha = 1 # Variable de instancia.
        self.__delta = 3 # Instancia de variable privada.
 
 
obj = Sample()
obj.beta = 2 # Otra variable de instancia (que existe solo dentro de la instancia "obj".)
print(obj.__dict__)
 
La salida del código es:

{'alpha': 1, '_Sample__delta': 3, 'beta': 2}"""