# Demostración del método isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

"""El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True (verdadero) o False (falso) de acuerdo al resultado.

"""

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

"""Ejecútalos y verifica su salida.

Nota: la causa del primer resultado es un espacio, no es ni un dígito ni una letra."""