"""4.6.9 Creando un objeto Calendar
El constructor de la clase Calendar toma un parámetro opcional llamado firstweekday, por defecto es igual a 0 (lunes).

El parámetro firstweekday debe ser un valor entero entre 0-6. Para este propósito, podemos usar las constantes ya conocidas: mira el código en el editor."""

import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

"""El programa generará el siguiente resultado:

6 0 1 2 3 4 5
El ejemplo de código usa el método de la clase Calendar llamado iterweekdays, que devuelve un iterador para los números de los días de la semana.

El primer valor devuelto siempre es igual al valor de la propiedad firstweekday. Debido a que en nuestro ejemplo el primer valor devuelto es 6, significa que la semana comienza un domingo."""