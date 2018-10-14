""" Data model for the TerminalTeller application """

import json
import os
from random import randint


# Locate the json file in the ttrader directory wherever the python
# executable is run. os.path is preferred to literal paths in strings
# because it can run on Linux, Mac, or Windows without changing
# code.
thisdir = os.path.dirname(os.path.realpath(__file__))
jsonfilename = "data.json"
JSONFILE = os.path.join(thisdir, jsonfilename)

# Note: keeping the data context of a module in a global variable will only
# work with very simple application:

# Global data store:
DATA = None
""" format of DATA:
{
    "4020000000000000": {
        "firstname": "Carter",
        "lastname": "Adams",
        "PIN": "1234",
        "balance": 3.50
    },
    "4025000000000000": { ... etc.
}
"""


def initialize():
    """ Koad DATA from permanent jsonfile or initialize empty DATA dict """

    # the global keyword allows a function to alter a global variabl
    global DATA
    if not os.path.isfile(JSONFILE):
        DATA = {}
        return

    with open(JSONFILE, "r") as file_object:
        DATA = json.load(file_object)


def save():
    """ Write the updated DATA to the permanent json store """

    with open(JSONFILE, "w") as file_object:
        json.dump(DATA, file_object)


def add_account(accountnumber, firstname, lastname, pin):
    """ add a new account to the DATA store """
    # q: Why is 'global' not needed here?

    DATA[accountnumber] = {
        "firstname": firstname,
        "lastname": lastname,
        "PIN": pin,
        "balance": 0.00
    }


def generate_account_number():
    """ Generates a new account number. Number is a Luhn-legal credit card #.

TODO: Stub method. Import your Luhn algorithm module from problem #1 and use
your generator method.
"""
    newnumber = None

    while newnumber in DATA or newnumber is None:  # use 'is None & not == None
        newnumber = randint(10000, 99999)
    return newnumber


def validate(accountnumber, pin):  # use Python legal variable name, not PIN
    """ Determine if accountnumber exist as an account and pin is its PIN """
    if accountnumber in DATA:
        return True
    return False


def get_name(accountnumber):
    """ The first and last name of an account, returned as a tuple

TODO: Add lastname
"""
    return DATA[accountnumber]["firstname"], None


def deposit(accountnumber, amount):
    """ Add amount to the account's balance return nothing

TODO: Implement this function.
"""
    pass
    # Recall that a function that updates an external value or produces
    # output as a 'side effect' (such as a print statement) will generally
    # not return a value. Some operations, such as the list's 'pop' method
    # will not follow this principle.
    #
    # The term 'method' is somewhat 'interchangeable with 'function'


def withdraw(accountnumber, amount):
    """ Subtract the amount from accountnumber

return nothing, raise ValueError if there are insufficient funds.
TODO: Implement this function
"""
    pass
