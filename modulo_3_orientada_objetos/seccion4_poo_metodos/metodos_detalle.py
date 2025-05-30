"""3.4.1 Métodos a detalle
Resumamos todos los hechos relacionados con el uso de métodos en las clases de Python.

Como ya sabes, un método es una función que está dentro de una clase.

Existe un requisito fundamental: un método está obligado a tener al menos un parámetro (no existen métodos sin parámetros; un método puede invocarse sin un argumento, pero no puede declararse sin parámetros).

El primer (o único) parámetro generalmente se denomina self. Te sugerimos que lo sigas nombrando de esta manera, darle otros nombres puede causar sorpresas inesperadas.

El nombre self sugiere el propósito del parámetro: identifica el objeto para el cual se invoca el método.

Si vas a invocar un método, no debes pasar el argumento para el parámetro self, Python lo configurará por ti.

El ejemplo en el editor muestra la diferencia."""

class Classy:
    def method(self):
        print("método")


obj = Classy()
obj.method()

"""El código da como salida:

método
Output
Toma en cuenta la forma en que hemos creado el objeto, hemos tratado el nombre de la clase como una función, y devuelve un objeto recién instanciado de la clase.

Si deseas que el método acepte parámetros distintos a self, debes:

Colocarlos después de self en la definición del método.
Pasarlos como argumentos durante la invocación sin especificar self.
Justo como aqui:


class Classy:
    def method(self, par):
        print("método:", par)
 
 
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)
 
El código da como salida:

método: 1
método: 2
método: 3
Output

El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.


class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
 
obj = Classy()
obj.var = 3
obj.method()
 
El código da como salida:

2 3
Output

El parámetro self también se usa para invocar otros métodos desde dentro de la clase.

Justo como aquí:


class Classy:
    def other(self):
        print("otro")
 
    def method(self):
        print("método")
        self.other()
 
 
obj = Classy()
obj.method()
 
El código da como salida:
método
otro
Output

Si se nombra un método de esta manera: __init__, no será un método regular, será un constructor.

Si una clase tiene un constructor, este se invoca automática e implícitamente cuando se instancia el objeto de la clase.

El constructor:

Esta obligado a tener el parámetro self (se configura automáticamente).
Pudiera (pero no necesariamente) tener mas parámetros que solo self; si esto sucede, la forma en que se usa el nombre de la clase para crear el objeto debe tener la definición __init__.
Se puede utilizar para configurar el objeto, es decir, inicializa adecuadamente su estado interno, crea variables de instancia, crea instancias de cualquier otro objeto si es necesario, etc.
Observa el código en el editor. El ejemplo muestra un constructor muy simple pero funcional."""

class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("objeto")

print(obj_1.var)
    