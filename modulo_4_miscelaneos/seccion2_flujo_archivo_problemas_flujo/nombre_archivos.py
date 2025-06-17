""""4.2.2 Nombre de archivos
Los diferentes sistemas operativos pueden tratar a los archivos de diferentes maneras. Por ejemplo, Windows usa una convención de nomenclatura diferente a la adoptada en los sistemas Unix/Linux.

Si utilizamos la noción de un nombre de archivo canónico (un nombre que define de forma exclusiva la ubicación del archivo, independientemente de su nivel en el árbol de directorios), podemos darnos cuenta de que estos nombres se ven diferentes en Windows y en Unix/Linux:




Además, los nombres de archivo de sistemas Unix/Linux distinguen entre mayúsculas y minúsculas. Los sistemas Windows almacenan mayúsculas y minúsculas en el nombre del archivo, pero no distinguen entre ellas.

Esto significa que estas dos cadenas: EsteEsElNombreDelArchivo y esteeselnombredelarchivo describen dos archivos diferentes en sistemas Unix/Linux, pero tienen el mismo nombre para un solo archivo en sistemas Windows.

TLa diferencia principal y más llamativa es que debes usar dos separadores diferentes para los nombres de directorio: \ en Windows, y / en Unix/Linux.

Esta diferencia no es muy importante para el usuario normal, pero es muy importante al escribir programas en Python.

Para entender por qué, intenta recordar el papel muy específico que desempeña \ dentro de las cadenas en Python.

Supongamos que estás interesado en un archivo en particular ubicado en el directorio dir, y con el nombre de file.

Supongamos también que deseas asignar a una cadena el nombre del archivo.

En sistemas Unix/Linux, sería de la siguiente manera:

name = "/dir/file"
 

Pero si intentas codificarlo para el sistema Windows:

name = "\dir\file"
 
Obtendrás una sorpresa desagradable, Python generará un error o la ejecución del programa se comportará de manera extraña, como si el nombre del archivo se hubiera distorsionado de alguna manera.

De hecho, no es extraño en lo absoluto, pero es bastante obvio y natural. Python usa la \ como un carácter de escape (como \n).

Esto significa que los nombres de archivo de Windows deben escribirse de la siguiente manera:

name = "\\dir\\file"
 
Afortunadamente, también hay una solución más. Python es lo suficientemente inteligente como para poder convertir diagonales en diagonales invertidas cada vez que descubre que el sistema operativo lo requiere.

Esto significa que cualquiera de las siguientes asignaciones:

name = "/dir/file"
name = "c:/dir/file"
 
Funcionará también con Windows.

Cualquier programa escrito en Python (y no solo en Python, porque esa convención se aplica a prácticamente todos los lenguajes de programación) no se comunica con los archivos directamente, sino a través de algunas entidades abstractas que se nombran de manera diferente en los distintos lenguajes o entornos, los términos más utilizados son handles o manejadores (un tipo de puntero inteligente) o streams o flujos (una especie de canal), los usaremos como sinónimos aquí.

El programador, que tiene un conjunto de funciones y métodos, puede realizar ciertas operaciones en el flujo o stream, que afectan los archivos reales utilizando mecanismos contenidos en el núcleo del sistema operativo.

De esta forma, puedes implementar el proceso de acceso a cualquier archivo, incluso cuando el nombre del archivo es desconocido al momento de escribir el programa.


Las operaciones realizadas con el flujo o stream abstracto reflejan las actividades relacionadas con el archivo físico.

Para conectar (vincular) el stream con el archivo, es necesario realizar una operación explícita.

La operación de conectar un stream con un archivo es llamada abrir el archivo, mientras que desconectar el enlace se denomina cerrar el archivo.

Por lo tanto, la conclusión es que la primera operación realizada en el flujo o stream es siempre open (abrir) y la ultima es close (cerrar). El programa, en efecto, es libre de manipular el stream entre estos dos eventos y manejar el archivo asociado.

Esta libertad está limitada por las características físicas del archivo y la forma en que se abrió el archivo.

Digamos nuevamente que la apertura del stream puede fallar, y puede ocurrir debido a varias razones: la más común es la falta de un archivo con un nombre específico.

También puede suceder que el archivo físico exista, pero el programa no puede abrirlo. También existe el riesgo de que el programa haya abierto demasiados streams, y el sistema operativo específico puede no permitir la apertura simultánea de más de n archivos (por ejemplo, 200).

Un programa bien escrito debe detectar estas aperturas fallidas y reaccionar en consecuencia.
"""