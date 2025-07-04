"""4.5.19 Creando objetos timedelta
Ya has aprendido que un objeto timedelta puede devolverse como resultado de restar dos objetos date o datetime.

Por supuesto, también puedes crear un objeto tu mismo. Para ello, vamos a familiarizarnos con los argumentos aceptados por el constructor de la clase, que son:days, seconds, microseconds, milliseconds, minutes, hours, y weeks. Cada uno de ellos es opcional y el valor predeterminado es 0.

Los argumentos deben ser números enteros o de punto flotante, y pueden ser positivos o negativos. Veamos un ejemplo sencillo en el editor."""

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)