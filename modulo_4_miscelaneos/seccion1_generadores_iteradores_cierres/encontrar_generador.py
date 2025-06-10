"""4.1.1 Generadores: donde encontrarlos

Generador - ¿Con qué asocias esta palabra? Quizás se refiere a algún dispositivo electrónico. O tal vez se refiere a una máquina pesada diseñada para producir energía eléctrica u otra cosa.

Un generador de Python es un fragmento de código especializado capaz de producir una serie de valores y controlar el proceso de iteración. Esta es la razón por la cual los generadores a menudo se llaman iteradores, y aunque hay quienes pueden encontrar una diferencia entre estos dos, aquí los trataremos como uno mismo."""

"""Puede que no te hayas dado cuenta, pero te has topado con generadores muchas, muchas veces antes. Echa un vistazo al fragmento de código:"""


for i in range(5):
    print(i)
    

"""La función range() es un generador, la cual también es un iterador.

¿Cuál es la diferencia?

Una función devuelve un valor bien definido, el cual, puede ser el resultado de una evaluación compleja, por ejemplo, de un polinomio, y se invoca una vez, solo una vez.

Un generador devuelve una serie de valores, y en general, se invoca (implícitamente) más de una vez.

En el ejemplo, el generador range() se invoca seis veces, proporcionando cinco valores de cero a cuatro, y finalmente señaliza que la serie está completa.

El proceso anterior es completamente transparente. Vamos a arrojar algo de luz sobre el. Vamos a mostrarte el protocolo iterador.

El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas impuestas por el contexto de las sentencias for e in. Un objeto conforme a estas reglas se llama iterador.

Un iterador debe proporcionar dos métodos:

__iter__() el cual debe devolver el objeto en sí y que se invoca una vez (es necesario para que Python inicie con éxito la iteración).
__next__() el cual debe devolver el siguiente valor (primero, segundo, etc). de la serie deseada: será invocado por las sentencias for/in para pasar a la siguiente iteración; si no hay más valores a proporcionar, el método deberá generar la excepción StopIteration.
¿Suena extraño? De ningúna manera. Mira el ejemplo en el editor."""


class Fib:
    def __init__(self, nn): 
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
    