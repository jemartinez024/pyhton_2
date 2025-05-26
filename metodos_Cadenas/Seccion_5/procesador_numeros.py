"""El tercer programa muestra un método simple que permite ingresar una línea llena de números y sumarlos fácilmente. Nota: la función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito.

El procesamiento será extremadamente fácil: queremos que se sumen los números.

Observa el código en el editor. Analicémoslo.

El emplear listas por comprensión puede hacer que el código sea más pequeño. Puedes hacerlo si quieres.

Presentemos nuestra versión:"""

#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split() #divide la línea en una lista con subcadenas.
total = 0 #se inicializa la suma total a cero
try: #como la conversión de cadena a flotante puede generar una excepción, es mejor continuar con la protección del bloque try-except.
    for substr in strings: #itera a través de la lista...
        total += float(substr) # ... e intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
    print("El total es:", total) #todo está bien hasta ahora, así que imprime la suma.
except:
    print(substr, "no es un numero.") #imprime un mensaje de diagnóstico que muestra al usuario el motivo de la falla.
    
