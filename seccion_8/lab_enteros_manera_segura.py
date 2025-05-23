"""2.8.2   LAB   Leyendo enteros de manera segura
Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado.

La función deberá:

Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
Si el valor de entrada es válido, será regresado como resultado.
Datos de Prueba
Prueba tu código cuidadosamente.

Así es como la función debería reaccionar ante la entrada del usuario:

Ingresa un numero entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1"""

def read_int(prompt, min, max):
    while True:
        text = input("Ingresa un numero entre -10 a 10: ")
        try:
            value = int(text)    
        except ValueError:
            print("Error: entrada incorrecta")
        #continue

        if value < min or value > max:
            print("Error: el valor no está dentro del rango permitido (-10..10")
        else:
            return value
            
value = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
5
print("El número es:", value)



