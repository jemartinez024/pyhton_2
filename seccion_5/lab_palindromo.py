# Ingresa el texto a encriptar.
text = input("Ingresa una palabra para comprobar si es un palíndromo: ")
text = text.replace(' ','')  ## Elimina los espacios en blanco que pueda tener
text = text.lower() # Convierte a minúsculas.

input_str = text
inverted_string = input_str[::-1]
print(inverted_string)  # Salida:

if input_str == inverted_string:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')
    