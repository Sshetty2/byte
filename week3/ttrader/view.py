def welcome_message():
    print("Hey there! Welcome to terminal trader! Can't wait to help you get rich!...\n\n", end = " ")

def input_terminal():
    print("Please select from the following options.. \n\n 1. Create Account \n 2. Log In \n 3. Quit \n\n Input:", end = " ")

def invalid_input():
    print("\n------------------------------------------------\nERROR: Invalid input.\n")

def already_exists():
    print("\n------------------------------------------------\nLooks like that user already exists.. ?? You're going to need to actually login\n ------------------------------------------------\n")

def create_account_username():
    print("------------------------------------------------\nOk, lets get started!\n\nEnter User ID:", end = " " )

def create_confirm():
    print("\n------------------------------------------------\nUser Account successfully created!\n ------------------------------------------------\n")

def enter_password():
    print("Enter Password:", end = " ")

def login():
    print("\nOk! please enter your username\nUser ID:", end = " ")

def does_not_exist():
    print("\n------------------------------------------------\nErr.. I don't see that user id in the system.. ?? Please try again\n ------------------------------------------------\n")

def invalid_password():
    print("\n------------------------------------------------\nERROR: Invalid Password.\n")

def login_menu(user_login):
    print(f"\n------------------------------------------------\n\nWelcome User {user_login.username}, \n\nLogin Menu:\n\n1. Check Balance\n2. Make Deposit\n3. Make Withdrawal\n4. Make a Transfer\n5. Log out\n6. Quit\n")