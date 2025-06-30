"""4.5.2 Obtener la fecha local y crear objetos del tipo fecha
Una de las clases proporcionadas por el módulo datetime es una clase llamada date. Los objetos de esta clase representan una fecha que consta de año, mes y día. Mira el código en el editor para ver cómo se ve en la práctica y como obtener la fecha local actual usando el método today.

Ejecuta el código para ver qué sucede."""

from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)
    