"""3.5.5 Cómo Python encuentra propiedades y métodos
Ahora veremos como Python trata con los métodos de herencia.

Echa un vistazo al ejemplo en el editor."""

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)

"""Vamos a analizarlo:

Existe una clase llamada Super, que define su propio constructor utilizado para asignar la propiedad del objeto, llamada name.
La clase también define el método __str__(), lo que permite que la clase pueda presentar su identidad en forma de texto.
La clase se usa luego como base para crear una subclase llamadaSub. La clase Sub define su propio constructor, que invoca el de la superclase. Toma nota de como lo hemos hecho: Super.__init__(self, name).
Hemos nombrado explícitamente la superclase y hemos apuntado al método para invocar a __init__(), proporcionando todos los argumentos necesarios.
Hemos instanciado un objeto de la clase Sub y lo hemos impreso.
El código da como salida:

Output
Mi nombre es Andy.

Nota: Como no existe el método __str__() dentro de la clase Sub, la cadena a imprimir se producirá dentro de la clase Super. Esto significa que el método __str__() ha sido heredado por la clase Sub.


Mira el código en el editor. Lo hemos modificado para mostrarte otro método de acceso a cualquier entidad definida dentro de la superclase.

En el ejemplo anterior, nombramos explícitamente la superclase. En este ejemplo, hacemos uso de la función super(), la cual accede a la superclase sin necesidad de conocer su nombre:"""

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

"""En el último ejemplo, nombramos explícitamente la superclase. En este ejemplo, hacemos uso de la función super(), que accede a la superclase sin necesidad de saber su nombre:


super().__init__(name)
 
La función super() crea un contexto en el que no tiene que (además, no debe) pasar el argumento propio al método que se invoca; es por eso que es posible activar el constructor de la superclase utilizando solo un argumento.

Nota: puedes usar este mecanismo no solo para invocar al constructor de la superclase, pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.

Intentemos hacer algo similar, pero con propiedades (más precisamente con: variables de clase).

Observa el ejemplo en el editor."""

# Probando propiedades: variables de clase.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)