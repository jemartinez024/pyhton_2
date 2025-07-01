"""4.5.15 Dando formato a la fecha y hora
Todas las clases del módulo datetime presentadas hasta ahora tienen un método llamado strftime. Este es un método muy importante, porque nos permite devolver la fecha y la hora en el formato que especificamos.

El método strftime toma solo un argumento en forma de cadena que especifica un formato que puede constar de directivas.

Una directiva es una cadena que consta del carácter % (porcentaje) y una letra minúscula o mayúscula. Por ejemplo, la directiva %Y significa el año con el siglo como número decimal. Veámoslo en un ejemplo. Ejecuta el código en el editor."""

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

"""Resultado:

Output
2020/01/04
En el ejemplo, hemos pasado un formato que consta de tres directivas separadas por / (diagonal) al método strftime. Por supuesto, el carácter separador se puede reemplazar por otro carácter, o incluso por una cadena.

Puedes poner cualquier carácter en el formato, pero solo las directivas reconocibles se reemplazarán con los valores apropiados. En nuestro formato, hemos utilizado las siguientes directivas:

%Y: devuelve el año con el siglo como número decimal. En nuestro ejemplo, esto es 2020.
%m: devuelve el mes como un número decimal con relleno de ceros. En nuestro ejemplo, es 01.
%d: devuelve el día como un número decimal con relleno de ceros. En nuestro ejemplo, es 04.
Nota: Puedes encontrar todas las directivas disponibles: aquí.

El formato de hora funciona de la misma forma que el formato de fecha, pero requiere el uso de directivas adecuadas. Echemos un vistazo más de cerca a algunos de ellos en el editor."""