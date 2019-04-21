import random 
import json
from randomCC import completed_number 
from card_validation import cardValidation

def inputTerminal():
    optionsMenu = input("Please select from the following options.. \n 1. Create Account \n 2. Log In \n 3. Quit \n input: ")
    while optionsMenu not in ["1","2","3"]:
        optionsMenu = input("Please input correct value \n input: ")
    if optionsMenu == "1":
        createAccount()
    if optionsMenu == "2":
        logIn()
    if optionsMenu == "3":
        print("goodbye")
        quit()


#designate login procedures
def logIn():
    print('not created yet')
    quit()



def createAccount():
    masterUserAccts = {}
    userName = input("input user name: ")
    while len(userName.split()) != 2:
        userName = input("please input only first and last name \n try again: ")
    userFirstName = userName.split()[0]
    userLastName = userName.split()[1]
    userID = userFirstName[0] + userLastName
    PIN = input("please input new 4-digit pin number: ")
    while len(PIN) != 4:
        PIN = input("please input 4-digit pin: ")
    masterUserAccts["UserID"] = userID
    masterUserAccts[userID] = {}
    masterUserAccts[userID]["User First Name"] = userFirstName
    masterUserAccts[userID]["User Last Name"] = userLastName
    masterUserAccts[userID]["PIN"] = PIN
    masterUserAccts[userID]["Balance"] = 00
    #  A new card number is added to the masterUserAccts object generated from randomCC
    # The new credit card number is first referenced with existing credit card numbers before being
    masterUserAccts[userID]["Credit Card Number"] = completed_number(['3', '3'], 16)
    print(masterUserAccts)
    print("new account created! \n ... Porting back to main menu")
    return inputTerminal()

#queries server for balance information
# def checkBalance():


#retreives x dollars from bank account
# def makeWithdrawal():


# Master run function 
def run():
    inputTerminal()
##################

run()

##################
