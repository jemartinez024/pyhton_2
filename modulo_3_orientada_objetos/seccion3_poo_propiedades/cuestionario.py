"""
3.3.5 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuáles de las propiedades de la clase Python son variables de instancia y cuáles son variables de clase? ¿Cuáles de ellos son privados?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False
 
Ocultar
population y victims son variables de clase, mientras que length y __venomous son variables de instancia (esta última también es privada).

Pregunta 2: Vas a negar la propiedad __venomous del objeto version_2, ignorando el hecho de que la propiedad es privada. ¿Cómo vas a hacer esto?

version_2 = Python()
 
Ocultar
version_2._Python__venomous = not version_2._Python__venomous

Pregunta 3: Escribe una expresión que compruebe si el objeto version_2 contiene una propiedad de instancia denominada constrictor (¡si, constrictor!).

Ocultar
hasattr(version_2, 'constrictor')
    

"""