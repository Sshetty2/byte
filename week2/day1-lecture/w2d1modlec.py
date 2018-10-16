"""

Week 2 Day 1 Lecture

Modules pt 2 and Classes pt 1

"""

import mymod
import mymod.myfile
from mymod import myfile
from mymod.myfile import myfunc
from mymod import myfunc2
from mymodimport myfunc3
from mymod.myfile import myfunc4 as mf

myfunc()
myfunc2()
myfile.myfunc()
myfunc3()
mf()
mymod.myfunc5()

print()
print("imported constant: ", mymod.MYCONST)
print()
print("__name__ values:")

print("name of executed file: ", __name__)
print("name of mymod.__name__: ", mymod.__name__)
print("name of mymod.myfile.__name__: ", mymod.myfile.__name__)
print("name of myfile.__name__ (different import): ", myfile.__name__)
