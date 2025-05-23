alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)



"""2.2.7 Las cadenas en Python son inmutables
También te hemos dicho que las cadenas de Python son inmutables. Esta es una característica muy importante. ¿Qué significa?

Esto significa principalmente que la similitud de cadenas y listas es limitada. No todo lo que puede hacerse con una lista puede hacerse con una cadena.

La primera diferencia importante no te permite usar la instrucción del para eliminar cualquier cosa de una cadena

El ejemplo siguiente no funcionará:

alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]
 
Lo único que puedes hacer con del y una cadena es eliminar la cadena como un todo. Intenta hacerlo.


Las cadenas de Python no tienen el método append() - no se pueden expander de ninguna manera.

El siguiente ejemplo es erróneo:

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")
 

Con la ausencia del método append(), el método insert() también es ilegal:

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")
 
No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.

La única consecuencia es que debes recordarlo e implementar tu código de una manera ligeramente diferente: observa el código en el editor."""

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)