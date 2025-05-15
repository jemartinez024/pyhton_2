"""
2.3.24 CUESTIONARIO DE SECCIÓN
Pregunta 1: ¿Cuál es el resultado esperado del siguiente código?

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
 
Ocultar
ABC123xyx
Pregunta 2: ¿Cuál es el resultado esperado del siguiente código?

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
print(s2[-2])
 
Ocultar
of
Pregunta 3: ¿Cuál es el resultado esperado del siguiente código?

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)
 
Ocultar
Where*are*the*snows?
Pregunta 4: ¿Cuál es el resultado esperado del siguiente código?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
 
Ocultar
It is either hard or possible"""