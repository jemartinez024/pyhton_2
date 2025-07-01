"""4.5.11 Las funciones asctime() y mktime()
El módulo time tiene funciones que esperan un objeto struct_time o una tupla que almacena valores de acuerdo con los índices presentados cuando se habla de la clase struct_time. Ejecuta el ejemplo en el editor."""

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
