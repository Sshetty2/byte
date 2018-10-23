"""
Model for the demonstration nonsense app
"""

from myapp.element import Element


class Datastore():

    elements = []

    def __init__(self):
        """ you can omit __init__ if nothing needs to be done. """
        pass

    def pushelement(self, value):
        """ add an Element object to elements """
        self.elements.append(Element(value))

    def __getitem__(self, index):
        """ define the behavior for [] """
        return str(self.elements[int(index)])

    def __len__(self):
        return len(self.elements)

    def __str___(self):
        return "<Datastore len={)>".format(len(self))
