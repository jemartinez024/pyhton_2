"""3.5.6 Cómo construir una jerarquía de clases
Construir una jerarquía de clases no es solo por amor al arte.

Si divides un problema entre las clases y decides cual de ellas debe ubicarse en la parte superior y cual debe ubicarse en la parte inferior de la jerarquía, debes analizar cuidadosamente el problema, pero antes de mostrarte como hacerlo (y como no hacerlo), queremos resaltar un efecto interesante. No es nada extraordinario (es solo una consecuencia de las reglas generales presentadas anteriormente), pero recordarlo puede ser clave para comprender como funcionan algunos códigos y cómo se puede usar este efecto para construir un conjunto flexible de clases.

Echa un vistazo al código en el editor."""

class One:
    def do_it(self):
        print("do_it de One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it de Two")


one = One()
two = Two()

one.doanything()
two.doanything()


"""Analicémoslo:

Existen dos clases llamadas One y Two, se entiende que Two es derivada de One. Nada especial. Sin embargo, algo es notable: el método do_it().
El método do_it() está definido dos veces: originalmente dentro de One posteriormente dentro de Two. La esencia del ejemplo radica en el hecho de que es invocado solo una vez dentro de One.
La pregunta es: ¿cuál de los dos métodos será invocado por las dos últimas líneas del código?


La primera invocación parece ser simple, el invocar el método doanything() del objeto llamado one obviamente activará el primero de los métodos.

La segunda invocación necesita algo de atención. También es simple si tienes en cuenta cómo Python encuentra los componentes de la clase. La segunda invocación ejecutará el método do_it() en la forma existente dentro de la clase Two, independientemente del hecho de que la invocación se lleva a cabo dentro de la clase One.

En efecto, el código genera el siguiente resultado:

Output
do_it de One
do_it de Two
Nota: la situación en la cual la subclase puede modificar el comportamiento de su superclase (como en el ejemplo) se llama poliformismo. La palabra proviene del griego (polys: "muchos, mucho" y morphe, "formas, forma"), lo que significa que una misma clase puede tomar varias formas dependiendo de las redefiniciones realizadas por cualquiera de sus subclases.

El método, redefinido en cualquiera de las superclases, que cambia el comportamiento de la superclase, se llama virtual.

En otras palabras, ninguna clase se da por hecho. El comportamiento de cada clase puede ser modificado en cualquier momento por cualquiera de sus subclases.

Te mostraremos como usar el poliformismo para extender la flexibilidad de la clase.


Mira el ejemplo en el editor."""

import time

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)
        
        
"""¿Se parece a algo? Sí, por supuesto que lo hace. Se refiere al ejemplo que se muestra al comienzo del módulo cuando hablamos de los conceptos generales de la programación orientada a objetos.

Puede parecer extraño, pero no utilizamos herencia en este ejemplo, solo queríamos mostrarte que no nos limita.

Definimos dos clases separadas capaces de producir dos tipos diferentes de vehículos terrestres. La principal diferencia entre ellos está en cómo giran. Un vehículo con ruedas solo gira las ruedas delanteras (generalmente). Un vehículo con pistas tiene que detener una de las pistas.

¿Puedes seguir el código?

Un vehículo con pistas realiza un giro deteniéndose y moviéndose en una de sus pistas (esto lo hace el método control_track() el cual se implementará más tarde).
Un vehículo con ruedas gira cuando sus ruedas delanteras giran (esto lo hace el método turn_front_wheels()).
El método turn() utiliza el método adecuado para cada vehículo en particular.
¿Puedes detectar el error del código?

Los métodos turn() son muy similares como para dejarlos en esta forma.

Vamos a reconstruir el código: vamos a presentar una superclase para reunir todos los aspectos similares de los vehículos, trasladando todos los detalles a las subclases.

Mira el código en el editor nuevamente."""


"""import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)"""
        
"""Esto es lo que hemos hecho:

Definimos una superclase llamada Vehicle, la cual utiliza el método turn() para implementar un esquema para poder girar, mientras que el giro en si es realizado por change_direction(); nota: dicho método está vacío, ya que vamos a poner todos los detalles en la subclase (dicho método a menudo se denomina método abstracto, ya que solo demuestra alguna posibilidad que será instanciada más tarde).
Definimos una subclase llamada TrackedVehicle (nota: es derivada de la clase Vehicle) la cual instancia el método change_direction() utilizando el método denominado control_track().
Respectivamente, la subclase llamada WheeledVehicle hace lo mismo, pero usa el método turn_front_wheels() para obligar al vehículo a girar.
La ventaja más importante (omitiendo los problemas de legibilidad) es que esta forma de código te permite implementar un nuevo algoritmo de giro simplemente modificando el método turn(), lo cual se puede hacer en un solo lugar, ya que todos los vehículos lo obedecerán.

Así es como el el poliformismo ayuda al desarrollador a mantener el código limpio y consistente.

La herencia no es la única forma de construir clases adaptables. Puedes lograr los mismos objetivos (no siempre, pero muy a menudo) utilizando una técnica llamada composición.

La composición es el proceso de componer un objeto usando otros objetos diferentes. Los objetos utilizados en la composición entregan un conjunto de rasgos deseados (propiedades y/o métodos), podemos decir que actúan como bloques utilizados para construir una estructura más complicada.

Puede decirse que:

La herencia extiende las capacidades de una clase agregando nuevos componentes y modificando los existentes; en otras palabras, la receta completa está contenida dentro de la clase misma y todos sus ancestros; el objeto toma todas las pertenencias de la clase y las usa.
La composición proyecta una clase como contenedor capaz de almacenar y usar otros objetos (derivados de otras clases) donde cada uno de los objetos implementa una parte del comportamiento de una clase.
Permítenos ilustrar la diferencia usando los vehículos previamente definidos. El enfoque anterior nos condujo a una jerarquía de clases en la que la clase más alta conocía las reglas generales utilizadas para girar el vehículo, pero no sabía cómo controlar los componentes apropiados (ruedas o pistas).

Las subclases implementaron esta capacidad mediante la introducción de mecanismos especializados. Hagamos (casi) lo mismo, pero usando composición. La clase, como en el ejemplo anterior, sabe cómo girar el vehículo, pero el giro real lo realiza un objeto especializado almacenado en una propiedad llamada controlador. El controlador es capaz de controlar el vehículo manipulando las partes relevantes del vehículo.

Echa un vistazo al editor: así es como podría verse."""

import time

class Tracks:
    def change_direction(self, left, on):
        print("pistas: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("ruedas: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

"""Existen dos clases llamadas Tracks y Wheels, ellas saben como controlar la dirección del vehículo. También hay una clase llamada Vehicle que puede usar cualquiera de los controladores disponibles (los dos ya definidos o cualquier otro definido en el futuro): el controlador se pasa a la clase durante la inicialización.

De esta manera, la capacidad de giro del vehículo se compone de un objeto externo, no implementado dentro de la clase Vehicle.

En otras palabras, tenemos un vehículo universal y podemos instalar pistas o ruedas en él.

El código produce el siguiente resultado:

Output
ruedas:  True True
ruedas:  True False
pistas:  False True
pistas:  False False"""