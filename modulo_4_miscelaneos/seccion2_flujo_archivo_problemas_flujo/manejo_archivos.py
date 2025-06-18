"""4.2.4 Manejo de archivos
Python supone que cada archivo está oculto detrás de un objeto de una clase adecuada.

Por supuesto, es difícil no preguntar cómo interpretar la palabra adecuada.

Los archivos se pueden procesar de muchas maneras diferentes: algunos dependen del contenido del archivo, otros de las intenciones del programador.

En cualquier caso, diferentes archivos pueden requerir diferentes conjuntos de operaciones y comportarse de diferentes maneras.

Un objeto de una clase adecuada es creado cuando abres el archivo y lo aniquilas al momento de cerrarlo.

Entre estos dos eventos, puedes usar el objeto para especificar que operaciones se deben realizar en un stream en particular. Las operaciones que puedes usar están impuestas por la forma en que abriste el archivo.

En general, el objeto proviene de una de las clases que se muestran aquí:"""

"""Nota: nunca se utiliza el constructor para dar vida a estos objetos. La unica forma de obtenerlos es invocar la función llamada open().

La función analiza los argumentos proporcionados y crea automáticamente el objeto requerido.

Si deseas deshacerte del objeto, invoca el método denominado close().

La invocación cortará la conexión con el objeto y el archivo, y eliminará el objeto.

Para nuestros propósitos, solo nos ocuparemos de los streams representados por los objetos BufferIOBase y TextIOBase. Entenderás por que pronto.

Debido al tipo de contenido de los flujos o streams, se dividen en tipo texto y binario.

Los streams de texto están estructurados en líneas; es decir, contienen caracteres tipográficos (letras, dígitos, signos de puntuación, etc). dispuestos en filas (líneas), como se ve a simple vista cuando se mira el contenido del archivo en el editor.

Este tipo de archivo es escrito (o leído) principalmente carácter por carácter, o línea por línea.

Los streams binarios no contienen texto, sino una secuencia de bytes de cualquier valor. Esta secuencia puede ser, por ejemplo, un programa ejecutable, una imagen, un audio o un videoclip, un archivo de base de datos, etc.

Debido a que estos archivos no contienen líneas, las lecturas y escrituras se relacionan con porciones de datos de cualquier tamaño. Por lo tanto, los datos se leen y escriben byte a byte, o bloque a bloque, donde el tamaño del bloque generalmente varía de uno a un valor elegido arbitrariamente.

Ahora viene un problema pequeño. En los sistemas Unix/Linux, los extremos de la línea están marcados por un solo carácter llamado LF (código ASCII 10) designado en los programas de Python como \n.

Otros sistemas operativos, especialmente los derivados del sistema prehistórico CP/M (que también aplica a los sistemas de la familia Windows) utilizan una convención diferente: el final de la línea está marcada por un par de caracteres, CR y LF (códigos ASCII 13 y 10) los cuales se puede codificar como \r\n.

Esta ambigüedad puede causar varias consecuencias desagradables.

Si creas un programa responsable de procesar un archivo de texto y está escrito para Windows, puedes reconocer los extremos de las líneas al encontrar los caracteres \r\n, pero si el mismo programa se ejecuta en un entorno Unix/Linux será completamente inútil, y viceversa: el programa escrito para sistemas Unix/Linux podría ser inútil en Windows.

Estas características indeseables del programa, que impiden o dificultan el uso del programa en diferentes entornos, se denomina falta de portabilidad.

Del mismo modo, el rasgo del programa que permite la ejecución en diferentes entornos se llama portabilidad. Un programa dotado de tal rasgo se llama programa portable.

Dado que los problemas de portabilidad eran (y siguen siendo) muy graves, se tomó la decisión de resolver definitivamente el problema de una manera que no atraiga mucho la atención del desarrollador.

"""