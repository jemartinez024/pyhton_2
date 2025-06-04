"""3.5.4 El operador is
También existe un operador de Python que vale la pena mencionar, ya que se refiere directamente a los objetos - aquí está:

object_one is object_two
 
El operador is verifica si dos variables, en este caso (object_one y object_two) se refieren al mismo objeto.

No olvides que las variables no almacenan los objetos en sí, sino solo los identificadores que apuntan a la memoria interna de Python.

Asignar un valor de una variable de objeto a otra variable no copia el objeto, sino solo su identificador. Es por ello que un operador como is puede ser muy útil en ciertas circunstancias.

Echa un vistazo al código en el editor."""

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2) #false
print(object_2 is object_3) #false
print(object_3 is object_1) #true
print(object_1.val, object_2.val, object_3.val) # 1 2 1

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2) # True False
# El operador is verifica si string_1 y string_2 son el mismo objeto, lo cual es falso, a pesar de que su contenido es el mismo.

"""Analicémoslo:

Existe una clase muy simple equipada con un constructor simple, que crea una sola propiedad. La clase se usa para instanciar dos objetos. El primero se asigna a otra variable, y su propiedad val se incrementa en uno.
Luego, el operador is se aplica tres veces para verificar todos los pares de objetos posibles, y todos los valores de la propiedad val son mostrados en pantalla.
La última parte del código lleva a cabo otro experimento. Después de tres tareas, ambas cadenas contienen los mismos textos, pero estos textos se almacenan en diferentes objetos.
El código imprime:

Output
False
False
True
1 2 1
True False

Los resultados prueban que object_1 y object_3 son en realidad los mismos objetos, mientras que string_1 y string_2 no lo son, a pesar de que su contenido sea el mismo."""