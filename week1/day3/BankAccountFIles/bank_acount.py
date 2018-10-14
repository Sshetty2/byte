import random 
import json
from randomCC import completed_number 
from card_validation import cardValidation
from pprint import pprint
import os
 
if os.stat("Account_Info_JSON.json").st_size == 0:
        masterUserAccts = {}
        with open("Account_Info_JSON.json", "w") as file_object:
            json.dump(masterUserAccts, file_object, indent=2)

with open("Account_Info_JSON.json", "r") as file_object:
    masterUserAccts = json.load(file_object)


def inputTerminal():
    optionsMenu = input("Please select from the following options.. \n\n 1. Create Account \n 2. Log In \n 3. Quit \n\n input:")
    while optionsMenu not in ["1","2","3", 1, 2, 3]:
        optionsMenu = input("Please input correct value \n input: ")
        return inputTerminal()
    if optionsMenu == "1" or optionsMenu == 1:
        createAccount()
    if optionsMenu == "2" or optionsMenu == 2:
        logIn_userID = input("Please input user id: ")
        while logIn_userID not in masterUserAccts:
           logIn_userID = input("Please input valid user id: ")
        logIn_PIN = input("Please input PIN: ")
        while logIn_PIN != masterUserAccts[logIn_userID]['PIN']:
            logIn_PIN = input("Please input valid pin: ")
        print(f"Hello, {masterUserAccts[logIn_userID]['User First Name']} {masterUserAccts[logIn_userID]['User Last Name']} \n\nLogin Menu:\n\n1. Check Balance\n2. Make Deposit\n3. Make Withdrawal\n4. Log out\n5. Make a Transfer\n6. Return to Main Menu\n")
        logIn(logIn_userID)
    if optionsMenu == "3" or optionsMenu == 3:
        print("goodbye")
        quit()


def logIn(logIn_userID):
        logIninput = input("What would you like to do? ")
        while logIninput not in ["1","2","3","4","5"]:
            logIninput = input("Please enter valid input")
        if logIninput == "1":
            checkBalance(logIn_userID)
        if logIninput == "2":
            depositAmount = input("How much would you like to deposit?: ")
            makeDeposit(logIn_userID, depositAmount)
        if logIninput == "3":
            withdrawalAmount = input("How much would you like to withdraw?: ")
            makeWithdrawal(logIn_userID, withdrawalAmount)
        if logIninput == "4":
            print("Logging out .. \n\n\n Goodbye!! \n\n\n")
            quit()
        if logIninput == "5":
            target_userName = input("who would you like to transfer to? (Full names only) ")
            while len(target_userName.split()) != 2:
                target_userName = input("please input only first and last name \n try again: ")
            target_userID_firstName = target_userName.split()[0]
            target_userID_lastName = target_userName.split()[1]
            target_userID = target_userID_firstName[0] + target_userID_lastName
            while target_userID not in masterUserAccts:
               target_userID = input("Please input valid user id: ") 
            transferAmt = input("How much would you like to transfer?: ")
            while int(transferAmt) < 0:
                transferAmt = input("Please enter an amount greater than zero: ")
            while int(transferAmt) > int(masterUserAccts[logIn_userID]['Balance']):
                transferAmt = input("Insufficient Funds -- Please enter valid amount: ")
            transfer(logIn_userID, target_userID, transferAmt)
            return inputTerminal()
        if logIninput == "6":
            return inputTerminal()
        
           

def createAccount():
    userName = input("input user name: ")
    while len(userName.split()) != 2:
        userName = input("please input only first and last name \n try again: ")
    userFirstName = userName.split()[0]
    userLastName = userName.split()[1]
    userID = userFirstName[0] + userLastName
    PIN = input("please input new 4-digit pin number: ")
    while len(PIN) != 4:
        PIN = input("please input 4-digit pin: ")
    masterUserAccts[userID] = {}
    masterUserAccts[userID]["User First Name"] = userFirstName.capitalize()
    masterUserAccts[userID]["User Last Name"] = userLastName.capitalize()
    masterUserAccts[userID]["PIN"] = PIN
    masterUserAccts[userID]["Balance"] = "00"
    #  A new card number is added to the masterUserAccts object generated from randomCC
    # The new credit card number is first referenced with existing credit card numbers before being added
    masterUserAccts[userID]["Credit Card Number"] = completed_number(['3', '3'], 16)
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    pprint(masterUserAccts)
    print(f'\n\nNew account created! \n\n you\'re new user ID is {userID}\n\n... Porting back to main menu\n\n')
    return logIn(logIn_userID)

def checkBalance(logIn_userID):
    print(f"your account balance is currently: {masterUserAccts[logIn_userID]['Balance']}\n\n")
    command = input("Return to main menu(Y/N)?: \n\n")
    while command not in ["Y", "y"]:
        return checkBalance(logIn_userID)
    return logIn(logIn_userID)

def makeDeposit(logIn_userID, depositAmount):
    masterUserAccts[logIn_userID]['Balance']= depositAmount
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"New Balance: {masterUserAccts[logIn_userID]['Balance']}\n")
    command = input("Return to main menu(Y/N)?: \n\n")
    while command not in ["Y", "y"]:
        return checkBalance(logIn_userID)
    return logIn(logIn_userID)

def makeWithdrawal(logIn_userID, withdrawalAmount):
    masterUserAccts[logIn_userID]['Balance']= withdrawalAmount
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"New Balance: {masterUserAccts[logIn_userID]['Balance']}\n")
    command = input("Return to main menu(Y/N)?: \n\n")
    while command not in ["Y", "y", "n", "N"]:
        command = input("Return to main menu(Y/N)?: \n\n")
    if command in ["n", "N"]:
        return makeWithdrawal(logIn_userID, withdrawalAmount)
    return logIn(logIn_userID)

def transfer(logIn_userID, target_userID, transferAmt):
    masterUserAccts[logIn_userID]['Balance']= str(int(masterUserAccts[logIn_userID]['Balance']) - int(transferAmt))
    masterUserAccts[target_userID]['Balance']= str(int(masterUserAccts[target_userID]['Balance']) + int(transferAmt))
    with open("Account_Info_JSON.json", "w") as file_object:
        json.dump(masterUserAccts, file_object, indent=2)
    print(f"\nSuccessful transaction!! \n\nNew Balance: {masterUserAccts[logIn_userID]['Balance']}\n\n Porting Back to main menu ... \n")
    return inputTerminal()    



# Master run function 
def run():
    inputTerminal()



##################

run()

##################
