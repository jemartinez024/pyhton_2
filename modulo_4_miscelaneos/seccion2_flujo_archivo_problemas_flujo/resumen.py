"""
4.2.11 RESUMEN DE SECCIÓN
1. Un archivo necesita ser abierto antes de que pueda ser procesado por un programa, y debe ser cerrado cuando el procesamiento termine.

El abrir un archivo lo asocia con el stream, que es una representación abstracta de los datos físicos almacenados en los medios. La forma en que se procesa el stream se llama modo de apertura. Existen tres modos de apertura:

modo lectura - solo se permiten operaciones de lectura.
modo escritura - solo se permiten operaciones de escritura.
modo de actualización - se permiten ambas, lectura y escritura.

2. Dependiendo del contenido del archivo físico, se pueden usar diferentes clases de Python para procesar archivos. En general, BufferedIOBase es capaz de procesar cualquier archivo, mientras que TextIOBase es una clase especializada dedicada al procesamiento de archivos de texto (es decir, archivos que contienen textos visibles para humanos divididos en líneas usando marcadores de nueva línea). Por lo tanto, los streams se pueden dividir en binarios y de texto.


3. Las siguientes sintaxis de la funcion open() se utilizan para abrir un archivo:

open(file_name, mode=open_mode, encoding=text_encoding)
La invocación crea un objeto stream y lo asocia con el archivo llamado file_name, utilizando el modo open_mode y configurando el especificado text_encoding, o genera una excepción en caso de un error.

4. Los tres streams predefinidos que ya estan abiertos cuando inicia el programa son:

sys.stdin, entrada estandar.
sys.stdout, salida estandar.
sys.stderr, salida de error estandar.

5. El objeto de la excepción IOError, creado cuando cualquier operación de archivo falla (incluyendo las operaciones de apertura), contiene una propiedad llamada errno, que contiene el código de finalización de la acción fallida. Utiliza este valor para diagnosticar el problema."""