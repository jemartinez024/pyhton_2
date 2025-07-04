"""
4.5.21 RESUMEN DE SECCIÓN
1. Para crear un objeto date, debes pasar los argumentos de año, mes y día de la siguiente manera:


from datetime import date
 
my_date = date(2020, 9, 29)
print("Año:", my_date.year) # Año: 2020
print("Mes:", my_date.month) # Mes: 9
print("Día:", my_date.day) # Día: 29
 
El objeto date tiene tres atributos (de solo lectura): año, mes y día.


2. El método today devuelve un objeto de fecha que representa la fecha local actual:


from datetime import date
print("Hoy:", date.today()) # Muestra: Hoy: 2020-09-29
 

3. En Unix, la marca de tiempo expresa el número de segundos desde el 1 de Enero de 1970 a las 00:00:00 (UTC). Esta fecha se llama la "época de Unix", porque ahí comenzó el conteo del tiempo en los sistemas Unix. La marca de tiempo es en realidad la diferencia entre una fecha en particular (incluida la hora) y el 1 de Enero de 1970, 00:00:00 (UTC), expresada en segundos. Para crear un objeto de fecha a partir de una marca de tiempo, debemos pasar una marca de tiempo Unix al método fromtimestamp:


from datetime import date
import time
 
timestamp = time.time()
d = date.fromtimestamp(timestamp)
 

Nota: La función time devuelve el número de segundos desde el 1 de Enero de 1970 hasta el momento actual en forma de número punto flotante.

4. El constructor de la clase time acepta seís argumentos (hour, minute, second, microsecond, tzinfo, y fold). Cada uno de estos argumentos es opcional.


from datetime import time
 
t = time(13, 22, 20)
 
print("Hora:", t.hour) # Hora: 13
print("Minuto:", t.minute) # Minuto: 22
print("Segundo:", t.second) # Segundo: 20
 

5. El módulo time contiene la función sleep, que suspende la ejecución del programa durante un número determinado de segundos, por ejemplo:


import time
 
time.sleep(10)
print("¡Hola Mundo!") # Este texto se mostrará después de 10 segundos.
 

6. En el módulo datetime, la fecha y la hora se pueden representar como objetos separados o como un solo objeto. La clase que combina fecha y hora se llama datetime. Todos los argumentos pasados al constructor van a atributos de clase de solo lectura. Son year, month, day, hour, minute, second, microsecond, tzinfo, y fold:


from datetime import datetime
 
dt = datetime(2020, 9, 29, 13, 51)
print("Fecha y Hora:", dt) # Muestra: Fecha y Hora: 2020-09-29 13:51:00
 

7. El método strftime toma solo un argumento en forma de cadena que especifica un formato que puede constar de directivas. Una directiva es una cadena que consta del carácter % (porcentaje) y una letra minúscula o mayúscula. A continuación se muestran algunas directivas útiles:

%Y: devuelve el año con el siglo como número decimal.
%m: devuelve el mes como un número decimal con relleno de ceros.
%d: devuelve el día como un número decimal con relleno de ceros.
%H: devuelve la hora como un número decimal con relleno de ceros.
%M: devuelve el minuto como un número decimal con relleno de ceros.
%S: devuelve el segundo como un número decimal con relleno de ceros.
Ejemplo:


from datetime import date
 
d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Muestra: 2020/09/29
 

8. Es posible realizar cálculos en los objetos date y datetime, por ejemplo:


from datetime import date
 
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
 
d = d1 - d2
print(d) # Muestra: 366 days, 0:00:00.
print(d * 2) # Muestra: 732 days, 0:00:00.
 

El resultado de la resta se devuelve como un objeto timedelta que expresa la diferencia en días entre las dos fechas en el ejemplo anterior.

Toma en cuenta que también se muestra la diferencia en horas, minutos y segundos. El objeto timedelta se puede utilizar para realizar más cálculos (por ejemplo, puedes multiplicarlo por 2)."""