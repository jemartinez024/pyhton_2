"""
3.5.10 RESUMEN DE SECCIÓN
1. Un método llamado __str__() es responsable de convertir el contenido de un objeto en una cadena (más o menos) legible. Puedes redefinirlo si deseas que tu objeto pueda presentarse de una forma más elegante. Por ejemplo:


class Mouse:
    def __init__(self, name):
        self.my_name = name
 
 
    def __str__(self):
        return self.my_name
 
 
the_mouse = Mouse('mickey')
print(the_mouse) # Imprime "mickey".
 

2. Una función llamada issubclass(Class_1, Class_2) es capaz de determinar si Class_1 es una subclase de Class_2. Por ejemplo:


class Mouse:
    pass
 
 
class LabMouse(Mouse):
    pass
 
 
print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse)) # Imprime "False True
 

3. Una función llamada isinstance(Object, Class) comprueba si un objeto proviene de una clase indicada. Por ejemplo:


class Mouse:
    pass
 
 
class LabMouse(Mouse):
    pass
 
 
mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse)) # Imprime "True False".
 

4. Un operador llamado is comprueba si dos variables hacen referencia al mismo objeto. Por ejemplo:


class Mouse:
    pass
 
 
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey) # Imprime "False True".
 

5. Una función sin parámetros llamada super() retorna la referencia a la superclase más cercana de la clase. Por ejemplo:


class Mouse:
    def __str__(self):
        return "Mouse"
 
 
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
 
 
doctor_mouse = LabMouse();
print(doctor_mouse) # Imprime "Laboratory Mouse".
 

6. Los métodos, así como las variables de instancia y de clase definidas en una superclase son heredados automáticamente por sus subclases. Por ejemplo:


class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
 
    def __str__(self):
        return "Hola, mi nombre es " + self.name
 
class LabMouse(Mouse):
    tpass
 
professor_mouse = LabMouse("Profesor Mouse")
print(professor_mouse, Mouse.Population) # Imprime "Hola, mi nombre es Profesor Mouse 1"
 

7. Para encontrar cualquier propiedad de objeto/clase, Python la busca dentro:

Del objeto mismo.
Todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
Si existe más de una clase en una ruta de herencia en particular, Python las escanea de izquierda a derecha.
Si lo mencionado anteriormente falla, la excepción AttributeError es generada.

8. Si alguna de las subclases define un método, variable de clase o variable de instancia del mismo nombre que existe en la superclase, el nuevo nombre anula cualquiera de las instancias anteriores del nombre. Por ejemplo:


class Mouse:
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
    return "Mi nombre es " + self.name
 
class AncientMouse(Mouse):
    def __str__(self):
    return "Meum nomen est " + self.name
 
mus = AncientMouse("Caesar") # Imprime "Meum nomen est Caesar"
print(mus)
 
"""