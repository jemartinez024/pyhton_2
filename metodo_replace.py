# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

"""El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento."""
    
"""La salida del ejemplo es:

www.pythoninstitute.org
Thare are it!
Apple"""

"""Si el segundo argumento es una cadena vacía, reemplazar significa realmente eliminar el primer argumento de la cadena. ¿Qué tipo de magia ocurre si el primer argumento es una cadena vacía?


La variante del método replace() con tres parámetros emplea un tercer argumento (un número) para limitar el número de reemplazos.

Observa el código modificado a continuación:"""

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
    