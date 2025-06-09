"""3.6.4 Cómo crear tu propia excepción
La jerarquía de excepciones no está cerrada ni terminada, y siempre puedes ampliarla si deseas o necesitas crear tu propio mundo poblado con tus propias excepciones.

Puede ser útil cuando se crea un módulo complejo que detecta errores y genera excepciones, y deseas que las excepciones se distingan fácilmente de cualquier otra de Python.

Esto se puede hacer al definir tus propias excepciones como subclases derivadas de las predefinidas.

Nota: si deseas crear una excepción que se utilizará como un caso especializado de cualquier excepción incorporada, derivala solo de esta. Si deseas construir tu propia jerarquía, y no quieres que esté estrechamente conectada al árbol de excepciones de Python, derivala de cualquiera de las clases de excepción principales, tal como: Exception.

Imagina que has creado una aritmética completamente nueva, regida por sus propias leyes y teoremas. Está claro que la división también se ha redefinido, y tiene que comportarse de una manera diferente a la división de rutina. También está claro que esta nueva división debería plantear su propia excepción, diferente de la incorporada ZeroDivisionError, pero es razonable suponer que, en algunas circunstancias, tu (o el usuario de tu aritmética) pueden tratar todas las divisiones entre cero de la misma manera.

Demandas como estas pueden cumplirse en la forma presentada en el editor."""

class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("peores noticias")
    else:		
        raise ZeroDivisionError("malas noticias")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('División entre cero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('Mi división entre cero')
    except ZeroDivisionError:
        print('División entre cero original')
    
    
""""Mira el código y analicémoslo:

Hemos definido nuestra propia excepción, llamada MyZeroDivisionError, derivada de la incorporada ZeroDivisionError. Como puedes ver, hemos decidido no agregar ningún componente nuevo a la clase.

En efecto, una excepción de esta clase puede ser, dependiendo del punto de vista deseado, tratada como una simple excepción ZeroDivisionError, o puede ser considerada por separado.

La función do_the_division() genera una excepción MyZeroDivisionError o ZeroDivisionError dependiendo del valor del argumento.

La función se invoca cuatro veces en total, mientras que las dos primeras invocaciones se manejan utilizando solo un bloque except (la más general), las dos últimas invocan dos bloques diferentes, capaces de distinguir las excepciones (no lo olvides: el orden de los bloques hace una diferencia fundamental).

Cuando vas a construir un universo completamente nuevo lleno de criaturas completamente nuevas que no tienen nada en común con todas las cosas familiares, es posible que desees construir tu propia estructura de excepciones.

Por ejemplo, si trabajas en un gran sistema de simulación destinado a modelar las actividades de un restaurante de pizza, puede ser conveniente formar una jerarquía de excepciones por separado.

Puedes comenzar a construirla definiendo una excepción general como una nueva clase base para cualquier otra excepción especializada. Lo hemos hecho de la siguiente manera:



class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza
 

p>Nota: vamos a recopilar más información específica aquí de lo que recopila una Excepción regular, entonces nuestro constructor tomará dos argumentos:
Uno que especifica una pizza como tema del proceso.
Otro que contiene una descripción más o menos precisa del problema.
Como puedes ver, pasamos el segundo parámetro al constructor de la superclase y guardamos el primero dentro de nuestra propiedad.

Un problema más específico (como un exceso de queso) puede requerir una excepción más específica. Es posible derivar la nueva clase de la ya definida PizzaError, como hemos hecho aquí:


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese
 

La excepción TooMuchCheeseError necesita más información que la excepción regular PizzaError, así que lo agregamos al constructor, el nombre cheese es entonces almacenado para su posterior procesamiento.


Mira el código en el editor. Combinamos las dos excepciones previamente definidas y las aprovechamos para que funcionen en un pequeño ejemplo."""


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no existe tal pizza en el menú")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "demasiado queso")
    print("¡Pizza lista!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
        
"""Una de ellas es generada dentro de la función make_pizza() cuando ocurra cualquiera de estas dos situaciones erróneas: una solicitud de pizza incorrecta o una solicitud de una pizza con demasiado queso.

Nota:

El remover el bloque que comienza con except TooMuchCheeseError hará que todas las excepciones que aparecen se clasifiquen como PizzaError.
El remover el bloque que comienza con except PizzaError provocará que la excepción TooMuchCheeseError no pueda ser manejada, y hará que el programa finalice.

La solución anterior, aunque elegante y eficiente, tiene una debilidad importante. Debido a la manera algo fácil de declarar los constructores, las nuevas excepciones no se pueden usar tal cual, sin una lista completa de los argumentos requeridos.

Eliminaremos esta debilidad estableciendo valores predeterminados para todos los parámetros del constructor. Observa:

class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza
 
 
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
 
 
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("¡Pizza lista!")
 
 
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
 

Ahora, si las circunstancias lo permiten, es posible usar únicamente los nombres de clase."""