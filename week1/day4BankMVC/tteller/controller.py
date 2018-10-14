""" Defines control flow of the TerminalTeller application

Homework reading: Read PEP 8 on code formatting and PEP 257 on docstrings.
"""

from tteller import view
from tteller import model


def loginloop():
    """ prompt the user to login, create an account or exit.

repeat the menu after a incorrect input or account creation
"""
    answer = view.accountmenu()

    if answer not in ["1", "2", "3"]:
        view.invalidinput()
        return loginloop()  # Recursion to repeat the menu.

    if answer == "1":  # login
        accountnumber, pin = view.loginprompt()
        if model.validate(accountnumber, pin):
            return accountnumber

        view.invalidaccount()
        return loginloop()

    if answer == "2":  # create account
        createaccount()
        return loginloop()

    if answer == "3":  # exit
        return None


def exitprogram():
    """ save data and exit the program """

    model.save()
    view.goodbye()
    quit()


def createaccount():
    """ Prompt a user for a first name, last name, and PIN

TODO: Stub Method: Prompt for the other fields.
"""

    firstname, lastname, pin = view.createaccount()
    accountnumber = model.generate_account_number()
    model.add_account(str(accountnumber), firstname, lastname, pin)
    view.creationconfirm(accountnumber)


def mainloop(accountnumber):
    """ Main menu loop. Check balance. Make deposit. Make withdrawal. Exit.

TODO: Stub Method: Create the full menu.
"""

    firstname, lastname = model.get_name(accountnumber)
    view.mainmenu(firstname)
    exitprogram()


def run():
    """ Main flow of the program. """

    model.initialize()
    accountnumber = loginloop()
    if not accountnumber:
        exitprogram()

    mainloop(accountnumber)
    exitprogram()


if __name__ == "__main__":
    run()
