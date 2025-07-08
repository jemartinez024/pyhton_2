"""Durante este curso, echamos un breve vistazo a la clase Calendar. Tu tarea ahora es ampliar su funcionalidad con un nuevo método llamado count_weekday_in_year, que toma un año y un día de la semana como parámetros, y luego devuelve el número de ocurrencias de un día de la semana específico en el año.

Utiliza los siguientes consejos:

Crea una clase llamada MyCalendar que se extiende de la clase Calendar.
Crea el método count_weekday_in_year con los parámetros de year y weekday. El parámetro weekday debe tener un valor entre 0 y 6, donde 0 es el lunes y 6 es el domingo. El método debe devolver el número de días como un número entero.
En tu implementación, usa el método monthdays2calendar de la clase Calendar.
Los siguientes son resultados esperados de ejemplo:

Argumentos de muestra

Output
year=2019, weekday=0
New Component Title
Salida esperada

Output
52

Argumentos de muestra

year=2000, weekday=6
Salida esperada

Output
53"""
import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        if weekday < 0 or weekday > 6:
            raise ValueError("weekday must be between 0 and 6")
        
        count = 0
        for month in range(1, 13):
            month_days = self.monthdays2calendar(year, month)
            for week in month_days:
                for day, day_weekday in week:
                    if day != 0 and day_weekday == weekday:
                        count += 1
        return count

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2000, calendar.SUNDAY)

print(number_of_days)