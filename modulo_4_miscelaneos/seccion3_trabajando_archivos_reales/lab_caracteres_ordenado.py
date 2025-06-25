"""4.3.9   LAB   Histograma de frecuencia de caracteres ordenado
El código anterior necesita ser mejorado. Está bien, pero tiene que ser mejor.

Tu tarea es hacer algunas enmiendas, que generen los siguientes resultados:

El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).
Suponiendo que el archivo de prueba contiene solo una línea con:

cBabAa
samplefile.txt
New Component Title
El resultado esperado debería verse de la siguiente manera:

Output
a -> 3
b -> 2
c -> 1

Consejo: Emplea una lambda para cambiar el ordenamiento."""

samplefile = input("Introduce el nombre del archivo: ")

try:
    with open(samplefile, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no existe.")

letters_count = {}
for char in content:
    if char.isalpha():
        char = char.lower()
        if char in letters_count:
            letters_count[char] += 1
        else:
            letters_count[char] = 1

letters_order = sorted(letters_count.items(), key=lambda item: -item[1])

with open(samplefile, 'w') as end_file:
    for letter, count in letters_order:
        end_file.write(f"{letter} -> {count}\n")

for letter in letters_order:
    print(f"{letter} -> {letters_count[letter]}")  