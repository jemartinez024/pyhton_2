"""3.4.7   LAB   La clase Timer
New Component Title
Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan fácil como podrías pensar, ya que tendremos algunos requisitos específicos.

Léelos con atención, ya que la clase sobre la que escribes se utilizará para lanzar cohetes en misiones internacionales a Marte. Es una gran responsabilidad. ¡Contamos contigo!

Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second(), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.
Emplea las siguientes sugerencias:

Todas las propiedades del objeto deben ser privadas.
Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.
Completa la plantilla que te proporcionamos en el editor. Ejecuta tu código y comprueba si el resultado es el mismo que el nuestro.

Salida Esperada
Output
23:59:59
00:00:00
23:59:59"""


class Timer:
    def __init__( self, hours=0, minutes=0, seconds=0 ):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        #
        # Escribir código aquí
        #

    def __str__(self):
         return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
        #
        # Escribir código aquí
        #

    def next_second(self): 
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes >= 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours >= 24:
                    self.__hours = 0
        #
        # Escribir código aquí
        #

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23
        #
        # Escribir código aquí
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)