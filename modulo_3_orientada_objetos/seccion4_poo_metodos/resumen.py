"""
3.4.5 RESUMEN DE SECCIÓN
1. Un método es una función dentro de una clase. El primer (o único) parámetro de cada método se suele llamar self, que está diseñado para identificar al objeto para el que se invoca el método con el fin de acceder a las propiedades del objeto o invocar sus métodos.


2. Si una clase contiene un constructor (un método llamado __init__), este no puede devolver ningún valor y no se puede invocar directamente.


3. Todas las clases (pero no los objetos) contienen una propiedad llamada __name__, que almacena el nombre de la clase. Además, una propiedad llamada __module__ almacena el nombre del módulo en el que se ha declarado la clase, mientras que la propiedad llamada __bases__ es una tupla que contiene las superclases de una clase.

Por ejemplo:


class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("Mi nombre es " + self.name + " y estoy viviendo en " + Sample.__module__)
 
 
obj = Sample()
obj.myself()
 
El código da como salida:

Output
Mi nombre es Sample y estoy viviendo en __main__"""