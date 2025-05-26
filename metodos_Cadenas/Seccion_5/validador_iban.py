"""El cuarto programa implementa (en una forma ligeramente simplificada) un algoritmo utilizado por los bancos Europeos para especificar los números de cuenta. El estándar llamado IBAN (Número de cuenta bancaria internacional) proporciona un método simple y bastante confiable para validar los números de cuenta contra errores tipográficos simples que pueden ocurrir durante la reescritura del número, por ejemplo, de documentos en papel, como facturas o facturas en las computadoras.

Puedes encontrar más detalles aquí: https://en.wikipedia.org/wiki/International_Bank_Account_Number.

Un número de cuenta compatible con IBAN consta de:

Un código de país de dos letras tomado del estándar ISO 3166-1 (por ejemplo, FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
Dos dígitos de verificación utilizados para realizar las verificaciones de validez: pruebas rápidas y simples, pero no totalmente confiables, que muestran si un número es inválido (distorsionado por un error tipográfico) o válido.
El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud de esa parte depende del país).
El estándar dice que la validación requiere los siguientes pasos (según Wikipedia):

(Paso 1) Verificar que la longitud total del IBAN sea correcta según el país (este programa no lo hará, pero puedes modificar el código para cumplir con este requisito si lo deseas; pero debes enseñar al código a conocer todas las longitudes utilizadas en Europa).
(Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es decir, el código del país y los dígitos de verificación).
(Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena, donde A = 10, B = 11 ... Z = 35.
(Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número dividiéndolo entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos y el IBAN puede ser válido.
Observa el código en el editor. Analicémoslo:"""

# Validador IBAN.

# Solicita al usuario que ingrese un IBAN.
iban = input("Ingresa un IBAN, por favor: ")

# Elimina los espacios en blanco que pueda tener el IBAN.
iban = iban.replace(' ','')  

# Verifica si el IBAN contiene únicamente caracteres alfanuméricos (letras y números).
if not iban.isalnum():  
    print("Has introducido caracteres no válidos.")

# Verifica si el IBAN tiene una longitud menor a la mínima (15 caracteres).
elif len(iban) < 15:  
    print("El IBAN ingresado es demasiado corto.")

# Verifica si el IBAN tiene una longitud mayor a la máxima (31 caracteres).
elif len(iban) > 31:  
    print("El IBAN ingresado es demasiado largo.")

# Si pasa todas las validaciones anteriores, se procede con el cálculo.
else:
    # Reorganiza el IBAN: mueve los 4 primeros caracteres al final y convierte todo a mayúsculas.
    iban = (iban[4:] + iban[0:4]).upper()

    # Se creará una nueva cadena 'iban2' que contendrá solo números.
    iban2 = ''
    
    # Convierte cada carácter a número:
    for ch in iban:
        if ch.isdigit():
            # Si el carácter ya es un número, se agrega tal cual.
            iban2 += ch
        else:
            # Si es una letra, se convierte a un número según la fórmula: A = 10, B = 11, ..., Z = 35.
            iban2 += str(10 + ord(ch) - ord('A'))
    
    # Convierte toda la cadena 'iban2' a un número entero para hacer la validación final.
    iban = int(iban2)

    # Si el número es divisible entre 97 y el residuo es 1, el IBAN es válido.
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

"""Agreguemos algunos datos de prueba (todos estos números son válidos; puedes invalidarlos cambiando cualquier carácter).

Inglés: GB72 HBZU 7006 7212 1253 00
Francés: FR76 30003 03620 00020216907 50
Alemán: DE02100100100152517108
Si eres residente de la UE, puedes usar tu propio número de cuenta para hacer pruebas."""