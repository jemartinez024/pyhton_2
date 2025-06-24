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

letters_order = sorted(letters_count.keys())

for letter in letters_order:
    print(f"{letter} -> {letters_count[letter]}")  