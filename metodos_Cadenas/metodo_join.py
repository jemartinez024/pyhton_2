# Demostración del método join():
print(",".join(["omicron", "pi", "rho"]))

"""El método join() es algo complicado, así que déjanos guiarte paso a paso:

Como su nombre lo indica, el método realiza una unión y espera un argumento del tipo lista; se debe asegurar que todos los elementos de la lista sean cadenas: de lo contrario, el método generará una excepción TypeError.
Todos los elementos de la lista serán unidos en una sola cadena pero...
... la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
La cadena recién creada se devuelve como resultado."""

"""Vamos a analizarlo:

El método join() se invoca desde una cadena que contiene una coma (la cadena puede ser larga o puede estar vacía).
El argumento del join es una lista que contiene tres cadenas.
El método devuelve una nueva cadena.

Aquí está:

omicron,pi,rho
"""