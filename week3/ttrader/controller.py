import model
import view

import getpass
import re

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
    pass_prompt(new_user)

def pass_prompt(new_user):
    while True:
        view.enter_password()
        password = getpass.getpass()
        if len(password) < 8:
            view.pass_length()
        elif re.search('[0-9]',password) is None:
            view.number_req()
        elif re.search('[A-Z]',password) is None: 
            view.upper_req()
        else:
            break
    view.reenter_pass()
    password_check = getpass.getpass()
    if password_check != password:
        view.pass_error()
        password = None
        return pass_prompt(new_user)
    hashed_pw = new_user.calculatehash(password)
    new_user.pass_hash = hashed_pw
    new_user.balance = 0 
    new_user.type = "USER"
    new_user.save()
    


def login():
    view.login()
    login_id = input().lower()
    new_login = model.Account(login_id)
    while not new_login.check_set_username():
        view.does_not_exist()
        return login_terminal()
    new_login = new_login.set_from_username()
    view.enter_password()
    password = getpass.getpass()
    while not new_login.check_password((new_login.pass_hash), password):
        view.invalid_password()
        view.enter_password()
        password = getpass.getpass()
    login_menu(new_login)

def login_menu(user_login):
    if user_login.type == "ADMIN":
        view.login_menu_admin(user_login)
        login_input = input()
        while login_input not in ["1","2","3","4","5","6","7","8","9","10","11"]:
            view.invalid_input()
            login_input = input()
        if login_input == "1":
            view.check_balance(user_login)
            return login_menu(user_login)
        if login_input == "2":
            all_positions = user_login.getpositions()
            view.check_all_positions(user_login)
            model.print_gettrades(all_positions)
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
            buy(user_login)
        if login_input == "5":
            sell(user_login)
        if login_input == "6":
            all_trades = user_login.gettrades()
            view.see_all_trades(user_login)
            model.print_gettrades(all_trades)
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
        if login_input == "10":
            view.see_all_accounts_one()
            all_accounts = user_login.get_all_accounts()
            model.print_all_accounts(all_accounts)
            return login_menu(user_login)
        if login_input == "11":
            print(model.return_top_headlines_content("author"))
            return login_menu(user_login)


    else:
        view.login_menu_user(user_login)
        login_input = input()
        while login_input not in ["1","2","3","4","5","6","7","8","9"]:
            view.invalid_input()
            login_input = input()
        if login_input == "1":
            view.check_balance(user_login)
            return login_menu(user_login)
        if login_input == "2":
            all_positions = user_login.getpositions()
            print(all_positions)
            view.check_all_positions(user_login)
            model.print_gettrades(all_positions)
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
            buy(user_login)
        if login_input == "5":
            sell(user_login)
        if login_input == "6":
            all_trades = user_login.gettrades()
            view.see_all_trades(user_login)
            model.print_gettrades(all_trades)
            return login_menu(user_login)
        if login_input == "7":
            view.goodbye()
            return login_terminal()
        if login_input == "8":
            view.goodbye()
            quit()
        if login_input == "9":
            view.deposit_amount()
        try:
            deposit_amount = int(input())
        except ValueError:
            view.invalid_input()
            return login_menu(user_login)
        while deposit_amount < 0:
            view.invalid_input
            deposit_amount= input()
        user_login.deposit_funds(deposit_amount)
        view.depsosit_successful()
        return login_menu(user_login)


def buy(user_login):
    view.ticker_selection_buy()
    ticker_buy = input().upper()
    ticker_check = model.apiget(ticker_buy)
    while ticker_check == None:
        print("Not a valid ticker!")
        view.ticker_selection_buy()
        ticker_buy = input().upper()
        ticker_check = model.apiget(ticker_buy)   
    view.volume_amount_buy(ticker_buy, ticker_check)
    try:
        volume_amount_buy = int(input())
    except ValueError:
        view.invalid_input()
        return buy(user_login)
    view.buy_confirm(ticker_buy, ticker_check, volume_amount_buy)
    buy_confirmation = input()
    while buy_confirmation not in ["Y","y","N","n"]:
        view.invalid_input()
        buy_confirmation = input()
    if buy_confirmation in ["N", "n"]:
        return login_menu(user_login)
    try:
        user_login.buy(ticker_buy, volume_amount_buy)
        updated_position_value = user_login.getposition(ticker_buy)
        view.updated_position_value(updated_position_value)
    except:   
        view.transaction_failed() 
        view.not_enough_funds()
    return login_menu(user_login)


def sell(user_login):
        view.ticker_selection_sell()
        ticker_sell = input().upper()
        ticker_sell_price = model.apiget(ticker_sell)
        while ticker_sell_price == None:
            print("Not a valid ticker!")
            view.ticker_selection_sell()
            ticker_sell = input().upper()
            ticker_sell_price = model.apiget(ticker_sell) 
        view.volume_amount_sell(ticker_sell, ticker_sell_price)
        try:
            volume_amount_sell = int(input())
        except ValueError:
            view.invalid_input()
            return sell(user_login)
        view.sell_confirm(ticker_sell, ticker_sell_price, volume_amount_sell)
        sell_confirmation = input()
        while sell_confirmation not in ["Y","y","N","n"]:
            view.invalid_input()
            sell_confirmation = input()
        if sell_confirmation in ["N", "n"]:
            return login_menu(user_login)        
        try:
            user_login.sell(ticker_sell, volume_amount_sell)
            updated_position_value = user_login.getposition(ticker_sell)
            view.updated_position_value(updated_position_value)
        except:
            view.transaction_failed()
            view.not_enough_shares()
        return login_menu(user_login)





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
