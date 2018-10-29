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
    print(f"\nWelcome User {user_login.username}, \n\nLogin Menu:\n\n1. Check Balance\n2. See all positions\n3. Buy Shares\n4. Sell Shares\n5. See All Trades\n6. Log out\n7. Quit\n8. Set account balance (Admin)\n\nInput:", end = " ")

def check_balance(user_login):
    print(f"\n------------------------------------------------\nUser {user_login.username} Account Balance : {user_login.balance}\n ------------------------------------------------\n")

def check_all_positions(user_login, all_positions):
    print(f"\n------------------------------------------------\nHello User {user_login.username}, here is a current snapshot of all of your current positions\n{all_positions}")

def ticker_selection_buy():
    print("------------------------------------------------\nOk, please enter the ticker symbol of the stock that you'd like to purchase!\n\nTicker Symbol:", end = " ")

def volume_amount_buy():
    print("------------------------------------------------\nOk, how much would you like to buy?\n\nVolume Amt:", end = " ")

def updated_position_value(updated_position_value):
    print(f"\n------------------------------------------------\nYour new position amount is {updated_position_value}\n------------------------------------------------\n")

def ticker_selection_sell():
    print("------------------------------------------------\nOk, please enter the ticker symbol of the stock that you'd like to sell!\n\nTicker Symbol:", end = " ")

def volume_amount_sell():
    print("------------------------------------------------\nOk, how much would you like to sell?\n\nVolume Amt:", end = " ")

def see_all_trades(user_login, all_positions):
    print(f"\n------------------------------------------------\nHello User {user_login.username}, here is a current snapshot of all of your trades\n{all_positions}")

def set_funds_amount():
    print("------------------------------------------------\nAccount Balance you'd like to set?\n\nAccount Balance:", end = " ")

def goodbye():
    print("\n------------------------------------------------\nThanks for using Terminal Trader!! \n\n Goodbye!!\n------------------------------------------------\n")