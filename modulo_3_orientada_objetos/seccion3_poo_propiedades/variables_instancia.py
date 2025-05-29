"""3.3.1 Variables de instancia
En general, una clase puede equiparse con dos tipos diferentes de datos para formar las propiedades de una clase. Ya viste uno de ellos cuando estábamos estudiando pilas.

Este tipo de propiedad existe solo cuando se crea explícitamente y se agrega a un objeto. Como ya sabes, esto se puede hacer durante la inicialización del objeto, realizada por el constructor.

Además, se puede hacer en cualquier momento de la vida del objeto. Es importante mencionar también que cualquier propiedad existente se puede eliminar en cualquier momento.

Tal enfoque tiene algunas consecuencias importantes:

Diferentes objetos de la misma clase pueden poseer diferentes conjuntos de propiedades.
Debe haber una manera de verificar con seguridad si un objeto específico posee la propiedad que deseas utilizar (a menos que quieras generar una excepción, siempre vale la pena considerarlo).
Cada objeto lleva su propio conjunto de propiedades, no interfieren entre sí de ninguna manera.
Tales variables (propiedades) se llaman variables de instancia.

La palabra instancia sugiere que están estrechamente conectadas a los objetos (que son instancias de clase), no a las clases mismas. Echemos un vistazo más de cerca.

Aquí hay un ejemplo:"""