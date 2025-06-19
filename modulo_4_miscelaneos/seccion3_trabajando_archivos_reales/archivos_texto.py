"""4.3.4 Manejo de archivos de texto: write()
Escribir archivos de texto parece ser más simple, ya que hay un método que puede usarse para realizar dicha tarea.

El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo abierto (no lo olvides), el modo de apertura debe reflejar la forma en que se transfieren los datos, escribir en un archivo abierto en modo de lectura no tendrá éxito).

No se agrega carácter de nueva línea al argumento de write(), por lo que debes agregarlo tu mismo si deseas que el archivo se complete con varias líneas.

El ejemplo en el editor muestra un código muy simple que crea un archivo llamado newtext.txt (nota: el modo de apertura w asegura que el archivo se creará desde cero, incluso si existe y contiene datos) y luego coloca diez líneas en él."""

from os import strerror

try:
	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
#print('newtext.txt', "ha sido creado con éxito.")
 
 
"""La cadena que se grabará consta de la palabra línea, seguida del número de línea. Hemos decidido escribir el contenido de la cadena carácter por carácter (esto lo hace el bucle interno for) pero no estás obligado a hacerlo de esta manera.

Solo queríamos mostrarte que write() puede operar con caracteres individuales.

El código crea un archivo con el siguiente texto:

Output
línea #1
línea #2
línea #3
línea #4
línea #5
línea #6
línea #7
línea #8
línea #9
línea #10
¿Puedes imprimir el contenido del archivo en la consola?

Te alentamos a que pruebes el comportamiento del método write() localmente en tu máquina.

Mira el ejemplo en el editor. Hemos modificado el código anterior para escribir líneas enteras en el archivo de texto."""


from os import strerror

try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    
"""El contenido del archivo recién creado es el mismo.

Nota: puedes usar el mismo método para escribir en el stream stderr, pero no intentes abrirlo, ya que siempre está abierto implícitamente.

New Component Title
Por ejemplo, si deseas enviar un mensaje de tipo cadena a stderr para distinguirlo de la salida normal del programa, puede verse así:


import sys
sys.stderr.write("Mensaje de Error")
 
"""