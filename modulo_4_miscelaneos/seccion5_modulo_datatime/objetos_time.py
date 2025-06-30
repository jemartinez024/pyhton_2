"""4.5.7 Creando objetos time
Ya sabes cómo presentar una fecha utilizando el objeto date. El módulo datetime también tiene una clase que te permite presentar la hora. ¿Puedes adivinar su nombre? Sí, se llama time:

time(hour, minute, second, microsecond, tzinfo, fold)
 
El constructor de la clase time acepta los siguientes parámetros opcionales:

Parametro:      Restricciones

hour            El parametro hour debe ser mayor o igual que 0 y menor que 23.
minute          El parametro minute debe ser mayor o igual que 0 y menor que 59.
second          El parametro second debe ser mayor o igual que 0 y menor que 59.
microsecond     El parametro microsecond debe ser mayor o igual que 0 y menor que 10000000.
tzinfo          El parametro tzinfo debe ser un objeto de la subclase tzinfo o none (por defecto).
fold            El parametro fold debe ser 0 o 1 (prederterminadamente 0).

El párametro tzinfo está asociado con las zonas horarias, mientras que fold está asociado con el tiempo de pared. No los usaremos durante este curso, pero te recomendamos que te familiarices con ellos.

Veamos cómo crear un objeto de tiempo en la práctica. Ejecuta el código en el editor.
"""

from datetime import time

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minutos:", t.minute)
print("Segundos:", t.second)
print("Microsegundo:", t.microsecond)


"""Resultado:

Output
Tiempo: 14:53:20.000001
Hora: 14
Minutos: 53
Segundos: 20
Microsegundos: 1
En el ejemplo, pasamos cuatro parámetros al constructor de la clase: hour, minute, second, and microsecond. Se puede acceder a cada uno de ellos utilizando los atributos de clase.

Nota: Pronto te diremos cómo puedes cambiar el formato de hora predeterminado."""