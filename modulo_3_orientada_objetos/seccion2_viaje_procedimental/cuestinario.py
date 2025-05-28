"""
3.2.7 CUESTIONARIO DE SECCIÓN
Pregunta 1: Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.

Ocultar
class Python(Snakes):
    
Pregunta 2: Algo falta en la siguiente declaración, ¿qué es?

class Snakes:
    def __init__():
        self.sound = 'Sssssss'
 
Ocultar
El constructor __init__() carece del parámetro obligatorio (deberíamos llamarlo self para cumplir con los estándares).

Pregunta 3: Modifica el código para garantizar que la propiedad venomous sea privada.

class Snakes:
    def __init__(self):
        self.venomous = True
 
Ocultar
El código debe verse de la siguiente manera:

class Snakes:
    def __init__(self):
        self.__venomous = True
"""