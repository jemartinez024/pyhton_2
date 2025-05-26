"""
2.6.3 RESUMEN DE SECCIÓN
1. Una excepción es un evento durante la ejecución del programa causado por una situación anormal. La excepción debe manejarse para evitar la terminación del programa. La parte del código que se sospecha que es la fuente de la excepción debe colocarse dentro del bloque try.

Cuando ocurre la excepción, la ejecución del código no se termina, sino que salta al bloque except. Este es el lugar donde debe llevarse a cabo el manejo de la excepción. El esquema general para tal construcción es el siguiente:


# El código que siempre corre suavemente
:
try:
    :
    # Código riesgoso.
    :
except:
    :
    # Aquí se maneja el error.
    :
:
# espalda a normal.
:
 
2. Si necesitas manejar más de una excepción proveniente del mismo bloque try, puedes agregar más de un bloque except, pero debes etiquetarlos con diferentes nombres, así:


# El código que siempre corre suavemente.
:
try:
    :
    # Código riesgoso.
    :
except Except_1:
    # Aquí se maneja el error.
except Except_2:
    # Hemos salvado al mundo aquí.
:
# espalda a normal.
:
 
En el mejor caso, se ejecuta uno de los bloques except; ninguno de los bloques se ejecuta cuando la excepción generada no coincide con ninguna de las excepciones especificadas.


3. No se puede agregar más de un bloque de excepción sin nombre después de los bloques con nombre.


# El código que siempre corre suavemente.
:
try:
    :
    # Código riesgoso.
    :
except Except_1:
    # Aquí se maneja el error.
except Except_2:
    # Hemos salvado al mundo aquí.
except:
    # Todo lo demás cae aquí.
:
# espalda a normal.
:
 """