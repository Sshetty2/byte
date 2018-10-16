""" Data model for the TerminalTeller application """
import random 
import json
import os
from random import randint
from card_validation import cardValidation
from randomCC import completed_number 


# Locate the json file in the ttrader directory wherever the python
# executable is run. os.path is preferred to literal paths in strings
# because it can run on Linux, Mac, or Windows without changing
# code.
thisdir = os.path.dirname(os.path.realpath(__file__))
jsonfilename = "Account_Info_JSON.json"
JSONFILE = os.path.join(thisdir, jsonfilename)



# Note: keeping the data context of a module in a global variable will only
# work with very simple application:

# Global data store:



def initialize():
    global masterUserAccts
    """ Koad DATA from permanent jsonfile or initialize empty DATA dict """
    # the global keyword allows a function to alter a global variabl
    if os.stat("Account_Info_JSON.json").st_size == 0:
            masterUserAccts = {}
            with open("Account_Info_JSON.json", "w") as file_object:
                json.dump(masterUserAccts, file_object, indent=2)

    with open("Account_Info_JSON.json", "r") as file_object:
        masterUserAccts = json.load(file_object)
         


def save():
    """ Write the updated DATA to the permanent json store """

    with open(JSONFILE, "w") as file_object:
        json.dump(masterUserAccts, file_object)


def add_account(userID, firstname, lastname, pin):
    """ add a new account to the DATA store """
    # q: Why is 'global' not needed here?

    masterUserAccts[accountnumber] = {
        "firstname": firstname,
        "lastname": lastname,
        "PIN": pin,
        "balance": 0.00
    }


def generate_account_number():
    """ Generates a new account number. Number is a Luhn-legal credit card #.

Stub method. Import your Luhn algorithm module from problem #1 and use
your generator method.
"""
    newnumber = completed_number(['3', '3'], 16)

    while newnumber in masterUserAccts or newnumber is None:  # use 'is None & not == None
        newnumber = completed_number(['3', '3'], 16)
    return newnumber


def validate(userID, pin):  # use Python legal variable name, not PIN
    """ Determine if accountnumber exist as an account and pin is its PIN """
    if userID in masterUserAccts:
        return True
    return False



def checkBalance(logIn_userID):
    print(f"\n---------------------\nyour account balance is currently: {masterUserAccts[logIn_userID]['Balance']}\n---------------------\n")
    return logIn(logIn_userID)

def makeDeposit(logIn_userID, depositAmount):
    masterUserAccts[logIn_userID]['Balance']= depositAmount
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"\n---------------------\nNew Balance: {masterUserAccts[logIn_userID]['Balance']}\n---------------------\n")
    return logIn(logIn_userID)

def makeWithdrawal(logIn_userID, withdrawalAmount): 
    masterUserAccts[logIn_userID]['Balance']= str(int(masterUserAccts[logIn_userID]['Balance']) - int(withdrawalAmount))
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"\n---------------------\nNew Balance: {masterUserAccts[logIn_userID]['Balance']}\n---------------------\n")
    return logIn(logIn_userID)

def transfer(logIn_userID, target_userID, transferAmt):
    masterUserAccts[logIn_userID]['Balance']= str(int(masterUserAccts[logIn_userID]['Balance']) - int(transferAmt))
    masterUserAccts[target_userID]['Balance']= str(int(masterUserAccts[target_userID]['Balance']) + int(transferAmt))
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"\n---------------------\nSuccessful transaction!! \n\nNew Balance: {masterUserAccts[logIn_userID]['Balance']}\n\n Porting Back to main menu ...\n---------------------\n")
    return logIn(logIn_userID)    





"""
    pass
    # Recall that a function that updates an external value or produces
    # output as a 'side effect' (such as a print statement) will generally
    # not return a value. Some operations, such as the list's 'pop' method
    # will not follow this principle.
    #
    # The term 'method' is somewhat 'interchangeable with 'function'

"""