"""4.3.1 Procesamiento de archivos de texto
En esta lección vamos a preparar un archivo de texto simple con contenido breve y simple.

Te mostraremos algunas técnicas básicas que puedes utilizar para leer el contenido del archivo y poder procesarlo.

El procesamiento será muy simple: vas a copiar el contenido del archivo a la consola y contarás todos los caracteres que el programa ha leído.

Pero recuerda: nuestra comprensión de un archivo de texto es muy estricta. Es un archivo de texto sin formato: puede contener solo texto, sin decoraciones adicionales (formato, diferentes fuentes, etc.).

Es por eso que debes evitar crear el archivo utilizando un procesador de texto avanzado como MS Word, LibreOffice Writer o algo así. Utiliza los conceptos básicos que ofrece tu sistema operativo: Bloc de notas, vim, gedit, etc.

Si tus archivos de texto contienen algunos caracteres nacionales no cubiertos por el juego de caracteres ASCII estándar, es posible que necesites un paso adicional. La invocación de tu función open() puede requerir un argumento que denote una codificación específica del texto.

Por ejemplo, si estás utilizando un sistema operativo Unix/Linux configurado para usar UTF-8 como una configuración de todo el sistema, la función open() puede verse de la siguiente manera:


stream = open('file.txt', 'rt', encoding='utf-8')
 

Donde el argumento de codificación debe establecerse en un valor dentro de una cadena que representa la codificación de texto adecuada (UTF-8, en este caso).

Consulta la documentación de tu sistema operativo para encontrar el nombre de codificación adecuado para tu entorno.


  Nota  
A los fines de nuestros experimentos con el procesamiento de archivos que se llevan a cabo en esta sección, vamos a utilizar un conjunto de archivos precargados (p. ej., los archivos tzop.txt, o text.txt files) con los cuales podrás trabajar. Si deseas trabajar con tus propios archivos localmente en tu máquina, te recomendamos que lo hagas y que utilices IDLE o cualquier otro Entorno de Desarrollo para llevar a cabo tus propias pruebas.

La lectura del contenido de un archivo de texto se puede realizar utilizando diferentes métodos; ninguno de ellos es mejor o peor que otro. Depende de ti cual de ellos prefieres y te gusta.

Algunos de ellos serán a veces más prácticos y otros más problemáticos. Se flexible. No tengas miedo de cambiar tus preferencias.

El más básico de estos métodos es el que ofrece la función read(), la cual pudiste ver en acción en la lección anterior.

Si se aplica a un archivo de texto, la función es capaz de:

Leer un número determinado de caracteres (incluso solo uno) del archivo y devolverlos como una cadena.
Leer todo el contenido del archivo y devolverlo como una cadena.
Si no hay nada más que leer (el cabezal de lectura virtual llega al final del archivo), la función devuelve una cadena vacía.

Comenzaremos con la variante más simple y usaremos un archivo llamado text.txt. El archivo contiene lo siguiente:

Output
Lo hermoso es mejor que lo feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.

Ahora observa el código en el editor y analicémoslo."""