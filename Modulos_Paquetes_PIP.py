"""1.2.1 Trabajando con módulos estándar
Antes de comenzar a revisar algunos módulos estándar de Python, veamos la función dir(). No tiene nada que ver con el comando dir de las terminales de Windows o Unix. El comando dir() no muestra el contenido de un directorio o carpeta de disco, pero no se puede negar que hace algo similar - puede revelar todos los nombres proporcionados a través de un módulo en particular.

Existe una condición: el módulo debe haberse importado previamente como un todo (es decir, utilizar la instrucción import module - from module no es suficiente).

La función devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:


dir(module)
  
Nota: Si el nombre del módulo tiene un alias, debes usar el alias, no el nombre original.

Usar la función dentro de un script normal no tiene mucho sentido, pero aún así, es posible.

Por ejemplo, se puede ejecutar el siguiente código para imprimir los nombres de todas las entidades dentro del módulo math:


import math
  
for name in dir(math):
  print(name, end="∖t")
El código del ejemplo debería producir el siguiente resultado:

__doc__ __loader__ __name__ __package__ __spec__ acos acosh asin asinh atan atan2
atan2 atanh ceil copysign cos cosh degrees e erf erfc exp expm1 fabs factorial floor
fmod frexp fsum gamma hypot isfinite isinf isnan ldexp lgamma log log10 log1p
log2 modf pi pow radians sin sinh sqrt tan tanh trunc
Output
¿Has notado los nombres extraños que comienzan con __ al inicio de la lista? Se hablará más sobre ellos cuando hablemos sobre los problemas relacionados con la escritura de módulos propios.

Algunos de los nombres pueden traer recuerdos de las lecciones de matemáticas, y probablemente no tendrás ningún problema en adivinar su significado.

El emplear la función dir() dentro de un código puede no parecer muy útil; por lo general, se desea conocer el contenido de un módulo en particular antes de escribir y ejecutar el código.

Afortunadamente, se puede ejecutar la función directamente en la consola de Python (IDLE), sin necesidad de escribir y ejecutar un script por separado.

Así es como se puede hacer:


import math
dir(math)
Deberías de ver algo similar a esto:

"""

"""1.2.2 Funciones selectas del módulo math
Comencemos con una vista previa de algunas de las funciones proporcionadas por el módulo math.

Se han elegido algunas arbitrariamente, pero esto no significa que las funciones no mencionadas aquí sean menos significativas. Tómate el tiempo para revisar las demás por ti mismo - no tenemos el espacio ni el tiempo para hablar de todas a detalle.

El primer grupo de funciones de módulo math están relacionadas con trigonometría:

sin(x) → el seno de x.
cos(x) → el coseno de x.
tan(x) → la tangente de x.
Todas estas funciones toman un argumento (una medida de ángulo expresada en radianes) y devuelven el resultado apropiado (ten cuidado con tan() - no todos los argumentos son aceptados).

Por supuesto, también están sus versiones inversas:

asin(x) → el arcoseno de x.
acos(x) → el arcocoseno de x.
atan(x) → el arcotangente de x.
Estas funciones toman un argumento (verifican que sea correcto) y devuelven una medida de un ángulo en radianes.

Para trabajar eficazmente con mediciones de ángulos, el módulo math proporciona las siguientes entidades:

pi → una constante con un valor que es una aproximación de π.
radians(x) → una función que convierte x de grados a radianes.
degrees(x) → una función que convierte x de radianes a grados.
Ahora observa el código en el editor. El programa de ejemplo no es muy sofisticado, pero ¿puedes predecir sus resultados?"""

"""from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)"""
    

