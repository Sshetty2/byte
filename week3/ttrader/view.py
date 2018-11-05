def welcome_message():
    print("Hey there! Welcome to terminal trader! Can't wait to help you get rich!...\n\n", end = " ")

def input_terminal():
    print("Please select from the following options.. \n\n 1. Create Account \n 2. Log In \n 3. Quit \n\n Selection:", end = " ")

def invalid_input():
    print("\n------------------------------------------------\nERROR: Invalid input.\n")

def already_exists():
    print("\n------------------------------------------------\nLooks like that user already exists.. ??\n ------------------------------------------------\n")

def create_account_username():
    print("------------------------------------------------\nOk, lets get started!\n\nEnter User ID:", end = " " )

def create_confirm():
    print("\n------------------------------------------------\nUser Account successfully created!\n ------------------------------------------------\n")

def enter_password():
    print("Enter Password:", end = " ")

def pass_length():
    print("\nMake sure your password is at least 8 letters\n------------------------------------------------\n")

def number_req():
    print("\nMake sure your password has a number in it\n------------------------------------------------\n")

def upper_req():
    print("\nMake sure your password has a capital letter in it\n------------------------------------------------\n")

def reenter_pass():
    print("Please re-type your password for verification")

def pass_error():
    print("Passwords do not match. Please try again")

def login():
    print("\nOk! please enter your username\nUser ID:", end = " ")

def does_not_exist():
    print("\n------------------------------------------------\nErr.. I don't see that user id in the system.. ?? Please try again\n ------------------------------------------------\n")

def invalid_password():
    print("\n------------------------------------------------\nERROR: Invalid Password.\n")

def login_menu_user(user_login):
    print(f"\n\nWelcome User {user_login.username}, \n\nLogin Menu:\n\n1. Check Balance\n2. See all positions\n3. Check Stock Price\n4. Buy Shares\n5. Sell Shares\n6. See All Trades\n7. Log out\n8. Quit\n9. Deposit Funds\n\nInput:", end = " ")

def check_balance(user_login):
    print(f"\n------------------------------------------------\nUser {user_login.username} Account Balance : {user_login.balance}\n -----------------------------------------------\n")

def check_all_positions(user_login):
    print(f"\n------------------------------------------------\nHello User {user_login.username}, here is a current snapshot of all of your current positions\n")

def ticker_selection_buy():
    print("\n------------------------------------------------\nOk, please enter the ticker symbol of the stock that you'd like to purchase!\n\nTicker Symbol:", end = " ")

def volume_amount_buy():
    print("\n------------------------------------------------\nOk, how much would you like to buy?\n\nVolume Amt:", end = " ")

def transaction_failed():
    print("\n------------------------------------------------\nERROR: Transaction Failed. ", end = " ")

def not_enough_funds():
    print("You do not have enough funds! \n------------------------------------------------\n")

def updated_position_value(updated_position_value):
    print(f"\n------------------------------------------------\nYour new position amount is {updated_position_value}\n------------------------------------------------\n")

def ticker_selection_sell():
    print("\n------------------------------------------------\nOk, please enter the ticker symbol of the stock that you'd like to sell!\n\nTicker Symbol:", end = " ")

def volume_amount_sell():
    print("\n------------------------------------------------\nOk, how much would you like to sell?\n\nVolume Amt:", end = " ")

def not_enough_shares():
    print("You do not own enough shares! \n------------------------------------------------\n")

def see_all_trades(user_login):
    print(f"\n------------------------------------------------\nHello User {user_login.username}, here is a current snapshot of all of your trades: \n")

def set_funds_amount():
    print("\n------------------------------------------------\nAccount Balance you'd like to set?\n\nAccount Balance:", end = " ")

def goodbye():
    print("\n\n------------------------------------------------\nThanks for using Terminal Trader!! \n\n Goodbye!!\n------------------------------------------------\n\n\n")

def ticker_query():
    print("\n------------------------------------------------\nOk, Enter the ticker symbol of the stock you'd like to get the price of\n\nTicker Symbol:", end = " ")

def ticker_check_price(ticker,ticker_price):
    print(f"\n------------------------------------------------\nThe price of ticker symbol {ticker} is {ticker_price}\n------------------------------------------------\n")

def login_menu_admin(user_login):
    print(f"\n------------------------------------------------\n\nWelcome User {user_login.username}, \n\nLogin Menu:\n\n1. Check Balance\n2. See all positions\n3. Check Stock Price\n4. Buy Shares\n5. Sell Shares\n6. See All Trades\n7. Log out\n8. Quit\n9. Set account balance (Admin)\n10. View All User Accounts\n\nInput:", end = " ")

def deposit_amount():
    print("\n------------------------------------------------\nOk, how much would you like to deposit?\n\nDeposit Amount:", end = " ")

def depsosit_successful():
    print("\n------------------------------------------------\nDeposit Successful\n ------------------------------------------------\n")

def see_all_accounts_one():
    print(f"\n------------------------------------------------\nHere is a list of all of the User Accounts:\n")