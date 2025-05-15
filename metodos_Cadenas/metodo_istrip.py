# Demostración del método lstrip():
print("[" + " tau ".lstrip() + "]")

"""El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales."""

"""El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los caracteres incluidos en el argumento (una cadena), no solo espacios en blanco:"""

print("www.cisco.com".lstrip("w."))

"""Aquí no se necesitan corchetes, ya que el resultado es el siguiente:

cisco.com"""

"""¿Puedes adivinar la salida del fragmento a continuación? Piensa cuidadosamente. Ejecuta el código y verifica tus predicciones."""

print("pythoninstitute.org".lstrip(".org"))
    