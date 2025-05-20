"""
2.6.4 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuál es el resultado esperado del siguiente código?

try:
    print("Vamos a intentar esto.")
    print("#"[2])
    print("¡Tuvimos éxito!")
except:
    print("Hemos fallado.")
print("Hemos terminado.")
 
Ocultar
Vamos a intentar esto
Hemos fallado
Hemos terminado
Pregunta 2: ¿Cuál es el resultado esperado del siguiente código?

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("cero")
except IndexingError:
    print("índice")
except:
    print("algo")
 
Ocultar
cero
"""