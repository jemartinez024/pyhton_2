# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

"""El programa Ejemplo 1 da la siguiente salida:

A
Output
Nota: Es una A mayúscula. ¿Por qué? Recuerdas la tabla ASCII, ¿qué letras ocupan las primeras posiciones, mayúsculas o minúsculas?

Hemos preparado dos ejemplos más para analizar: Ejemplos 2 y 3.

Como puedes ver, presentan más que solo cadenas. El resultado esperado se ve de la siguiente manera:

[ ]
0
Output
Nota: hemos utilizado corchetes para evitar que el espacio se pase por alto en tu pantalla."""