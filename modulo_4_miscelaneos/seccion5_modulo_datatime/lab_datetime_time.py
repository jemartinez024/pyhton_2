"""4.5.20   LAB   Los módulos datetime y time
Durante este curso, has aprendido sobre el método strftime, que requiere conocimiento de las directivas para crear un formato. Ahora es el momento de poner en práctica estas directivas.

Por cierto, tendrás la oportunidad de practicar el trabajo con documentación, porque tendrás que encontrar directivas que aún no conoces.

Aquí está tu tarea:
Escribe un programa que cree un objeto datetime para el 4 de noviembre de 2020, 14:53:00. El objeto creado debe llamar al método strftime con el formato apropiado para mostrar el siguiente resultado:

Output
2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Día de la semana: 3
Día del año: 309
Número de semana en el año: 44
Nota: Cada línea de resultado debe crearse llamando al método strftime con al menos una directiva en el argumento de formato."""

import time
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

dt = dt.replace(year=2020, month=11, day=4)
print(dt)

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

d = date(2020, 11, 4)
print("Día de la semana: ", d.isoweekday())

d = date(2020, 11, 4)
print(dt.ctime())

delta = timedelta(weeks=43, days=8)
print("Día del año: ", delta)


