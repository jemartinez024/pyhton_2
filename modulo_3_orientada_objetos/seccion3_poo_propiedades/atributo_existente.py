"""3.3.3 Comprobando la existencia de un atributo
La actitud de Python hacia la instanciación de objetos plantea una cuestión importante: en contraste con otros lenguajes de programación, es posible que no esperes que todos los objetos de la misma clase tengan los mismos conjuntos de propiedades.

Justo como en el ejemplo en el editor. Míralo cuidadosamente."""

"""class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)"""


"""El objeto creado por el constructor solo puede tener uno de los dos atributos posibles: a o b.

La ejecución del código producirá el siguiente resultado:

1
Traceback (most recent call last):
  File ".main.py", line 11, in
    print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'
Output
Como puedes ver, acceder a un atributo de objeto (clase) no existente genera una excepción AttributeError.

La instrucción try-except te brinda la oportunidad de evitar problemas con propiedades inexistentes.

Es fácil: mira el código en el editor."""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

"""Como puedes ver, esta acción no es muy sofisticada. Esencialmente, acabamos de barrer el tema debajo de la alfombra.

Afortunadamente, hay una forma más de hacer frente al problema.


Python proporciona una función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica. La función se llama hasattr, y espera que le pasen dos argumentos:

La clase o el objeto que se verifica.
El nombre de la propiedad cuya existencia se debe informar (Nota: debe ser una cadena que contenga el nombre del atributo).
La función retorna True o False.

Así es como puedes utilizarla:

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
 
 
example_object = ExampleClass(1)
print(example_object.a)
 
if hasattr(example_object, 'b'):
    print(example_object.b)
 
No olvides que la función hasattr() también puede operar en clases. Puedes usarla para averiguar si una variable de clase está disponible, como en el ejemplo en el editor.

La función devuelve True si la clase especificada contiene un atributo dado, y False de lo contrario.

¿Puedes adivinar la salida del código? Ejecútalo para verificar tus conjeturas."""

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))



"""Un ejemplo más: analiza el código a continuación e intenta predecir su salida:"""


class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
 
 
example_object = ExampleClass()
 
print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
 
"""¿Tuviste éxito? Ejecuta el código para verificar tus predicciones.

Bien, hemos llegado al final de esta sección. En la siguiente sección vamos a hablar sobre los métodos, ya que los métodos dirigen los objetos y los activan."""