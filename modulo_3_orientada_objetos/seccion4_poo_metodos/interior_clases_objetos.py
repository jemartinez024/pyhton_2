"""3.4.2 La vida al interior de las clases y objetos
Cada clase de Python y cada objeto de Python está pre-equipado con un conjunto de atributos útiles que pueden usarse para examinar sus capacidades.

Ya conoces uno de estos: es la propiedad __dict__.

Observemos como esta propiedad trata con los métodos: mira el código en el editor."""


class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

"""Ejecútalo para ver que produce. Verifica el resultado.

Encuentra todos los métodos y atributos definidos. Localiza el contexto en el que existen: dentro del objeto o dentro de la clase.


__dict__ es un diccionario. Otra propiedad incorporada que vale la pena mencionar es una cadena llamada __name__.

La propiedad contiene el nombre de la clase. No es nada emocionante, es solo una cadena.

Nota: el atributo __name__ está ausente del objeto, existe solo dentro de las clases.


Si deseas encontrar la clase de un objeto en particular, puedes usar una función llamada type(), la cual es capaz (entre otras cosas) de encontrar una clase que se haya utilizado para crear instancias de cualquier objeto.

Observa el código en el editor, ejecútalo y compruébalo tu mismo."""

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

"""La salida del código es:

Output
Classy
Classy
Nota una sentencia como esta:


print(obj.__name__)
 
provocará un error.


__module__ es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.

Vamos a comprobarlo: ejecuta el código en el editor."""

class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)


"""La salida del código es:

Output
__main__
__main__
Como sabes, cualquier módulo llamado __main__ en realidad no es un módulo, sino es el archivo actualmente en ejecución.


___bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son superclases directas de la clase.

El orden es el mismo que el utilizado dentro de la definición de clase.

Te mostraremos solo un ejemplo muy básico, ya que queremos resaltar cómo funciona la herencia.

Además, te mostraremos cómo usar este atributo cuando discutamos los aspectos orientados a objetos de las excepciones.

Nota: solo las clases tienen este atributo, los objetos no.

Hemos definido una función llamada printBases(), diseñada para presentar claramente el contenido de la tupla.

Observa el código en el editor. Ejecútalo."""

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
"""La salida del código es:
Output
( object )
( object  )
( SuperOne SuperTwo )"""