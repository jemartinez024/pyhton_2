"""3.5.9 El problema del diamante
El segundo ejemplo del espectro de problemas que posiblemente pueden surgir de la herencia múltiple está ilustrado por un problema clásico llamado problema del diamante. El nombre refleja la forma del diagrama de herencia; observa la imagen:
Existe la superclase superior llamada A.

Existen dos subclases derivadas de A: B y C.

También está la subclase inferior llamada D, derivada de B y C (o C y B, ya que estas dos variantes significan cosas diferentes en Python).
¿Puedes ver el diamante ahí?

Echa un vistazo al código en el editor. La misma estructura, pero expresada en Python.
"""

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

"""Algunos lenguajes de programación no permiten la herencia múltiple en absoluto y, como consecuencia, no te permitirán construir un diamante; este es el camino que Java y C# han elegido seguir desde sus orígenes.

Python, sin embargo, ha elegido una ruta diferente: permite la herencia múltiple y no le importa si escribe y ejecuta código como el del editor. Pero no te olvides del MRO: siempre está a cargo.


Reconstruyamos nuestro ejemplo de la página anterior para hacerlo más parecido a un diamante, como se muestra a continuación:"""


class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()