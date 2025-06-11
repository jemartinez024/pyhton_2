"""4.1.2 La sentencia yield
El protocolo iterador no es difícil de entender y usar, pero también es indiscutible que el protocolo es bastante inconveniente.

La principal molestia que tiene es que necesita guardar el estado de la iteración en las invocaciones subsecuentes de __iter__.

Por ejemplo, el iterador Fib se ve obligado a almacenar con precisión el lugar en el que se detuvo la última invocación (es decir, el número evaluado y los valores de los dos elementos anteriores). Esto hace que el código sea más grande y menos comprensible.

Es por eso que Python ofrece una forma mucho más efectiva, conveniente y elegante de escribir iteradores.

El concepto se basa fundamentalmente en un mecanismo muy específico proporcionado por la palabra clave reservada yield.

Se puede ver a la palabra clave reservada yield como un hermano más inteligente de la sentencia return, con una diferencia esencial.

Echa un vistazo a esta función:


def fun(n):
    for i in range(n):
        return i
 

Se ve extraño, ¿no? Está claro que el bucle for no tiene posibilidad de terminar su primera ejecución, ya que el return lo romperá irrevocablemente.

Además, invocar la función no cambiará nada: el bucle for comenzará desde cero y se romperá inmediatamente.

Podemos decir que dicha función no puede guardar y restaurar su estado en invocaciones posteriores.

Esto también significa que una función como esta no se puede usar como generador.

Hemos reemplazado exactamente una palabra en el código, ¿puedes verla?

def fun(n):
      for i in range(n):
         yield i
 

Hemos puesto yield en lugar de return. Esta pequeña enmienda convierte la función en un generador, y el ejecutar la sentencia yield tiene algunos efectos muy interesantes.

Primeramente, proporciona el valor de la expresión especificada después de la palabra clave reservada yield, al igual que return, pero no pierde el estado de la función.

Todos los valores de las variables están congelados y esperan la próxima invocación, cuando se reanuda la ejecución (no desde cero, como ocurre después de un return).

Hay una limitación importante: dicha función no debe invocarse explícitamente ya que no es una función; es un objeto generador.

La invocación devolverá el identificador del objeto, no la serie que esperamos del generador.

Debido a las mismas razones, la función anterior (la que tiene el return) solo se puede invocar explícitamente y no se debe usar como generador."""



def fun(n):
      for i in range(n):
         yield i
         