"""Además de las funciones circulares (enumeradas anteriormente), el módulo math también contiene un conjunto de sus análogos hiperbólicos:

sinh(x) → el seno hiperbólico.
cosh(x) → el coseno hiperbólico.
tanh(x) → la tangente hiperbólica.
asinh(x) → el arcoseno hiperbólico.
acosh(x) → el arcocoseno hiperbólico.
atanh(x) → el arcotangente hiperbólico.
Existe otro grupo de las funciones math relacionadas con la exponenciación:

e → una constante con un valor que es una aproximación del número de Euler (e)
exp(x) → encontrar el valor de ex.
log(x) → el logaritmo natural de x.
log(x, b) → el logaritmo de x con base b.
log10(x) → el logaritmo decimal de x (más preciso que log(x, 10))
log2(x) → el logaritmo binario de x (más preciso que log(x, 2))
Nota: la función pow():

pow(x, y) → fencuentra el valor de xy (toma en cuenta los dominios).
Esta es una función incorporada y no se tiene que importar.

Observa el código en el editor. ¿Puedes predecir su salida?

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

El último grupo consta de algunas funciones de propósito general como:

ceil(x) → devuelve el entero más pequeño mayor o igual que x.
floor(x) → el entero más grande menor o igual que x.
trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
Observa el código en el editor. Analiza el programa cuidadosamente.

Demuestra las diferencias fundamentales entre ceil(), floor() y trunc().


from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))"""



"""1.2.3 ¿Existe aleatoriedad real en las computadoras?
Otro módulo que vale la pena mencionar es el que se llama random, que significa aleatorio.

Ofrece algunos mecanismos que permiten operar con números pseudoaleatorios.

Toma en cuenta el prefijo pseudo - los números generados por los módulos pueden parecer aleatorios en el sentido de que no se pueden predecir, pero no hay que olvidar que todos se calculan utilizando algoritmos muy refinados.

Los algoritmos no son aleatorios, son deterministas y predecibles. Solo aquellos procesos físicos que se salgan completamente de nuestro control (como la intensidad de la radiación cósmica) pueden usarse como fuente de datos aleatorios reales. Los datos producidos por computadoras deterministas no pueden ser aleatorios de ninguna manera.

Un generador de números aleatorios toma un valor llamado semilla, lo trata como un valor de entrada, calcula un número "aleatorio" basado en él (el método depende de un algoritmo elegido) y produce una nueva semilla.

La duración de un ciclo en el que todos los valores semilla son únicos puede ser muy largo, pero no es infinito: tarde o temprano los valores iniciales comenzarán a repetirse y los valores generadores también se repetirán. Esto es normal. Es una característica, no un error.

El valor de la semilla inicial, establecido durante el inicio del programa, determina el orden en que aparecerán los valores generados.


El factor aleatorio del proceso puede ser aumentado al establecer la semilla tomando un número de la hora actual - esto puede garantizar que cada ejecución del programa comience desde un valor semilla diferente (por lo tanto, usará diferentes números aleatorios).

Afortunadamente, Python realiza dicha inicialización al importar el módulo.


1.2.4 Funciones selectas del módulo random

La función random
La función general llamada random() (no debe confundirse con el nombre del módulo) produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).

El programa de ejemplo a continuación producirá cinco valores pseudoaleatorios - ya que sus valores están determinados por el valor semilla actual (bastante impredecible), no puedes adivinarlos:


from random import random

for i in range(5):
  print(random())
    

from random import random

for i in range(5):
  print(random())
    
Ejecuta el programa. Esto es lo que tenemos:
  
PS C:\Users\jemartinez\dev\Python_2> & C:/Users/jemartinez/AppData/Local/Programs/Python/Python313/python.exe c:/Users/jemartinez/dev/Python_2/Modulos_Paquetes_PIP.py
0.2796269428519822
0.08771334882386561
0.6699090503135905
0.5523039024745945
0.7744229321980444
PS C:\Users\jemartinez\dev\Python_2> & C:/Users/jemartinez/AppData/Local/Programs/Python/Python313/python.exe c:/Users/jemartinez/dev/Python_2/Modulos_Paquetes_PIP.py
0.9023113674518802
0.05591535919503998
0.5318323458471206
0.7696962978475601
0.11942378324987957
PS C:\Users\jemartinez\dev\Python_2> & C:/Users/jemartinez/AppData/Local/Programs/Python/Python313/python.exe c:/Users/jemartinez/dev/Python_2/Modulos_Paquetes_PIP.py
0.7026155477161776
0.623302479524357
0.5125891469839027
0.5082799392062859
0.5929858280821544


La función seed
La función seed() es capaz de directamente establecer la semilla del generador. Te mostramos dos de sus variantes:

seed() - establece la semilla con la hora actual.
seed(int_value) - establece la semilla con el valor entero int_value.
Hemos modificado el programa anterior; de hecho, hemos eliminado cualquier rastro de aleatoriedad del código:

from random import random, seed

seed(0)

for i in range(5):
  print(random())


from random import random, seed

seed(0)

for i in range(5):
  print(random())

Debido al hecho de que la semilla siempre se establece con el mismo valor, la secuencia de valores generados siempre se ve igual.

Ejecuta el programa. Esto es lo que tenemos:

0.844421851525
0.75795440294
0.420571580831
0.258916750293
0.511274721369
Output
¿Y tú?

Nota: tus valores pueden ser ligeramente diferentes si tu sistema utiliza aritmética de punto flotante más precisa o menos precisa, pero la diferencia se verá bastante lejos del punto decimal."""


