"""3.3.3 Comprobando la existencia de un atributo
La actitud de Python hacia la instanciación de objetos plantea una cuestión importante: en contraste con otros lenguajes de programación, es posible que no esperes que todos los objetos de la misma clase tengan los mismos conjuntos de propiedades.

Justo como en el ejemplo en el editor. Míralo cuidadosamente."""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)