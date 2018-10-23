""" Defines control flow of the TerminalTeller application

Homework reading: Read PEP 8 on code formatting and PEP 257 on docstrings.
"""

from Model import Smodel
from View import Sview

def inputTerminal():
    optionsMenu = Sview.loginmenu()
    while optionsMenu not in ["1","2","3", 1, 2, 3]:
        Sview.invalidinput()
        return inputTerminal()
    if optionsMenu == "1" or optionsMenu == 1:
        createaccount()
    if optionsMenu == "2" or optionsMenu == 2:
        login()
        loginMenu = Sview.accountmenu()
    if optionsMenu == "3" or optionsMenu == 3:
        exitprogram()




def login(): 
    user_ID, PIN = Sview.loginprompt()
    if Smodel.validate(user_ID, PIN): 
        logIninput = Sview.accountmenu()
        while logIninput not in ["1","2","3","4","5","6"]:
            Sview.invalidinput()
            logIninput = input("input: ")
        if logIninput == "1":
            balance = Smodel.check_balance(user_ID)
            Sview.checkBalance(balance)
            return login()
        if logIninput == "2":
            depositAmount = Sview.deposit_amount()
            new_balance = Smodel.makeDeposit(user_ID, depositAmount)
            Sview.deposit_successful(new_balance)
            return login()
        if logIninput == "3":
            withdrawalAmount = Sview.withdrawal_amount()
            balance = Smodel.makeWithdrawal(user_ID, withdrawalAmount) 
            Sview.withdrawal_successful(balance)
            return login()
        if logIninput == "4":
            transfer, transferee = Sview.transfer_amount()
            Smodel.transfer(user_ID, transferee, transfer)
            Sview.transfer_successful()
            return login()
            
        if logIninput == "5":
            return inputTerminal()
        if logIninput == "6":
            exitprogram()
            
    else:         
        Sview.invalidinput()
        return login()
    
    


def exitprogram():
    """ save data and exit the program """

    Smodel.save()
    Sview.goodbye()
    quit()


def createaccount():
    firstname, lastname, pin = Sview.create_account()
    userID = firstname[0] + lastname
    Smodel.add_account(userID, firstname, lastname, pin)
    Sview.creationconfirm(userID)
    Smodel.save()
    return inputTerminal()


def mainloop(userID):
    """ Main menu loop. Check balance. Make deposit. Make withdrawal. Exit.

TODO: Stub Method: Create the full menu.
"""

    firstname, lastname = Smodel.get_name(userID)
    Sview.mainmenu(firstname)
    exitprogram()


def run():
    """ Main flow of the program. """

    Smodel.initialize()
    inputTerminal() 
#    if not userID:
 #       exitprogram()

#    mainloop(userID)
 #   exitprogram()


if __name__ == "__main__":
    run()

