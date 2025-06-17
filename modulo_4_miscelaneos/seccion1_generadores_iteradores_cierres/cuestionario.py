"""
4.1.11 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuál es el resultado esperado del siguiente código?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Sí, sabemos que y no siempre se considera una vocal.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
 
Ocultar
a e i o u y

Pregunta 2: Escribe una función lambda, estableciendo a 1 su argumento entero, y aplícalo a la función map() para producir la cadena 1 3 3 5 en la consola.

any_list = [1, 2, 3, 4]
even_list = # Completa la línea aquí.
print(even_list)
 
Ocultar
list(map(lambda n: n | 1, any_list))
    

Pregunta 3: ¿Cuál es el resultado esperado del siguiente código?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))
 
Ocultar
And*Now*for*Something*Completely*Different


  NOTA  
PEP 8, la Guía de Estilo para Código Python, recomienda que las funciones lambdas no deben asignarse a variables, sino que deben definirse como funciones.

Esto significa que es mejor utilizar una sentencia def, y evita usar una sentencia de asignación que vincule una expresión lambda a un identificador. Analiza el código a continuación:


# Recomendado:
def f(x): return 3*x
 
 
# No recomendado:
f = lambda x: 3*x
 

La vinculación de lambdas a identificadores generalmente duplica la funcionalidad de la declaración def. El uso de sentencias def, por otro lado, genera más líneas de código.

Es importante comprender que a la realidad a menudo le gusta dibujar sus propios escenarios, que no necesariamente siguen las convenciones o recomendaciones formales. Si decides seguirlos o no, dependerá de muchas cosas: tus preferencias, otras convenciones adoptadas, las pautas internas de la empresa, la compatibilidad con el código existente, etc. Toma en cuenta esto.


"""

any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)
 

