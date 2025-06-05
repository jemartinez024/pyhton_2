"""3.5.8 ¿Qué es el Orden de Resolución de Métodos (MRO) y por qué no todas las herencias tienen sentido?
MRO, en general, es una forma (puedes llamarlo una estrategia) en la que un lenguaje de programación en particular escanea la parte superior de la jerarquía de una clase para encontrar el método que necesita actualmente. Vale la pena enfatizar que los diferentes lenguajes usan MROs levemente (o incluso completamente) diferentes. Python es único en este aspecto y sus costumbres son un poco específicas.

Te mostraremos cómo funciona el MRO de Python en dos casos peculiares que son ejemplos claros de problemas que pueden ocurrir cuando intentas usar la herencia múltiple de manera demasiado imprudente. Comencemos con un fragmento que inicialmente puede parecer simple. Mira lo que te hemos preparado en el editor."""

class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("Medio")


class Bottom(Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

"""Estamos seguros de que si analizas el fragmento tu mismo, no verás ninguna anomalía en él. Sí, tienes toda la razón: parece claro y simple, y no genera preocupaciones. Si ejecutas el código, producirá el siguiente resultado predecible:

Output
abajo
Medio
superior

Sin sorpresas hasta ahora. Hagamos un pequeño cambio en este código. Echa un vistazo:"""

class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    
    
"""¿Puedes ver la diferencia? Está escondida en esta línea:


class Bottom(Middle, Top):
 
De esta manera exótica, hemos convertido un código muy simple con una clara ruta de herencia única en un misterioso acertijo de herencia múltiple. "¿Es válido?" Te puedes preguntar. Sí lo es. "¿Cómo es eso posible?" te preguntas, esperamos que realmente sientas la necesidad de hacer esta pregunta.

Como puedes ver, el orden en el que se enumeran las dos superclases entre paréntesis cumple con la estructura del código: la clase Middle precede a la clase Top, justo como en la ruta de herencia real.

A pesar de su rareza, la muestra es correcta y funciona como se esperaba, pero debe indicarse que esta notación no aporta ninguna funcionalidad nueva ni significado adicional.

Modifiquemos el código una vez más; ahora intercambiaremos ambos nombres de superclase en la definición de clase Bottom. Así es como se ve el fragmento de código ahora:"""

class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

"""New Component Title
Para anticiparnos a tu pregunta, diremos que esta enmienda ha estropeado el código y ya no se ejecutará. Qué pena. El orden que intentamos forzar (Top, Middle) es incompatible con la ruta de herencia que se deriva de la estructura del código. A Python no le gustará. Esto es lo que veremos:

Output
TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
Creemos que el mensaje habla por sí solo. El MRO de Python no se puede doblar ni violar, no solo porque esa es la forma en que funciona Python, sino también porque es una regla que debes obedecer."""