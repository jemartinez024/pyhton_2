my_list = [1, 2, 3]
foo = tuple(map(lambda x: x**x, my_list))# Insertar línea de código aquí.
print(foo)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x>1, my_tuple)) # Insertar línea de código aquí.
print(foo)



def I():
    s = 'abcdef'
    for c in s[1::]:
        yield c


for x in I():
    print(x, end='')




def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='')



def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

b = bytearray(3)
print(b)

"""import os

os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd())"""

"""import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())"""



from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)

from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

from datetime import datetime  


print(datetime.now().timestamp())
