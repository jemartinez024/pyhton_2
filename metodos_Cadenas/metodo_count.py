# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))


"""El método count()
El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema.

Observa el segundo ejemplo en el editor. ¿Puedes adivinar su salida?"""


"""
2.2.9 RESUMEN DE SECCIÓN
1. Las cadenas de Python son secuencias inmutables y se pueden indexar, dividir e iterar como cualquier otra secuencia, además de estar sujetas a los operadores in y not in. Hay dos tipos de cadenas en Python:

cadenas de una línea, que no pueden cruzar los límites de las líneas; las denotamos usando apóstrofes ('cadena') o comillas (“cadena”)
cadenas de varias líneas, que ocupan más de una línea de código fuente, delimitadas por trígrafos:
'''
cadena
'''

u

"""

"""

2. La longitud de una cadena está determinada por la función len(). El carácter de escape (\) no se cuenta. Por ejemplo:


print(len("\n\n"))
 
Su salida es 2.

3. Las cadenas pueden ser concatenadas usando el operador +, y replicadas usando el operador *. Por ejemplo:


asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
 
Su salida es *+*+*+*+*.

4. El par de funciones chr() y ord() se pueden utilizar para crear un carácter utilizando su punto de código y para determinar un punto de código correspondiente a un carácter. Las dos expresiones siguientes son siempre verdaderas:


chr(ord(character)) == character
ord(chr(codepoint)) == codepoint
 

5. Algunas otras funciones que se pueden aplicar a cadenas son:

list() - crea una lista que consta de todos los caracteres de la cadena.
max() - encuentra el carácter con el punto de código máximo.
min() - encuentra el carácter con el punto de código mínimo.

6. El método llamado index() encuentra el índice de una subcadena dada dentro de la cadena."""