"""4.5.6 ¿Que dia de la semana es?
Uno de los métodos más útiles que facilita el trabajo con fechas es el método llamado weekday. Devuelve el día de la semana como un número entero, donde 0 es el lunes y 6 es el domingo. Ejecuta el código en el editor."""

from datetime import date

d = date(2025, 6, 29)
print(d.weekday())


from datetime import date

d = date(2025, 6, 29)
print(d.isoweekday())

"""Resultado:

1
Como puedes ver, para la misma fecha obtenemos un número entero diferente, pero expresando el mismo día de la semana. El entero devuelto por el método isodayweek sigue la especificación ISO 85601."""