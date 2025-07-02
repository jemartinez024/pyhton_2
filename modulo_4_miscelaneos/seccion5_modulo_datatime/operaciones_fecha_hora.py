"""4.5.18 Operaciones con la fecha y hora
Tarde o temprano tendrás que realizar algunos cálculos sobre la fecha y la hora. Afortunadamente, existe una clase llamada timedelta en el módulo datetime que se creó con tal propósito.

Para crear un objeto timedelta, simplemente realiza una resta en los objetos date o datetime, tal como hicimos en el ejemplo en el editor. Ejecútalo."""

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)