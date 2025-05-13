# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

"""El método index()
El método index() (es un método, no una función) busca la secuencia desde el principio, para encontrar el primer elemento del valor especificado en su argumento.

Nota: el elemento buscado debe aparecer en la secuencia, su ausencia causará una excepción ValueError.

El método devuelve el índice de la primera aparición del argumento (lo que significa que el resultado más bajo posible es 0, mientras que el más alto es la longitud del argumento decrementado en 1)."""

# Demostración de la función list():
print(list("abcabc"))