"""4.2.5 Abriendo los flujos o streams
El abrir un stream se realiza mediante una función que se puede invocar de la siguiente manera:


stream = open(file, mode = 'r', encoding = None)
 

Vamos a analizarlo:

El nombre de la función (open) habla por si mismo; si la apertura es exitosa, la función devuelve un objeto stream; de lo contrario, se genera una excepción (por ejemplo, FileNotFoundError si el archivo que vas a leer no existe);

El primer parámetro de la función (file) especifica el nombre del archivo que se asociará al stream.

El segundo parámetro (mode) especifica el modo de apertura utilizado para el stream; es una cadena llena de una secuencia de caracteres, y cada uno de ellos tiene su propio significado especial (más detalles pronto).

El tercer parámetro (encoding) especifica el tipo de codificación (por ejemplo, UTF-8 cuando se trabaja con archivos de texto).

La apertura debe ser la primera operación realizada en el stream.
Nota: el modo y los argumentos de codificación pueden omitirse; en dado caso, se tomarán sus valores predeterminados. El modo de apertura predeterminado es leer en modo de texto, mientras que la codificación predeterminada depende de la plataforma utilizada.

Permítenos ahora presentarte los modos de apertura más importantes y útiles. ¿Listo?

Modos para abrir los flujos o streams:
r modo de apertura: lectura

El stream será abierto en modo lectura.
El archivo asociado con el stream debe existir y tiene que ser legible, de lo contrario la función open() generará una excepción.
w modo de apertura: escritura

El stream será abierto en modo escritura.
El archivo asociado con el stream no necesita existir. Si no existe, se creará; si existe, se truncará a la longitud de cero (se borra); si la creación no es posible (por ejemplo, debido a permisos del sistema) la función open() generará una excepción.
a modo de apertura: adjuntar

la transmisión se abrirá en modo de adición;
El archivo asociado con el stream no necesita existir; si no existe, se creará; si existe, el cabezal de grabación virtual se establecerá al final del archivo (el contenido anterior del archivo permanece intacto).
r+ modo de apertura: lectura y actualización

El stream será abierto en modo lectura y actualización.
El archivo asociado con el stream debe existir y tiene que permitir escritura, de lo contrario la función open() generará una excepción.
Se permiten operaciones de lectura y escritura en el stream.
w+ modo de apertura: escritura y actualización

El stream será abierto en modo escritura y actualización.
El archivo asociado con el stream no necesita existir; si no existe, se creará; el contenido anterior del archivo permanece intacto.
Se permiten operaciones de lectura y escritura en el stream.

4.2.6 Selección de los modos de texto y binario
Si hay una letra b al final de la cadena del modo significa que el stream se debe abrir en el modo binario.

Si la cadena del modo termina con una letra t el stream es abierto en modo texto.

El modo texto es el comportamiento predeterminado que se utiliza cuando no se especifica ya sea modo binario o texto.

Finalmente, la apertura exitosa del archivo establecerá la posición actual del archivo (el cabezal virtual de lectura/escritura) antes del primer byte del archivo si el modo no es a y después del último byte del archivo si el modo es a.
Modo texto                  Modo binario                Descripción
rt (predeterminado)           rb                         Lectura
wt (predeterminado)           wb                         Escritura
at (predeterminado)           ab                         Adjnutar
r+t                          r+b                        Lectura actualización
w+t                          w+b                        Escritura actualización

EXTRA  
También puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el modo de apertura x. Si el archivo ya existe, la función open() generará una excepción.

"""