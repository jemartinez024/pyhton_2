"""4.5.16 La función strftime() en el módulo time
Probablemente no te sorprendas al saber que la función strftime está disponible en el módulo time. Se diferencia ligeramente de los métodos strftime en las clases proporcionadas por el módulo datetime porque, además del argumento de formato, también puede tomar (opcionalmente) un objeto tuple o struct_time.

Si no se pasa una tupla o un objeto struct_time, el formateo se realizará utilizando la hora local actual. Echa un vistazo al ejemplo en el editor."""

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))