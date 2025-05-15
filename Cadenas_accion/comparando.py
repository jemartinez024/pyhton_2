"""2.4.1 Comparando cadenas
Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.

Observa estos operadores, también sirven para comparar cadenas:

==
!=
>
>=
<
<=
Existe un "pero": los resultados de tales comparaciones a veces pueden ser un poco sorprendentes. No olvides que Python no es consciente (no puede serlo de ninguna manera) de problemas lingüísticos sutiles, simplemente compara valores de puntos de código, carácter por carácter.

Los resultados que se obtienen de una operación de este tipo a veces son sorprendentes. Comencemos con los casos más simples.


Dos cadenas son iguales cuando consisten de los mismos caracteres en el mismo orden. Del mismo modo, dos cadenas no son iguales cuando no consisten de los mismos caracteres en el mismo orden.

Ambas comparaciones dan True (verdadero) como resultado:


'alpha' == 'alpha'
'alpha' != 'Alpha'
 

La relación entre cadenas se determina al comparar el primer carácter diferente en ambas cadenas (ten en cuenta los puntos de código ASCII / UNICODE en todo momento).

Cuando se comparan dos cadenas de diferentes longitudes y la más corta es idéntica a la más larga, la cadena más larga se considera mayor.

Justo como aquí:


'alpha' < 'alphabet'
 

La comparación es True (verdadera).

La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas se consideran menores en comparación con las minúsculas).

La expresión es True (verdadera):


'beta' > 'Beta'
 
Aún si una cadena contiene solo dígitos, todavía no es un número. Se interpreta como lo que es, como cualquier otra cadena regular, y su aspecto numérico (potencial) no se toma en cuenta, en ninguna manera.

Observa los ejemplos:"""

print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')


"""Producen los siguientes resultados:

False
True
False
True
True"""

"""El comparar cadenas con los números generalmente es una mala idea.

Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas por los operadores == y !=. El primero siempre devuelve False (falso), mientras que el segundo siempre devuelve True (verdadero).

El uso de cualquiera de los operadores de comparación restantes generará una excepción TypeError.

Vamos a verlo:"""

print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
print('10' > 10)


"""Los resultados en este caso son:

False
True
False
True
TypeError exception
Output

Ejecuta todos los ejemplos y realiza más experimentos"""
