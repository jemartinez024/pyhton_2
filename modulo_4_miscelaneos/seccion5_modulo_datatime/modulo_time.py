"""4.5.8 El módulo time
Además de la clase time, la biblioteca estándar de Python ofrece un módulo llamado time, que proporciona una función relacionada con el tiempo. Ya se tuvo la oportunidad de aprender la función llamada time cuando se habló de la clase date. Ahora veremos otra función útil disponible en este módulo.

Debes pasar muchas horas frente a una computadora mientras realiza este curso. A veces puedes sentir la necesidad de tomar una siesta. ¿Por qué no? Escribamos un programa que simule la siesta corta de un estudiante. Echa un vistazo al código en el editor."""

import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)
    