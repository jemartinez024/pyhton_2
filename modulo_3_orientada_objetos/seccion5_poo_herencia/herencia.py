"""3.5.1 Herencia: ¿por qué y cómo?
Antes de comenzar a hablar sobre la herencia, queremos presentar un nuevo y práctico mecanismo utilizado por las clases y los objetos de Python: es la forma en que el objeto puede presentarse a si mismo.

Comencemos con un ejemplo. Observa el código en el editor."""

"""class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)"""

"""El programa imprime solo una línea de texto, que en nuestro caso es:

Output
<__main__.Star object at 0x7f1074cc7c50>
Si ejecutas el mismo código en tu computadora, verás algo muy similar, aunque el número hexadecimal (la subcadena que comienza con 0x) será diferente, ya que es solo un identificador de objeto interno utilizado por Python, y es poco probable que aparezca igual cuando se ejecuta el mismo código en un entorno diferente.

Como puedes ver, la impresión aquí no es realmente útil, y algo más específico, es preferible.

Afortunadamente, Python ofrece tal función.

Cuando Python necesita que alguna clase u objeto deba ser presentado como una cadena (es recomendable colocar el objeto como argumento en la invocación de la función print()), intenta invocar un método llamado __str__() del objeto y emplear la cadena que devuelve.

El método por default __str__() devuelve la cadena anterior: fea y poco informativa. Puedes cambiarlo definiendo tu propio método.

Lo acabamos de hacer: observa el código en el editor."""

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' en ' + self.galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)

"""El método nuevo __str__() genera una cadena que consiste en los nombres de la estrella y la galaxia, nada especial, pero los resultados de impresión se ven mejor ahora, ¿no?

¿Puedes adivinar la salida? Ejecuta el código para verificar si tenías razón.

El término herencia es más antiguo que la programación de computadoras, y describe la práctica común de pasar diferentes bienes de una persona a otra después de la muerte de esa persona. El término, cuando se relaciona con la programación de computadoras, tiene un significado completamente diferente.

Definamos el término para nuestros propósitos:

La herencia es una práctica común (en la programación de objetos) de pasar atributos y métodos de la superclase (definida y existente) a una clase recién creada, llamada subclase.

En otras palabras, la herencia es una forma de construir una nueva clase, no desde cero, sino utilizando un repertorio de rasgos ya definido. La nueva clase hereda (y esta es la clave) todo el equipamiento ya existente, pero puedes agregar algo nuevo si es necesario.

Gracias a eso, es posible construir clases más especializadas (más concretas) utilizando algunos conjuntos de reglas y comportamientos generales predefinidos.

El factor más importante del proceso es la relación entre la superclase y todas sus subclases (nota: si B es una subclase de A y C es una subclase de B, esto también significa que C es una subclase de A, ya que la relación es totalmente transitiva).

Aquí se presenta un ejemplo muy simple de herencia de dos niveles:


class Vehicle:
    pass
 
 
class LandVehicle(Vehicle):
    pass
 
 
class TrackedVehicle(LandVehicle):
    pass
 
Todas las clases presentadas están vacías por ahora, ya que te mostraremos cómo funcionan las relaciones mutuas entre las superclases y las subclases. Las llenaremos con contenido pronto.

Podemos decir que:

La clase Vehicle es la superclase para clases LandVehicle y TrackedVehicle.
La clase LandVehicle es una subclase de Vehicle y la superclase de TrackedVehicle al mismo tiempo.
La clase TrackedVehicle es una subclase tanto de Vehicle y LandVehicle.
El conocimiento anterior proviene de la lectura del código (en otras palabras, lo sabemos porque podemos verlo).

¿Python sabe lo mismo? ¿Es posible preguntarle a Python al respecto? Sí lo es."""