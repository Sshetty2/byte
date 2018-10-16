""" TerminalTeller views """

# from getpass import getpass


def accountmenu():
    """ Display login / account creation options """
    print(
        """Input your choice:
    1. Login
    2. Create an account
    3. Exit

Input your selection: """,
        end="")
    return input()


def invalidinput():
    """ Display invalid input error. """

    print("\n\t\tERROR: Invalid input.\n")


def invalidaccount():
    """ Account number / PIN incorrect error. """

    print("\n\t\tInvalid credentials.")


def createaccount():
    """ Prompt returning firstname, lastname, and PIN

TODO: Stub method, finish this.
Look at the getpass method of the getpass module for private input.
"""

    print("Input first name for new account: ", end="")
    firstname = input()
    return firstname, None, None


def creationconfirm(accountnumber):
    """ Display account number after successful creation """

    print("\t\tAccount created, your account number is {}.".format(
        accountnumber))


def loginprompt():
    """ Login prompt, return accountnumber, pin

TODO: Stub method, finish this
"""
    print("Input your account number: ", end="")
    accountnumber = input()
    return accountnumber, None


def goodbye():
    """ Message displayed on exit. """

    print("\t\tThank you for using TerminalTeller!")


def mainmenu(name):
    """ Main menu, display all options and prompt for a selection

TODO: Stub method, finish this
"""
    print("Hello, {}".format(name))

# TODO: Add additional views as needed.
