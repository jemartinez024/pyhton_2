"""4.1.7 Lambdas y la función map()
En el más simple de todos los casos posibles, la función map():


map(function, list)
 

Toma dos argumentos:

Una función.
Una lista.
La descripción anterior está extremadamente simplificada, ya que:

El segundo argumento map() puede ser cualquier entidad que se pueda iterar (por ejemplo, una tupla o un generador).
map() puede aceptar más de dos argumentos.
La función map() aplica la función pasada por su primer argumento a todos los elementos de su segundo argumento y devuelve un iterador que entrega todos los resultados de funciones subsequentes.

Puedes usar el iterador resultante en un bucle o convertirlo en una lista usando la función list().

¿Puedes ver un papel para una lambda aquí?

Observa el código en el editor: hemos usado dos lambdas en él."""

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    