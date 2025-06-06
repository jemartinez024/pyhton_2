"""3.6.2 Las excepciones son clases
Los ejemplos anteriores se centraron en detectar un tipo específico de excepción y responder de manera apropiada. Ahora vamos a profundizar más y mirar dentro de la excepción misma.

Probablemente no te sorprenderá saber que las excepciones son clases. Además, cuando se genera una excepción, se crea una instancia de un objeto de la clase y pasa por todos los niveles de ejecución del programa, buscando el bloque "except" que está preparado para tratar con la excepción.

Tal objeto lleva información útil que puede ayudarte a identificar con precisión todos los aspectos de la situación pendiente. Para lograr ese objetivo, Python ofrece una variante especial de la cláusula de excepción: puedes encontrarla en el editor."""

try:
    i = int("¡Hola!")
except Exception as e:
    print(e)
    print(e.__str__())
    
    """Como puedes ver, la sentencia except se extendió y contiene una frase adicional que comienza con la palabra clave reservada as, seguida por un identificador. El identificador está diseñado para capturar la excepción con el fin de analizar su naturaleza y sacar conclusiones adecuadas.

Nota: el alcance del identificador solo es dentro del except, y no va más allá.

El ejemplo presenta una forma muy simple de utilizar el objeto recibido: simplemente imprímelo (como puedes ver, la salida es producida por el método del objeto __str__()) y contiene un breve mensaje que describe la razón.

Se imprimirá el mismo mensaje si no hay un bloque except en el código, y Python se verá obligado a manejarlo por sí mismo.


Todas las excepciones integradas de Python forman una jerarquía de clases. Si lo deseas, puedes extenderlo sin problema.

Observa el código en el editor."""

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)


"""Este programa muestra todas las clases de excepción predefinidas en forma de árbol.

Como un árbol es un ejemplo perfecto de una estructura de datos recursiva, la recursión parece ser la mejor manera de recorrerlo. La función print_exception_tree() toma dos argumentos:

Un punto dentro del árbol desde el cual comenzamos a recorrerlo.
Un nivel de anidación (lo usaremos para construir un dibujo simplificado de las ramas del árbol).
Comencemos desde la raíz del árbol: la raíz de las clases de excepciones de Python es la clase BaseException (es una superclase de todas las demás excepciones).

Para cada una de las clases encontradas, se realiza el mismo conjunto de operaciones:

Imprimir su nombre, tomado de la propiedad __name__.
Iterar a través de la lista de subclases provistas por el método __subclasses__(), e invocar recursivamente la función print_exception_tree(), incrementando el nivel de anidación respectivamente.
Toma en cuenta como hemos dibujado las ramas. La impresión no está ordenada de alguna manera: si deseas un desafío, puedes intentar ordenarla tú mismo. Además, hay algunas imprecisiones sutiles en la forma en que se presentan algunas ramas. Eso también se puede arreglar, si lo deseas.

Así es como se ve:

Output
BaseException
    +---Exception
    |    +---TypeError
    |    +---StopAsyncIteration
    |    +---StopIteration
    |    +---ImportError
    |    |    +---ModuleNotFoundError
    |    |    +---ZipImportError
    |    +---OSError
    |    |    +---ConnectionError
    |    |    |    +---BrokenPipeError
    |    |    |    +---ConnectionAbortedError
    |    |    |    +---ConnectionRefusedError
    |    |    |    +---ConnectionResetError
    |    |    +---BlockingIOError
    |    |    +---ChildProcessError
    |    |    +---FileExistsError
    |    |    +---FileNotFoundError
    |    |    +---IsADirectoryError
    |    |    +---NotADirectoryError
    |    |    +---InterruptedError
    |    |    +---PermissionError
    |    |    +---ProcessLookupError
    |    |    +---TimeoutError
    |    |    +---UnsupportedOperation
    |    |    +---herror
    |    |    +---gaierror
    |    |    +---timeout
    |    |    +---Error
    |    |    |    +---SameFileError
    |    |    +---SpecialFileError
    |    |    +---ExecError
    |    |    +---ReadError
    |    +---EOFError
    |    +---RuntimeError
    |    |    +---RecursionError
    |    |    +---NotImplementedError
    |    |    +---_DeadlockError
    |    |    +---BrokenBarrierError
    |    +---NameError
    |    |    +---UnboundLocalError
    |    +---AttributeError
    |    +---SyntaxError
    |    |    +---IndentationError
    |    |    |    +---TabError
    |    +---LookupError
    |    |    +---IndexError
    |    |    +---KeyError
    |    |    +---CodecRegistryError
    |    +---ValueError
    |    |    +---UnicodeError
    |    |    |    +---UnicodeEncodeError
    |    |    |    +---UnicodeDecodeError
    |    |    |    +---UnicodeTranslateError
    |    |    +---UnsupportedOperation
    |    +---AssertionError
    |    +---ArithmeticError
    |    |    +---FloatingPointError
    |    |    +---OverflowError
    |    |    +---ZeroDivisionError
    |    +---SystemError
    |    |    +---CodecRegistryError
    |    +---ReferenceError
    |    +---BufferError
    |    +---MemoryError
    |    +---Warning
    |    |    +---UserWarning
    |    |    +---DeprecationWarning
    |    |    +---PendingDeprecationWarning
    |    |    +---SyntaxWarning
    |    |    +---RuntimeWarning
    |    |    +---FutureWarning
    |    |    +---ImportWarning
    |    |    +---UnicodeWarning
    |    |    +---BytesWarning
    |    |    +---ResourceWarning
    |    +---error
    |    +---Verbose
    |    +---Error
    |    +---TokenError
    |    +---StopTokenizing
    |    +---Empty
    |    +---Full
    |    +---_OptionError
    |    +---TclError
    |    +---SubprocessError
    |    |    +---CalledProcessError
    |    |    +---TimeoutExpired
    |    +---Error
    |    |    +---NoSectionError
    |    |    +---DuplicateSectionError
    |    |    +---DuplicateOptionError
    |    |    +---NoOptionError
    |    |    +---InterpolationError
    |    |    |    +---InterpolationMissingOptionError
    |    |    |    +---InterpolationSyntaxError
    |    |    |    +---InterpolationDepthError
    |    |    +---ParsingError
    |    |    |    +---MissingSectionHeaderError
    |    +---InvalidConfigType
    |    +---InvalidConfigSet
    |    +---InvalidFgBg
    |    +---InvalidTheme
    |    +---EndOfBlock
    |    +---BdbQuit
    |    +---error
    |    +---_Stop
    |    +---PickleError
    |    |    +---PicklingError
    |    |    +---UnpicklingError
    |    +---_GiveupOnSendfile
    |    +---error
    |    +---LZMAError
    |    +---RegistryError
    |    +---ErrorDuringImport
    +---GeneratorExit
    +---SystemExit
    +---KeyboardInterrupt
"""