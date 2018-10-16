"""
mymod.myfile namespace
"""


def myfunc():
    """ a demonstration function """
    print("function imported from mymod.myfile")


def myfunc3():
    """ imported into the top level of the namespace in __init__.py """
    print("function imported into __init__.py")


def myfunc4():
    """ renamed by the import statement """
    print("function renamed into mf")
