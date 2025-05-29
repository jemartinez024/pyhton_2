"""3.3.2 Variables de clase
Una variable de clase es una propiedad que existe en una sola copia y se almacena fuera de cualquier objeto.

Nota: no existe una variable de instancia si no hay ningún objeto de la clase; solo existe una variable de clase en una copia, incluso si no hay objetos en la clase.

Las variables de clase se crean de manera diferente. El ejemplo te dirá más:"""

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
 
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
 

"""Observa:

Hay una asignación en la primera linea de la definición de clase: establece la variable denominada counter a 0; inicializando la variable dentro de la clase pero fuera de cualquiera de sus métodos hace que la variable sea una variable de clase.
El acceder a dicha variable tiene el mismo aspecto que acceder a cualquier atributo de instancia; está en el cuerpo del constructor; como puedes ver, el constructor incrementa la variable en uno; en efecto, la variable cuenta todos los objetos creados.
Ejecutar el código provocará el siguiente resultado:

{'_ExampleClass__first': 1} 3
{'_ExampleClass__first': 2} 3
{'_ExampleClass__first': 4} 3
Output
Dos conclusiones importantes se pueden sacar del ejemplo:

Las variables de clase no se muestran en el diccionario de un objeto __dict__ (esto es natural ya que las variables de clase no son partes de un objeto), pero siempre puedes intentar buscar en la variable del mismo nombre, pero a nivel de clase, te mostraremos esto muy pronto.
Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).
El cambiar el nombre de una variable de clase tiene los mismos efectos que aquellos con los que ya está familiarizado.

Mira el ejemplo en el editor. ¿Puedes adivinar su salida?"""

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

"""Ejecuta el programa y verifica si tus predicciones fueron correctas. Todo funciona como se esperaba, ¿no?

Hemos dicho antes que las variables de clase existen incluso cuando no se creó ninguna instancia de clase (objeto).

Ahora aprovecharemos la oportunidad para mostrarte la diferencia entre estas dos variables __dict__, la de la clase y la del objeto.

Observa el código en el editor. La prueba está ahí."""

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)

"""Echemos un vistazo más de cerca:

Definimos una clase llamada ExampleClass.

La clase define una variable de clase llamada varia.

El constructor de la clase establece la variable con el valor del parámetro.

Nombrar la variable es el aspecto más importante del ejemplo porque:
El cambiar la asignación a self.varia = val crearía una variable de instancia con el mismo nombre que la de la clase.
El cambiar la asignación a varia = val operaría en la variable local de un método; (te recomendamos probar los dos casos anteriores; esto te facilitará recordar la diferencia).
La primera línea del código fuera de la clase imprime el valor del atributo ExampleClass.varia. Nota: utilizamos el valor antes de instanciar el primer objeto de la clase.
Ejecuta el código en el editor y verifica su salida.

Como puedes ver __dict__ contiene muchos más datos que la contraparte de su objeto. La mayoría de ellos son inútiles ahora, el que queremos que verifiques cuidadosamente muestra el valor actual de varia.

Nota que el __dict__ del objeto está vacío, el objeto no tiene variables de instancia."""