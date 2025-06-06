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
    