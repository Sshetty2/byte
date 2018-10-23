"""
Controller for the demonstration nonsense app.
"""

from myapp.model import Datastore


class Controller():  # the () is option if not inheriting, but I like them

    data = Datastore()

    def __init__(self):
        """ called when you create a new instance of the class """
        self.data.pushelement("item 1")
        self.data.pushelement("item 2")
        self.data.pushelement("item 3")

    def run(self):
        """ input loop """

        while True:
            print("""Options:
1: Add element
2: Get element
3: Get all elements
4: Exit

: """, end="")
            answer = input()

            if answer in ["1", "2", "3", "4"]:
                if answer == "1":
                    self.data.pushelement(self.newitemprompt())

                elif answer == "2":
                    index = self.indexprompt()
                    print(self.data[index])

                elif answer == "3":
                    print()
                    for element in self.data:
                        print(element)

                elif answer == "4":
                    return

            print()

    def newitemprompt(self):
        print("\nInput a string: ", end="")
        return input()

    def indexprompt(self):
        print("\nInput the index: ", end="")
        return input()
