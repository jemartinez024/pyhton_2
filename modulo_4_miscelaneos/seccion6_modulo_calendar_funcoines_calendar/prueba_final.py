"""identify

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
print(chr(ord('p') + 2))

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

