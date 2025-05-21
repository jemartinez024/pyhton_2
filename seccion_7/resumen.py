"""
2.7.2 RESUMEN DE SECCIÓN
1. No se puede agregar más de un bloque except sin nombre (anónimo) después de los bloques con nombre.


# El código que siempre se ejecuta sin problemas.
:
try:
    :
    # Código riesgoso.
    :
except Except_1:
    # Aquí se maneja el problema.
except Except_2:
    # Aquí salvamos al mundo.
except:
    # Todo lo demás cae aquí.
:
# espalda a normal.
:
 

2. Todas las excepciones de Python predefinidas forman una jerarquía, es decir, algunas de ellas son más generales (la llamada BaseException es la más general) mientras que otras son más o menos concretas (por ejemplo, IndexError es más concreta que LookupError).

No debes poner excepciones más concretas antes de las más generales dentro de la misma secuencia de bloques except. Por ejemplo, puedes hacer esto:


try:
    # Código riesgoso.
except IndexError:
    # Solucionando problemas con listas.
except LookupError:
    # Lidiando con búsquedas erróneas.
 
Pero no hagas esto (a menos de que estés absolutamente seguro de que quieres que alguna parte de tu código sea inaccesible).


try:
    # Código riesgoso.
except LookupError:
    # Lidiando con búsquedas erróneas.
except IndexError:
     nunca llegarás aquí
 

3. La sentencia de Python raise NombreDeExcepción puede generar una excepción bajo demanda. La misma sentencia pero sin NombreDeExcepción, se puede usar solamente dentro del bloque except, y genera la misma excepción que se está manejando actualmente.


4. La sentencia de Python assert expression evalúa la expresión y genera la excepción AssertError cuando la expresión es igual a cero, una cadena vacía o None. Puedes usarla para proteger algunas partes críticas de tu código de datos devastadores.

"""