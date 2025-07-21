"""""identify

from mod import fun

mod:fun(2)
from mod import I

"""

"""import math
print(dir(math))"""

"""# archivo a.py
print("a", end='')

# archivo b.py
import a
print("b", end='')

# archivo c.py
print("c", end='')
import a
import b

"""

"""try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
"""

#for line in open('text.txt', 'rt'):
"""var = 
assert var != 0
print(var)

x = "\\\"
print(len(x))
"""
"""print(chr(ord('p') + 2))

print(float("1.3"))

class Class:
    def __init__(self, val=0):
        pass

object = Class()




class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)



class A:
    A = 1
    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))

class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C))
"""


"""class A:
    def __init__(self, v):
        self.__a = v + 1


a = A(0)
print(a.__a"""



"""class A:
    def __init__(self):
        pass


a = A(1)
print(hasattr(a, 'A'))
"""


"""class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()

try:
    raise Exception(1, 2, 3)
except Exception as e:
     print(len(e.args))

def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in my_fun(2):
    print(x, end='')



class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')

def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

numbers = [0, 2, 7, 9, 10]
foo = map(lambda num: num **2, numbers)
# Inserta la línea de código aquí.
print(list(foo))

numbers = [i*i for i in range(5)]
foo = list(filter(lambda x: x % 2, numbers)) # Inserta la línea de código aquí.
print(foo)"""



"""import random

a = random.randint(0, 100)
b = random.choice(0 , 100, 3)
c = random.randrange(10, 100,3)


print(a, b, c)"""

      
      

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)
