"""
__init__.py in a directory defines names in the top level of a module's
namespace.

if variablename is defined in
./module/__init__.py

it can be accessed as module.variablename

you can move a name defined in another file into the top namespace with an
import statement.
"""

from mymod.myfile import myfunc3
from mymod.internal import callme


def myfunc2():
    """ function demonstrating __init__.py """
    print("myfunc2 imported from variablename")


def myfunc5():
    print("the value of the imported callme() function :", callme())
MYCONST = "constants are ususally defined in __init__.py"
