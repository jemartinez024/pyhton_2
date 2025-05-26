word = input("Ingresa la palabra que deseas encontrar: ").upper()
strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

# Escribe el resto del código aquí.
try:
    for letter in word:
        start = strn.index(letter, start)
        start += 1
    print("Si")
except ValueError:
    print("No")