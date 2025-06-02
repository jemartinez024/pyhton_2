"""3.4.4 Investigando Clases
¿Qué puedes descubrir acerca de las clases en Python? La respuesta es simple: todo.

Tanto la reflexión como la introspección permiten al programador hacer cualquier cosa con cada objeto, sin importar de dónde provenga.

Analiza el código en el editor."""


class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


"""La función llamada incIntsI() toma un objeto de cualquier clase, escanea su contenido para encontrar todos los atributos enteros con nombres que comienzan con i, y los incrementa en uno.

¿Imposible? ¡De ninguna manera!

Así es como funciona:

La línea 1: define una clase muy simple...
Las líneas 5 a la 11: ... la llenan con algunos atributos.
La línea 14: ¡esta es nuestra función!
La línea 15: escanea el atributo __dict__, buscando todos los nombres de atributos.
La línea 16: si un nombre comienza con i...
La línea 17: ... utiliza la función getattr() para obtener su valor actual; nota: getattr() toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y devuelve el valor del atributo actual.
La línea 18: comprueba si el valor es de tipo entero, emplea la función isinstance() para este propósito (discutiremos esto más adelante).
La línea 19: si la comprobación sale bien, incrementa el valor de la propiedad haciendo uso de la función setattr(); la función toma tres argumentos: un objeto, el nombre de la propiedad (como una cadena) y el nuevo valor de la propiedad.
El código da como salida:

Output
{'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
{'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}
¡Eso es todo!"""
