"""3.1.1 Los conceptos básicos del enfoque orientado a objetos
Demos un paso fuera de la programación y las computadoras, y analicemos temas de programación orientada a objetos.

Casi todos los programas y técnicas que has utilizado hasta ahora pertenecen al estilo de programación procedimental. Es cierto que has utilizado algunos objetos incorporados, pero cuando nos referimos a ellos, se mencionan lo mínimo posible.

La programación procedimental fue el enfoque dominante para el desarrollo de software durante décadas de TI, y todavía se usa en la actualidad. Además, no va a desaparecer en el futuro, ya que funciona muy bien para proyectos específicos (en general, no muy complejos y no grandes, pero existen muchas excepciones a esa regla).

El enfoque orientado a objetos es bastante joven (mucho más joven que el enfoque procedimental) y es particularmente útil cuando se aplica a proyectos grandes y complejos llevados a cabo por grandes equipos formados por muchos desarrolladores.

Este tipo de programación en un proyecto facilita muchas tareas importantes, por ejemplo, dividir el proyecto en partes pequeñas e independientes y el desarrollo independiente de diferentes elementos del proyecto.

Python es una herramienta universal para la programación procedimental y orientada a objetos. Se puede utilizar con éxito en ambos enfoques.

Además, puedes crear muchas aplicaciones útiles, incluso si no se sabe nada sobre clases y objetos, pero debes tener en cuenta que algunos de los problemas (por ejemplo, el manejo de la interfaz gráfica de usuario) puede requerir un enfoque estricto de objetos.

Afortunadamente, la programación orientada a objetos es relativamente simple."""

"""3.1.2 Enfoque procedimental versus el enfoque orientado a objetos
En el enfoque procedimental, es posible distinguir dos mundos diferentes y completamente separados: el mundo de los datos y el mundo del código. El mundo de los datos está poblado con variables de diferentes tipos, mientras que el mundo del código está habitado por códigos agrupados en módulos y funciones.

Las funciones pueden usar datos, pero no al revés. Además, las funciones pueden abusar de los datos, es decir, usar el valor de manera no autorizada (por ejemplo, cuando la función seno recibe el saldo de una cuenta bancaria como parámetro).

Los datos no pueden usar funciones. ¿Pero es esto completamente cierto? ¿Hay algunos tipos especiales de datos que puedan usar funciones?

Sí, los hay, los llamados métodos. Estas son funciones que se invocan desde dentro de los datos, no junto con ellos. Si puedes ver esta distinción, has dado el primer paso en la programación de objetos.

El enfoque orientado a objetos sugiere una forma de pensar completamente diferente. Los datos y el código están encapsulados juntos en el mismo mundo, divididos en clases.

Cada clase es como una receta que se puede usar cuando quieres crear un objeto útil. Puedes producir tantos objetos como necesites para resolver tu problema.

Cada objeto tiene un conjunto de rasgos (se denominan propiedades o atributos; usaremos ambas palabras como sinónimos) y es capaz de realizar un conjunto de actividades (que se denominan métodos).

Las recetas pueden modificarse si son inadecuadas para fines específicos y, en efecto, pueden crearse nuevas clases. Estas nuevas clases heredan propiedades y métodos de los originales, y generalmente agregan algunos nuevos, creando nuevas herramientas más específicas."""