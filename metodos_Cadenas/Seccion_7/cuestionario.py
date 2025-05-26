"""
2.7.3 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuál es la salida esperada del siguiente código?

try:
    print(1/0)
except ZeroDivisionError:
    print("cero")
except ArithmeticError:
    print("arit")
except:
    print("algo")
 
Ocultar
cero
Pregunta 2: ¿Cuál es la salida esperada del siguiente código?

try:
    print(1/0)
except ArithmeticError:
    print("arit")
except ZeroDivisionError:
    print("cero")
except:
    print("algo")
 
Ocultar
arit
Pregunta 3: ¿Cuál es la salida esperada del siguiente código?

def foo(x):
    assert x
    return 1/x
 
 
try:
    print(foo(0))
except ZeroDivisionError:
    print("cero")
except:
    print("algo")
 
Ocultar
algo
"""