"""3.6.3 Anatomía detallada de las excepciones
Echemos un vistazo más de cerca al objeto de la excepción, ya que hay algunos elementos realmente interesantes aquí (volveremos al tema pronto cuando consideremos las técnicas base de entrada y salida de Python, ya que su subsistema de excepción extiende un poco estos objetos).

La clase BaseException introduce una propiedad llamada args. Es una tupla diseñada para reunir todos los argumentos pasados al constructor de la clase. Está vacío si la construcción se ha invocado sin ningún argumento, o solo contiene un elemento cuando el constructor recibe un argumento (no se considera el argumento self aquí), y así sucesivamente.

Hemos preparado una función simple para imprimir la propiedad args de una manera elegante, puedes ver la función en el editor."""


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("mi excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

"""Hemos utilizado la función para imprimir el contenido de la propiedad args en tres casos diferentes, donde la excepción de la clase Exception es generada de tres maneras distintas. Para hacerlo más espectacular, también hemos impreso el objeto en sí, junto con el resultado de la invocación __str__().

El primer caso parece de rutina, solo hay el nombre Exception después de la palabra clave reservada raise. Esto significa que el objeto de esta clase se ha creado de la manera más rutinaria.

El segundo y el tercer caso pueden parecer un poco extraños a primera vista, pero no hay nada extraño, son solo las invocaciones del constructor. En la segunda sentencia raise, el constructor se invoca con un argumento, y en el tercero, con dos.

Como puedes ver, la salida del programa refleja esto, mostrando los contenidos apropiados de la propiedad args:

Output
:  :
mi excepción : mi excepción : mi excepción
('mi', 'excepción') : ('mi', 'excepción') : ('mi', 'excepción')"""