""" TerminalTeller views """


# from getpass import getpass





def loginmenu():
    """ Display login / account creation options """
    print("Please select from the following options.. \n\n 1. Create Account \n 2. Log In \n 3. Quit \n")
    optionsMenu = input("input selection:")
    return optionsMenu

def accountmenu():
    """ Display login / account creation options """
    print(f"\n Hello, \n\nLogin Menu:\n\n1. Check Balance\n2. Make Deposit\n3. Make Withdrawal\n4. Make a Transfer\n5. Log out\n6. Quit\n")
    loginmenuoptions = input("input:")
    return loginmenuoptions

def invalidinput():
    """ Display invalid input error. """

    print("\n\tERROR: Invalid input.\n")



def create_account():
    """ Prompt returning firstname, lastname, and PIN

TODO: Stub method, finish this.
Look at the getpass method of the getpass module for private input.
"""

    print("Input first name for new account: ", end="")
    firstname = input().capitalize()
    while len((firstname).split()) != 1:
        firstname = input("please input only first name \n try again: ").capitalize()
    print("Input last name for new account: ", end="")
    lastname = input().capitalize()
    while len((lastname).split()) != 1:
        lastname = input("please input only last name \n try again: ").capitalize()
    print("Input PIN for new account: ", end="")
    PIN = input()
    while len(PIN) != 4:
        PIN = input("please input 4-digit pin: ")


    return firstname, lastname, PIN


def creationconfirm(userID):
    """ Display account number after successful creation """

    print("\t\tAccount created, your user ID is {}.".format(
        userID))


def loginprompt():
    """ Login prompt, return accountnumber, pin

TODO: Stub method, finish this
"""
    global user_ID
    print("Input your user ID: ")
    user_ID = input()
    user_ID_first = ''.join(list(user_ID)[0]).capitalize()
    user_ID_second = ''.join(list(user_ID)[1]).capitalize()
    user_ID_rest = ''.join(list(user_ID)[2:])
    user_ID = user_ID_first + user_ID_second + user_ID_rest
    print("Input your PIN: ")
    PIN = input()
    return user_ID, PIN

def deposit_amount():
    print("How much would you like to deposit?: ")
    deposit = input()
    return deposit

def withdrawal_amount():
    print("How much would you like to withdraw?: ")
    withdraw = input()
    return withdraw

def transfer_amount():
    print("Who would you like to transfer to (User names only)? ") 
    transferee = input()
    transferee_first = ''.join(list(transferee)[0]).capitalize()
    transferee_second = ''.join(list(transferee)[1]).capitalize()
    transferee_rest = ''.join(list(transferee)[2:])
    transferee = transferee_first + transferee_second + transferee_rest
    while transferee not in masterUserAccts:
        transferee = input("Please input valid user id: ")
    print("How much would you like to transfer?: ")
    transfer = input()
    while int(transfer) < 0:
        transfer = input("Please enter an amount greater than zero: ")
    while int(transfer) > int(Smodel.masterUserAccts[user_ID]['balance']):
            transfer = input("Insufficient Funds -- Please enter valid amount: ")
    return transfer, transferee



def checkBalance(balance):
    print(f"\n---------------------\nyour account balance is currently: {balance}\n---------------------\n")

def deposit_successful(new_balance):
    print(f"\n---------------------\nSuccessful deposit! \n\nNew Balance: {new_balance}\n---------------------\n")

def withdrawal_successful(remaining_balance):
    print(f"\n---------------------\nWithdrawal successful! \n\nNew Balance: {remaining_balance}\n---------------------\n")

def transfer_successful():
    print(masterUserAccts)
    print(f"\n---------------------\nSuccessful transaction!! \n\nNew Balance: {masterUserAccts[user_ID]['balance']}\n---------------------\n")

def goodbye():
    """ Message displayed on exit. """

    print("\t\tThank you for using the Teller Service!")


def mainmenu(name):
    """ Main menu, display all options and prompt for a selection

TODO: Stub method, finish this
"""
    print("Hello, {}".format(name))

# TODO: Add additional views as needed.
