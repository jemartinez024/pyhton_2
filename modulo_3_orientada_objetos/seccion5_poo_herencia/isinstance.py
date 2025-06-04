"""3.5.3 isinstance()
Como ya sabes, un objeto es la encarnación de una clase. Esto significa que el objeto es como un pastel horneado usando una receta que se incluye dentro de la clase.

Esto puede generar algunos problemas.

Supongamos que tienes un pastel (por ejemplo, resultado de un argumento pasado a tu función). Deseas saber que receta se ha utilizado para prepararlo. ¿Por qué? Porque deseas saber que esperar de él, por ejemplo, si contiene nueces o no, lo cual es información crucial para ciertas personas.

Del mismo modo, puede ser crucial si el objeto tiene (o no tiene) ciertas características. En otras palabras, si es un objeto de cierta clase o no.

Tal hecho podría ser detectado por la función llamada isinstance():


isinstance(objectName, ClassName)
 
La función devuelve True si el objeto es una instancia de la clase, o False de lo contrario.

Ser una instancia de una clase significa que el objeto (el pastel) se ha preparado utilizando una receta contenida en la clase o en una de sus superclases.

No lo olvides: si una subclase contiene al menos las mismas características que cualquiera de sus superclases, significa que los objetos de la subclase pueden hacer lo mismo que los objetos derivados de la superclase, por lo tanto, es una instancia de su clase de inicio y cualquiera de sus superclases.

Probémoslo. Analiza el código en el editor."""


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
    
"""Hemos creado tres objetos, uno para cada una de las clases. Luego, usando dos bucles anidados, verificamos todos los pares posibles de clase de objeto para averiguar si los objetos son instancias de las clases.

Ejecuta el código.

Esto es lo que obtenemos:

Output
True    False   False
True    True    False
True    True    True

Hagamos que el resultado sea más legible

       es una subcalse de        Vehicle    LandVehicle    TrackedVehicle
           my_vehicle             True         False          False
           my_land_vehicle        True         True           False
           my_tracked_vehicle     True         True           True

¿La tabla confirma nuestras expectativas?
"""