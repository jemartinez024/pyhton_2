"""4.2.4 Manejo de archivos
Python supone que cada archivo está oculto detrás de un objeto de una clase adecuada.

Por supuesto, es difícil no preguntar cómo interpretar la palabra adecuada.

Los archivos se pueden procesar de muchas maneras diferentes: algunos dependen del contenido del archivo, otros de las intenciones del programador.

En cualquier caso, diferentes archivos pueden requerir diferentes conjuntos de operaciones y comportarse de diferentes maneras.

Un objeto de una clase adecuada es creado cuando abres el archivo y lo aniquilas al momento de cerrarlo.

Entre estos dos eventos, puedes usar el objeto para especificar que operaciones se deben realizar en un stream en particular. Las operaciones que puedes usar están impuestas por la forma en que abriste el archivo.

En general, el objeto proviene de una de las clases que se muestran aquí:"""