""" Defines control flow of the TerminalTeller application

Homework reading: Read PEP 8 on code formatting and PEP 257 on docstrings.
"""

from BankAccountFiles import view
from BankAccountFiles import model


def logIn():
        logIn_userID = view.accountmenu()
        while logIninput not in ["1","2","3","4","5","6"]:
            logIninput = input("Please enter valid input")
        if logIninput == "1":
            checkBalance(logIn_userID)
        if logIninput == "2":
            depositAmount = input("How much would you like to deposit?: ")
            makeDeposit(logIn_userID, depositAmount)
        if logIninput == "3":
            withdrawalAmount = input("How much would you like to withdraw?: ")
            while int(withdrawalAmount) > int(masterUserAccts[logIn_userID]['Balance']):
                withdrawalAmount = input("Insufficient Funds -- Please enter valid amount: ")
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



"""
    answer = view.accountmenu()

    if answer not in ["1", "2", "3"]:
        view.invalidinput()
        return loginloop()  # Recursion to repeat the menu.

    if answer == "1":  # login
        userID, pin = view.loginprompt()
        if model.validate(userID, pin):
            return userID

        view.invalidaccount()
        return loginloop()

    if answer == "2":  # create account
        createaccount()
        return loginloop()

    if answer == "3":  # exit
        return None

"""

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
    userID = model.generate_account_number()
    model.add_account(str(userID), firstname, lastname, pin)
    view.creationconfirm(userID)


def mainloop(userID):
    """ Main menu loop. Check balance. Make deposit. Make withdrawal. Exit.

TODO: Stub Method: Create the full menu.
"""

    firstname, lastname = model.get_name(userID)
    view.mainmenu(firstname)
    exitprogram()


def run():
    """ Main flow of the program. """

    model.initialize()
    view.accountmenu()
    logIn() 
    userID = logIn()
    if not userID:
        exitprogram()

    mainloop(userID)
    exitprogram()


if __name__ == "__main__":
    run()
