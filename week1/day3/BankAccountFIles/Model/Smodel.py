""" Data model for the TerminalTeller application """
import random 
import json
import os
from random import randint
from random import Random

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



def initialize():
    global masterUserAccts
    """ Koad DATA from permanent jsonfile or initialize empty DATA dict """
    # the global keyword allows a function to alter a global variabl
    if not os.path.isfile(JSONFILE):
            masterUserAccts = {}
            with open(JSONFILE, "w") as file_object:
                json.dump(masterUserAccts, file_object, indent=2)

    with open(JSONFILE, "r") as file_object:
        masterUserAccts = json.load(file_object)
         


def save():
    """ Write the updated DATA to the permanent json store """

    with open(JSONFILE, "w") as file_object:
        json.dump(masterUserAccts, file_object)


def add_account(userID, firstname, lastname, pin):
    """ add a new account to the DATA store """
    # q: Why is 'global' not needed here?

    masterUserAccts[userID] = {
        "firstname": firstname,
        "lastname": lastname,
        "PIN": pin,
        "balance": 0.00,
        "Credit Card": str(generate_credit_card())
    }

def generate_credit_card():
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
         if pin == masterUserAccts[userID]['PIN']:
            return True
    return False

def check_balance(logIn_userID):
    return masterUserAccts[logIn_userID]['balance']

def makeDeposit(logIn_userID, depositAmount):
    masterUserAccts[logIn_userID]['balance'] = str(int(masterUserAccts[logIn_userID]['balance']) + int(depositAmount))
    save()
    return masterUserAccts[logIn_userID]['balance']
    

def makeWithdrawal(logIn_userID, withdrawalAmount): 
    while int(withdrawalAmount) > int(masterUserAccts[logIn_userID]['balance']):
        withdrawalAmount = input("Insufficient Funds -- Please enter valid amount: ")       
    masterUserAccts[logIn_userID]['balance']= str(int(masterUserAccts[logIn_userID]['balance']) - int(withdrawalAmount))
    save()
    return masterUserAccts[logIn_userID]['balance']

def transfer(logIn_userID, target_userID, transferAmt):
    masterUserAccts[logIn_userID]['balance']= str(int(masterUserAccts[logIn_userID]['balance']) - int(transferAmt))
    print(logIn_userID, target_userID, transferAmt)
    masterUserAccts[target_userID]['balance']= str(int(masterUserAccts[target_userID]['balance']) + int(transferAmt))
    save()





"""
    pass
    # Recall that a function that updates an external value or produces
    # output as a 'side effect' (such as a print statement) will generally
    # not return a value. Some operations, such as the list's 'pop' method
    # will not follow this principle.
    #
    # The term 'method' is somewhat 'interchangeable with 'function'

"""
generator = Random()

def completed_number(prefix, length):
    
    ccnumber = prefix

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9
        sum += odd
        if pos != (length - 2):
            sum += int(reversedCCnumber[pos + 1])
        pos += 2

    # Calculate check digit
    print(ccnumber)
    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
    ccnumber.append(str(checkdigit))
    return int(float(''.join((ccnumber))))


