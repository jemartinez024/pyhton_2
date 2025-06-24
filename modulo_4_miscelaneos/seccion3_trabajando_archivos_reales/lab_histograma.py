samplefile = input("Introduce el nombre del archivo: ")

try:
    with open(samplefile, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no existe.")

