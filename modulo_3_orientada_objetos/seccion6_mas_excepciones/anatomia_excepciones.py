"""3.6.3 Anatomía detallada de las excepciones
Echemos un vistazo más de cerca al objeto de la excepción, ya que hay algunos elementos realmente interesantes aquí (volveremos al tema pronto cuando consideremos las técnicas base de entrada y salida de Python, ya que su subsistema de excepción extiende un poco estos objetos).

La clase BaseException introduce una propiedad llamada args. Es una tupla diseñada para reunir todos los argumentos pasados al constructor de la clase. Está vacío si la construcción se ha invocado sin ningún argumento, o solo contiene un elemento cuando el constructor recibe un argumento (no se considera el argumento self aquí), y así sucesivamente.

Hemos preparado una función simple para imprimir la propiedad args de una manera elegante, puedes ver la función en el editor."""