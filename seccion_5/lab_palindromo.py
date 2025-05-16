# Ingresa el texto a encriptar.
text = input("Ingresa una palabra para comprobar si es un palíndromo: ")
text = text.replace(' ','')  ## Elimina los espacios en blanco que pueda tener el IBAN.
text = text.lower()

str = text
inverted_string = str[::-1]
print(inverted_string)  # Salida:

if str == inverted_string:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')
    