import model
import view

import getpass


def login_terminal():
    view.input_terminal()
    options_menu = input()
    while options_menu not in ["1","2","3", 1, 2, 3]:
        view.invalid_input()
        return login_terminal()
    if options_menu == "1" or options_menu == 1:
        create_account()
        view.create_confirm()
        return login_terminal()
    if options_menu == "2" or options_menu == 2:
        login()
    if options_menu == "3" or options_menu == 3:
        view.goodbye()
        quit()

def create_account():
    view.create_account_username()
    username = input()
    new_user = model.Account(username)
    while new_user.check_set_username():
        view.already_exists()
        return login_terminal()
    view.enter_password()
    password = getpass.getpass()
    hashed_pw = new_user.calculatehash(password)
    new_user.pass_hash = hashed_pw
    new_user.balance = 0 
    new_user.type = "USER"
    new_user.save()
    
def login():
    view.login()
    login_id = input()
    new_login = model.Account(login_id)
    while not new_login.check_set_username():
        view.does_not_exist()
        return login_terminal()
    new_login = new_login.set_from_username(login_id)
    view.enter_password()
    password = getpass.getpass()
    while not new_login.check_password((new_login.pass_hash), password):
        view.invalid_password()
        view.enter_password()
        password = input()
    login_menu(new_login)

def login_menu(user_login):
    view.login_menu(user_login)
    login_input = input()
    while login_input not in ["1","2","3","4","5","6","7","8","9"]:
        view.invalidinput()
        login_input = input()
    if login_input == "1":
        view.check_balance(user_login)
        return login_menu(user_login)
    if login_input == "2":
        all_positions = user_login.getpositions()
        view.check_all_positions(user_login, all_positions)
        return login_menu(user_login)
    if login_input == "3":
        view.ticker_query()
        ticker = input().upper()
        price = model.apiget(ticker)
        while price == None:
            print("Not a valid ticker!")
            view.ticker_query()
            ticker = input().upper()
            price = model.apiget(ticker)
        view.ticker_check_price(ticker, price)
        return login_menu(user_login)
    if login_input == "4":
        view.ticker_selection_buy()
        ticker_buy = input().upper()
        view.volume_amount_buy()
        volume_amount_buy = int(input())
        try:
            user_login.buy(ticker_buy, volume_amount_buy)
            updated_position_value = user_login.getposition(ticker_buy)
            view.updated_position_value(updated_position_value)
        except:   
            view.transaction_failed() 
            view.not_enough_funds()
        return login_menu(user_login)
    if login_input == "5":
        view.ticker_selection_sell()
        ticker_sell = input().upper()
        view.volume_amount_sell()
        volume_amount_sell = int(input())
        try:
            user_login.sell(ticker_sell, volume_amount_sell)
            updated_position_value = user_login.getposition(ticker_sell)
            view.updated_position_value(updated_position_value)
        except:
            view.transaction_failed()
            view.not_enough_shares()
        return login_menu(user_login)
    if login_input == "6":
        all_trades = user_login.gettrades()
        view.see_all_trades(user_login, all_trades)
        return login_menu(user_login)
    if login_input == "7":
        view.goodbye()
        return login_terminal()
    if login_input == "8":
        view.goodbye()
        quit()
    if login_input == "9":
        view.set_funds_amount()
        amt_of_funds = input()
        user_login.set_balance(amt_of_funds)
        return login_menu(user_login)
        quit()


def run():
    """ Main flow of the program. """
    view.welcome_message()
    login_terminal() 
    view.goodbye()
    quit()
#    if not userID:
 #       exitprogram()

#    mainloop(userID)
 #   exitprogram()

if __name__ == "__main__":
    run()