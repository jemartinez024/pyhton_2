"""4.5.6 ¿Que dia de la semana es?
Uno de los métodos más útiles que facilita el trabajo con fechas es el método llamado weekday. Devuelve el día de la semana como un número entero, donde 0 es el lunes y 6 es el domingo. Ejecuta el código en el editor."""

from datetime import date

d = date(2025, 6, 29)
print(d.weekday())


from datetime import date

d = date(2025, 6, 29)
print(d.isoweekday())

