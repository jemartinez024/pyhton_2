# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))


print('kappa'.find('a', 2))

"""Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición, puedes usar una variante de dos parámetros del método find(). Mira el ejemplo:


print('kappa'.find('a', 2))
 
El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).

De las dos letras a, solo se encontrará la segunda. Ejecuta el código y verifica."""

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    
"""El código imprime los índices de todas las ocurrencias del artículo the, y su salida se ve así:

15
80
198
221
238"""


print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

"""El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).

Por lo tanto, las salidas de ejemplo son:

1
-1
Output
(a no se puede encontrar dentro de los límites de búsqueda dados en el segundo print())."""