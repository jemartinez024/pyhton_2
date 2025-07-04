"""4.5.19 Creando objetos timedelta
Ya has aprendido que un objeto timedelta puede devolverse como resultado de restar dos objetos date o datetime.

Por supuesto, también puedes crear un objeto tu mismo. Para ello, vamos a familiarizarnos con los argumentos aceptados por el constructor de la clase, que son:days, seconds, microseconds, milliseconds, minutes, hours, y weeks. Cada uno de ellos es opcional y el valor predeterminado es 0.

Los argumentos deben ser números enteros o de punto flotante, y pueden ser positivos o negativos. Veamos un ejemplo sencillo en el editor."""

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

"""Resultado:

Output
16 days, 3:00:00

El resultado de 16 días se obtiene convirtiendo el argumento weeks en días (2 semanas = 14 días) y agregando el argumento days (2 días). Este es un comportamiento normal, porque el objeto timedelta solo almacena días, segundos y microsegundos internamente. De manera similar, el argumento hora se convierte en minutos. Echa un vistazo al siguiente ejemplo:


from datetime import timedelta
 
delta = timedelta(weeks=2, days=2, hours=3)
print("Días:", delta.days)
print("Segundos:", delta.seconds)
print("Microsegundos:", delta.microseconds)
 

Resultado:

Output
Días: 16
Segundos: 10800
Microsegundos: 0
El resultado de 10800 se obtiene convirtiendo 3 horas en segundos. De esta forma el objeto timedelta almacena los argumentos pasados durante su creación. Las semanas se convierten en días, las horas y los minutos en segundos y los milisegundos en microsegundos.


Ya sabes cómo el objeto timedelta almacena los argumentos pasados internamente. Veamos cómo se puede utilizar en la práctica.

Observa algunas operaciones admitidas por las clases del módulo datetime. Ejecuta el código que te proporcionamos en el editor."""


from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
    