"""Las funciones randrange y randint
Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

randrange(fin)
randrange(inicio, fin)
randrange(inicio, fin, incremento)
randint(izquiera, derecha)
Las primeras tres invocaciones generarán un valor entero tomado (pseudoaleatoriamente) del rango:

range(fin)
range(inicio, fin)
range(inicio, fin, incremento)
Toma en cuenta la exclusión implícita del lado derecho.

La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).

Observa el código en el editor. Este programa generará una línea que consta de tres ceros y un cero o un uno en el cuarto lugar.




"""




"""Tanto randrange como randint pertenecen al módulo random en Python y sirven para generar números aleatorios, pero tienen diferencias clave.

1️⃣ randint(a, b)
Genera un número entero aleatorio entre a y b, incluyendo ambos extremos.

📌 Sintaxis:

random.randint(a, b)

📌 Ejemplo:

import random

num = random.randint(1, 10)
print(num)  # Puede imprimir cualquier número del 1 al 10 (incluyendo ambos extremos)

✅ Incluye tanto 1 como 10 en el rango de valores posibles.

2️⃣ randrange(start, stop, step)
Genera un número entero aleatorio dentro de un rango, pero excluye el límite superior (stop).
Además, permite especificar un step (incremento).

📌 Sintaxis:

random.randrange(start, stop, step)

📌 Ejemplo sin step:

import random

num = random.randrange(1, 10)  
print(num)  # Puede imprimir un número entre 1 y 9 (NO incluye el 10)

✅ Incluye 1, pero NO el 10.

📌 Ejemplo con step:

import random

num = random.randrange(1, 10, 2)  # Solo tomará números impares: 1, 3, 5, 7, 9
print(num)

✅ Incluye números dentro del rango con incrementos de 2 (1, 3, 5, 7, 9).

🔎 Diferencias clave

Función	                    Incluye el límite superior	      Soporta step
randint(a, b)	                ✅ Sí (incluye b)	               ❌ No
randrange(start, stop, step)	❌ No (excluye stop)	             ✅ Sí

📌 Ejemplo de comparación:

import random

print(random.randint(1, 10))    # Puede imprimir: 1, 2, 3, ..., 10
print(random.randrange(1, 10))  # Puede imprimir: 1, 2, 3, ..., 9

📌 ¿Cuándo usar cada una?

✔ Si quieres un número aleatorio dentro de un rango exacto, usa randint().
✔ Si necesitas un número con un salto específico (por ejemplo, solo pares o impares), usa randrange()."""



