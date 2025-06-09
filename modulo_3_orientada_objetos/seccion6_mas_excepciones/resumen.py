"""
3.6.5 RESUMEN DE SECCIÓN
1. El bloque else: de la sentencia try se ejecuta cuando no ha habido ninguna excepción durante la ejecución del try:.


2. El bloque finally: de la sentencia try es siempre executado.


3. La sintaxis except Exception_Name as exception_object: te permite interceptar un objeto que contiene información sobre una excepción pendiente. La propiedad del objeto llamada args (una tupla) almacena todos los argumentos pasados al constructor del objeto.


4. Las clases de excepciones pueden extenderse para enriquecerlas con nuevas capacidades o para adoptar sus características a excepciones recién definidas.


    try:
        assert __name__ == "__main__"
    except:
        print("fallido", end=' ')
    else:
        print("éxito", end=' ')
    finally:
        print("terminado")
 

El código da como salida: éxito terminado."""