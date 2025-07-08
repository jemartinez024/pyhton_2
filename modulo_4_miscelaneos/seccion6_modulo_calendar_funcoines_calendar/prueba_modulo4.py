my_list = [1, 2, 3]
foo = tuple(map(lambda x: x**x, my_list))# Insertar línea de código aquí.
print(foo)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x>1, my_tuple)) # Insertar línea de código aquí.
print(foo)

def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x, end='')

