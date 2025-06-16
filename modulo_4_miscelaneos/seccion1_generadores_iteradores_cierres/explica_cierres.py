"""4.1.9 Una breve explicación de cierres
Comencemos con una definición: cierres es una técnica que permite almacenar valores a pesar de que el contexto en el que se crearon ya no existe. ¿Complicado? Un poco.

Analicemos un ejemplo simple:

def outer(par):
    loc = par
 
 
var = 1
outer(var)
 
print(par)
print(loc)
 

El ejemplo es obviamente erróneo.

Las dos últimas líneas provocarán una excepción NameError - ni par ni loc son accesibles fuera de la función. Ambas variables existen cuando y solo cuando la función exterior() esta siendo ejecutada.


Observa el ejemplo en el editor. Hemos modificado el código significativamente."""

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

"""Hay un elemento completamente nuevo - una función (llamada inner) dentro de otra función (llamada outer).

¿Cómo funciona? Como cualquier otra función excepto por el hecho de que inner() solo se puede invocar desde dentro de outer(). Podemos decir que inner() es una herramienta privada de outer(), ninguna otra parte del código la puede acceder.

Observa cuidadosamente:

La función inner() devuelve el valor de la variable accesible dentro de su alcance, ya que interior() puede utilizar cualquiera de las entidades a disposición de outer().
La función outer() devuelve la función inner() por si misma; mejor dicho, devuelve una copia de la función inner() al momento de la invocación de la función outer(); la función congelada contiene su entorno completo, incluido el estado de todas las variables locales, lo que también significa que el valor de loc se retiene con éxito, aunque outer() ya ha dejado de existir.
En efecto, el código es totalmente válido y genera:

Output
1
La función devuelta durante la invocación de outer() es un cierre.

Un cierre se debe invocar exactamente de la misma manera en que se ha declarado.

En el ejemplo siguiente:


def outer(par):
    loc = par
 
    def inner():
        return loc
    return inner
 
 
var = 1
fun = outer(var)
print(fun())
 

La función inner() no tenía parámetros, por lo que tuvimos que invocarla sin argumentos.

Ahora mira el código en el editor. Es totalmente posible declarar un cierre equipado con un número arbitrario de parámetros, por ejemplo, al igual que la función power()."""

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
    
"""Esto significa que el cierre no solo utiliza el ambiente congelado, sino que también puede modificar su comportamiento utilizando valores tomados del exterior.

Este ejemplo muestra una circunstancia más interesante: puedes crear tantos cierres como quieras usando el mismo código. Esto se hace con una función llamada make_closure(). Nota:

El primer cierre obtenido de make_closure() define una herramienta que eleva al cuadrado su argumento.
El segundo está diseñado para elevar el argumento al cubo.
Es por eso que el código produce el siguiente resultado:

Output
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
Realiza tus propias pruebas."""