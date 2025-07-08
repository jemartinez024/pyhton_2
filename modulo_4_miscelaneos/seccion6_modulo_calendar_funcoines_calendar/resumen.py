"""
4.6.14 RESUMEN DE SECCIÓN
1. En el módulo calendar, los días de la semana se muestran de lunes a domingo. Cada día de la semana tiene su representación en forma de número entero, donde el primer día de la semana (lunes) está representado por el valor 0, mientras que el último día de la semana (domingo) está representado por el valor 6.


2. Para mostrar un calendario de cualquier año, se emplea la función calendar con el año pasado como argumento, por ejemplo:

import calendar
print(calendar.calendar(2020))
 
Nota: Una buena alternativa a la función anterior es la función llamada prcal, que también toma los mismos parámetros que la función calendar, pero no requiere el uso de la función print para mostrar el calendario.


3. Para mostrar un calendario de cualquier mes del año, se emplea la función month, pasándole el año y el mes. Por ejemplo:


import calendar
print(calendar.month(2020, 9))
 
Nota: También puedes usar la función prmonth, que tiene los mismos parámetros que la función month, pero no requiere el uso de la función print para mostrar el calendario.


4. La función setfirstweekday te permite cambiar el primer día de la semana. Toma un valor de 0 a 6, donde 0 es domingo y 6 es sábado.


5. El resultado de la función weekday es un día de la semana como un valor entero para un año, mes y día determinados:


import calendar
print(calendar.weekday(2020, 9, 29)) # Esto muestra 1, que significa martes.
 

6. La función weekheader devuelve los nombres de los días de la semana en forma abreviada. El método weekheader requiere que se especifique el ancho en caracteres para un día de la semana. Si el ancho que proporciona es mayor que 3, aún se obtendrán los nombres abreviados de los días de la semana que constan de solo tres caracteres. Por ejemplo:


import calendar
print(calendar.weekheader(2)) # Esto muestra: Mo Tu We Th Fr Sa Su
 

7. Una función muy útil disponible en el módulo calendar es la función llamada isleap, que, como su nombre indica, te permite comprobar si el año es bisiesto o no.


print("¡Hola mundo!")

8. Puedes crear un objeto calendar tu mismo usando la clase Calendar, que al crear el objeto, te permite cambiar el primer día de la semana con el parámetro opcional firstweekday, por ejemplo:


import calendar
 
c = calendar.Calendar(2)
 
for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Resultado: 2 3 4 5 6 0 1
 
iterweekdays devuelve un iterador para los números de los días de la semana. El primer valor devuelto siempre es igual al valor de la propiedad firstweekday."""