"""🔹 choice(seq)
📌 Devuelve un solo elemento aleatorio de una secuencia (lista, tupla, cadena, etc.).

📌 Sintaxis:

random.choice(seq)

📌 Ejemplo:

import random

colores = ["rojo", "azul", "verde", "amarillo"]
color_aleatorio = random.choice(colores)

print(color_aleatorio)  # Puede imprimir "rojo", "azul", "verde" o "amarillo"
✅ Usar choice() es útil cuando solo necesitas seleccionar UN elemento al azar."""



"""🔹 sample(seq, k)
📌 Devuelve una lista con k elementos aleatorios SIN repetición.

📌 Sintaxis:

random.sample(seq, k)

📌 Donde:

seq: La secuencia de la que se seleccionarán los elementos.
k: El número de elementos a seleccionar (debe ser menor o igual a la cantidad total de elementos en seq).

📌 Ejemplo:

import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seleccion = random.sample(numeros, 3)

print(seleccion)  # Puede imprimir algo como [3, 7, 1]
✅ Los elementos en la lista de salida no se repiten.
❌ Si k es mayor que la longitud de seq, Python generará un error.

📌 Diferencias clave entre choice() y sample()

Función	     ¿Cuántos elementos selecciona?	     ¿Permite repetir elementos?
choice()	   1 solo elemento	                   No aplica (solo selecciona uno)
sample()	   k elementos	                       ❌ No (sin repetición)

🔹 ¿Cuándo usar cada una?
✔ Si solo necesitas elegir UN elemento al azar, usa choice().
✔ Si necesitas varios elementos sin repetición, usa sample().

📌 Ejemplo de comparación:

import random

frutas = ["manzana", "banana", "cereza", "durazno", "pera"]

# Un solo elemento aleatorio
print(random.choice(frutas))  # Ejemplo: "banana"

# Tres elementos aleatorios sin repetición
print(random.sample(frutas, 3))  # Ejemplo: ['pera', 'cereza', 'manzana']"""

"""1.2.6 Funciones selectas del módulo platform
La función platform
El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform. Simplemente devuelve una cadena que describe el entorno; por lo tanto, su salida está más dirigida a los humanos que al procesamiento automatizado (lo verás pronto).

Así es como se puede invocar:


platform(aliased = False, terse = False)
 
Y ahora:

aliased → cuando se establece a True (o cualquier valor distinto a cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.
terse → cuando se establece a True (o cualquier valor distinto a cero) puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).
Ejecutamos el programa:


from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))
 
usando tres plataformas diferentes, esto es lo que se obtuvo:

Intel x86 + Windows ® Vista (32 bit):
Windows-Vista-6.0.6002-SP2
Windows-Vista-6.0.6002-SP2
Windows-Vista
Output
Intel x86 + Gentoo Linux (64 bit):
Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-glibc2.3.4
Output
Raspberry PI2 + Raspbian Linux (32 bit)
Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
Linux-4.4.0-1-rpi2-armv7l-with-glibc2.9
Output
También puedes ejecutar el programa en el IDLE de tu máquina local para verificar que salida tendrá.

La función machine
En ocasiones, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código, una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena.

Nuevamente, ejecutamos el programa:


from platform import machine
 
print(machine())
en tres plataformas diferentes:

Intel x86 + Windows ® Vista (32 bit):
x86
Output
Intel x86 + Gentoo Linux (64 bit):
x86_64
Output
Raspberry PI2 + Raspbian Linux (32 bit):
armv7l
Output
La función processor
La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).

Una vez más, ejecutamos el programa:


from platform import processor
 
print(processor())
en tres plataformas diferentes:

Intel x86 + Windows ® Vista (32 bit):
x86
Output
Intel x86 + Gentoo Linux (64 bit):
Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz
Output
Raspberry PI2 + Raspbian Linux (32 bit):
armv7l
Output
Prueba esto en tu máquina local.

La función system
Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.


from platform import system
 
print(system())
 
Nuestras plataformas de ejemplo se presentan de la siguiente manera:

Intel x86 + Windows ® Vista (32 bit):
Windows
Output
Intel x86 + Gentoo Linux (64 bit):
Linux
Output
Raspberry PI2 + Raspbian Linux (32 bit):
Linux
Output
La función version
La versión del sistema operativo se proporciona como una cadena por la función version().


from platform import version
 
print(version())
 
Ejecuta el código y verifica su salida. Esto es lo que tenemos:

Intel x86 + Windows ® Vista (32 bit):
6.0.6002
Output
Intel x86 + Gentoo Linux (64 bit):
#1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017
Output
Raspberry PI2 + Raspbian Linux (32 bit):
#1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)
Output
Las funciones python_implementation y python_version_tuple
Si necesitas saber que versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas, aquí hay dos de ellas:

python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
La parte mayor de la versión de Python.
La parte menor.
El número del nivel de parche.

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
print(atr)

Nuestro programa de ejemplo produjo el siguiente resultado:

CPython
3
7
7
Output
Es muy probable que tu versión de Python sea diferente.
"""

