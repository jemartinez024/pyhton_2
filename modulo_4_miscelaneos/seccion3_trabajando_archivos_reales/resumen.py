"""
4.4.11 RESUMEN DE SECCIÓN
1. Para leer el contenido de un archivo, se pueden utilizar los siguientes métodos>

read(number): lee el número de carácteres/bytes del archivo y los retorna como una cadena, es capaz de leer todo el archivo a la vez.
readline() lee una sola línea del archivo de texto.
readlines(número) lee el número de líneas del archivo de texto; es capaz de leer todas las líneas a la vez.
readinto(bytearray): lee los bytes del archivo y llena el bytearray con ellos.

2. Para escribir contenido nuevo en un archivo, se pueden utilizar los siguientes métodos:

write(string): escribe una cadena a un archivo de texto.
write(bytearray): escribe todos los bytes de un bytearray a un archivo.

3. El método open() devuelve un objeto iterable que se puede usar para recorrer todas las líneas del archivo dentro de un bucle for. Por ejemplo:

for line in open("file", "rt"):
    print(line, end='')
 
El código copia el contenido del archivo a la consola, línea por línea. Nota: el stream se cierra automáticamente cuando llega al final del archivo."""