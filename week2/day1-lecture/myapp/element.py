"""
Element for the demonstration nonsense app
"""

class Element():
    """ individual item in the data store """

    def __init__(self, value):
        """ attributes can be defined in any method. but they should almost
always all be set in the class definition or the __init__ method """
        self.value = value

    def __str__(self):
        return("Element: {}".format(self.value))
