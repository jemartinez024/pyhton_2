"""
4.3.7 Copiando archivos: una herramienta simple y funcional
Ahora vas a juntar todo este nuevo conocimiento, agregarle algunos elementos nuevos y usarlo para escribir un código real que pueda copiar el contenido de un archivo.

Por supuesto, el propósito no es crear un reemplazo para los comandos como copy de (MS Windows) o cp de (Unix/Linux) pero para ver una forma posible de crear una herramienta de trabajo, incluso si nadie quiere usarla.

Observa el código en el editor."""

from os import strerror

srcname = input("Ingresa el nombre del archivo fuente: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Ingresa el nombre del archivo destino: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()
    