"""1.2.7 Índice de Módulos en Python
Aquí solo hemos cubierto los conceptos básicos de los módulos de Python. Los módulos de Python conforman su propio universo, en el que Python es solo una galaxia, y nos aventuraríamos a decir que explorar las profundidades de estos módulos puede llevar mucho más tiempo que familiarizarse con Python “puro”.

Además, la comunidad de Python en todo el mundo crea y mantiene cientos de módulos adicionales utilizados en aplicaciones muy específicas como la genética, la psicología o incluso la astrología.

Estos módulos no están (y no serán) distribuidos junto con Python, o a través de canales oficiales, lo que hace que el universo de Python sea más amplio, casi infinito.

Puedes leer sobre todos los módulos estándar de Python aquí: https://docs.python.org/3/py-modindex.html.


No te preocupes - no necesitarás todos estos módulos. Muchos de ellos son muy específicos.

Todo lo que se necesita hacer es encontrar los módulos que se desean y aprender a cómo usarlos. Es fácil.

En la siguiente sección veremos algo más. Te mostraremos cómo escribir tu propio módulo."""



"""
1.2.8 RESUMEN DE SECCIÓN
1. Una función llamada dir() puede mostrarte una lista de las entidades contenidas dentro de un módulo importado. Por ejemplo:


import os
dir(os)
Imprime una lista de todo el contenido del módulo os el cual, puedes usar en tu código.

2. El módulo math contiene más de 50 funciones y constantes que realizan operaciones matemáticas (como sine(), pow(), factorial()) o aportando valores importantes (como π y la constante de Euler e).

3. El módulo random agrupa más de 60 entidades diseñadas para ayudarte a usar números pseudoaleatorios. No olvides el prefijo “pseudo”, ya que no existe un número aleatorio real cuando se trata de generarlos utilizando los algoritmos de la computadora.

4. El módulo platform contiene alrededor de 70 funciones que te permiten sumergirte en las capas subyacentes del sistema operativo y el hardware. Usarlos te permite aprender más sobre el entorno en el que se ejecuta tu código.

5. El Índice de Módulos de Python https://docs.python.org/3/py-modindex.html es un directorio de módulos impulsado por la comunidad disponible en el universo de Python. Si deseas encontrar un módulo que se adapte a tus necesidades, comienza tu búsqueda allí."""



"""
1.2.9 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuál es el valor esperado de la variable result después de que se ejecuta el siguiente código?

import math
result = math.e == math.exp(1)
Ocultar
Verdadero
Pregunta 2: (Completa el enunciado) Establecer la semilla del generador con el mismo valor cada vez que se ejecuta tu programa garantiza que ...

Ocultar
... los valores pseudoaleatorios emitidos desde el módulo random serán exactamente los mismos.

Pregunta 3: ¿Cuál de las funciones del módulo platform utilizarías para determinar el nombre del CPU que corre dentro de tu computadora?

Ocultar
La función processor().

Pregunta 4: ¿Cuál es el resultado esperado del siguiente fragmento de código?

import platform
print(len(platform.python_version_tuple()))
Ocultar
3
"""

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())

for atr in python_version_tuple():
    print(atr)