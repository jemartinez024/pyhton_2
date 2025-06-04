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

"""Como puedes observar, la clase Super define una variable de clase llamada supVar, y la clase Sub define una variable llamada subVar.

Ambas variables son visibles dentro del objeto de clase Sub, es por ello que el código da como salida:

Output
2
1

El mismo efecto se puede observar con variables de instancia, observa el segundo ejemplo en el editor."""

# Probando propiedades: variables de instancia.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

"""El constructor de la clase Sub crea una variable de instancia llamada subVar, mientras que el constructor de Super hace lo mismo con una variable de nombre supVar. Al igual que el ejemplo anterior, ambas variables son accesibles desde el objeto de clase Sub.

La salida del programa es:

Output
12
11
Nota: La existencia de la variable supVar obviamente está condicionada por la invocación del constructor de la clase Super. Omitirlo daría como resultado la ausencia de la variable en el objeto creado (pruébalo tu mismo).


Ahora es posible formular una declaración general que describa el comportamiento de Python.

Cuando intentes acceder a una entidad de cualquier objeto, Python intentará (en este orden):


Encontrarla dentro del objeto mismo.
Encontrarla en todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
Si ambos intentos fallan, una excepción (AttributeError) será generada.


La primera condición puede necesitar atención adicional. Como sabes, todos los objetos derivados de una clase en particular pueden tener diferentes conjuntos de atributos, y algunos de los atributos pueden agregarse al objeto mucho tiempo después de la creación del objeto.

El ejemplo en el editor resume esto en una línea de herencia de tres niveles. Analízalo cuidadosamente."""

class Level1:
    variable_1 = 100 #  variable de clase
    def __init__(self): # constructor
        self.var_1 = 101 # variable de instancia

    def fun_1(self): # método
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())

"""Todos los comentarios que hemos hecho hasta ahora están relacionados con casos de herencia única, cuando una subclase tiene exactamente una superclase. Esta es la situación más común (y también la recomendada).

Python, sin embargo, ofrece mucho más aquí. En las próximas lecciones te mostraremos algunos ejemplos de herencia múltiple.

La herencia múltiple ocurre cuando una clase tiene más de una superclase. Sintácticamente, dicha herencia se presenta como una lista de superclases separadas por comas entre paréntesis después del nombre de la nueva clase, al igual que aquí:

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())
 

La clase Sub tiene dos superclases: SuperA y SuperB. Esto significa que la clase Sub hereda todos los bienes ofrecidos por ambas clases SuperA y SuperB.

El código imprime:

10 11
20 21

Ahora es el momento de introducir un nuevo término - overriding (anulación).

¿Qué crees que sucederá si más de una de las superclases define una entidad con un nombre en particular?


Analicemos el ejemplo en el editor."""


class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

"""Tanto la clase, Level1 y Level2 definen un método llamado fun() y una propiedad llamada var. ¿Significará esto el objeto de la claseLevel3 podrá acceder a dos copias de cada entidad? De ningún modo.

La entidad definida después (en el sentido de herencia) anula la misma entidad definida anteriormente. Es por eso que el código produce el siguiente resultado:

Output
200 201
Como puedes ver, la variable de clase var y el método fun() de la clase Level2 anula las entidades de los mismos nombres derivados de la clase Level1.

Esta característica se puede usar intencionalmente para modificar el comportamiento predeterminado de las clases (o definido previamente) cuando cualquiera de tus clases necesite actuar de manera diferente a su ancestro.

También podemos decir que Python busca una entidad de abajo hacia arriba y está completamente satisfecho con la primera entidad del nombre deseado que encuentra.

¿Qué ocurre cuando una clase tiene dos ancestros que ofrecen la misma entidad y se encuentran en el mismo nivel? En otras palabras, ¿Qué se debe esperar cuando surge una clase usando herencia múltiple? Miremos lo siguiente.

Echemos un vistazo al ejemplo en el editor."""

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Right, Left):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

"""La clase Sub hereda todos los bienes de dos superclases Left y Right (estos nombres están destinados a ser significativos).

No hay duda de que la variable de clase var_right proviene de la clase Right, y var_left proviene de la clase Left respectivamente.

Esto es claro. Pero, ¿De donde proviene la variable var? ¿Es posible adivinarlo? El mismo problema se encuentra con el método fun() - ¿Será invocada desde Left o desde Right? Ejecutemos el programa: la salida será:

Output
L LL RR Left
Esto prueba que ambos casos poco claros tienen una solución dentro de la clase Left. ¿Es esta una premisa suficiente para formular una regla general? Sí lo es.

Podemos decir que Python busca componentes de objetos en el siguiente orden:

Dentro del objeto mismo.
En sus superclases, de abajo hacia arriba.
Si hay más de una clase en una ruta de herencia, Python las escanea de izquierda a derecha.
¿Necesitas algo más? Simplemente haz una pequeña enmienda en el código, reemplaza:class Sub(Left, Right): con: class Sub(Right, Left):, luego ejecuta el programa nuevamente y observa qué sucede.

¿Qué ves ahora? Vemos:

Output
R LL RR Right
¿Ves lo mismo o algo diferente?"""