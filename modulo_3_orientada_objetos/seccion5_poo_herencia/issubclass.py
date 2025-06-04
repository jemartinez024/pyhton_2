"""3.5.2 issubclass()
Python ofrece una función que es capaz de identificar una relación entre dos clases, y aunque su diagnóstico no es complejo, puede verificar si una clase particular es una subclase de cualquier otra clase.

Así es como se ve:


issubclass(ClassOne, ClassTwo)

La función devuelve True si ClassOne es una subclase de ClassTwo, y False de lo contrario.

Vamos a verlo en acción, puede sorprenderte. Mira el código en el editor. Léelo cuidadosamente."""

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
    
"""Hay dos bucles anidados. Su propósito es verificar todos los pares de clases ordenadas posibles y que imprima los resultados de la verificación para determinar si el par coincide con la relación subclase-superclase.

Ejecuta el código. El programa produce el siguiente resultado:

Output
True    False   False
True    True    False
True    True    True
Hagamos que el resultado sea más legible:

       es una subcalse de      Vehicle    LandVehicle    TrackedVehicle
            Vehicle             True         False          False
            LandVehicle         True         True           False
            TrackedVehicle      True         True            True

Existe una observación importante que hacer: cada clase se considera una subclase de sí misma."""