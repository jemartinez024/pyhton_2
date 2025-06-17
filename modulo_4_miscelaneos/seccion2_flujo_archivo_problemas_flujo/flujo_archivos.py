"""4.2.3 Flujos de archivos (streams)
La apertura del stream no solo está asociada con el archivo, sino que también se debe declarar la manera en que se procesará el stream. Esta declaración se llama open mode (modo de apertura).

Si la apertura es exitosa, el programa solo podrá realizar las operaciones que sean consistentes con el modo abierto declarado.

Hay dos operaciones básicas a realizar con el stream:

Lectura del stream: las porciones de los datos se recuperan del archivo y se colocan en un área de memoria administrada por el programa (por ejemplo, una variable).
Escritura del stream: Las porciones de los datos de la memoria (por ejemplo, una variable) se transfieren al archivo.
Existen tres modos básicos utilizados para abrir un stream:

Modo Lectura: un stream abierto en este modo permite solo operaciones de lectura; intentar escribir en la transmisión provocará una excepción (la excepción se llama UnsupportedOperation, la cual hereda el OSError y el ValueError, y proviene del módulo io).
Modo Escritura: un stream abierto en este modo permite solo operaciones de escritura; intentar leer el stream provocará la excepción mencionada anteriormente.
Modo Actualizar: un stream abierto en este modo permite tanto lectura como escritura.

Antes de discutir como manipular los streams, te debemos una explicación. El stream se comporta casi como una grabadora.

Cuando lees algo de un stream, un cabezal virtual se mueve sobre la transmisión de acuerdo con el número de bytes transferidos desde el stream.


Cuando escribes algo en el stream el mismo cabezal se mueve a lo largo del stream registrando los datos de la memoria.

Siempre que hablemos de leer y escribir en el stream, trata de imaginar esta analogía. Los libros de programación se refieren a este mecanismo como la posición actual del archivo, aquí también usaremos este término.

Ahora es necesario mostrarte el objeto responsable de representar los streams en los programas."""