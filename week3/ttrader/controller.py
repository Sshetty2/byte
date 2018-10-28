import model
import view

def login_terminal():
    view.input_terminal()
    options_menu = input()
    while options_menu not in ["1","2","3", 1, 2, 3]:
        view.invalid_input()
        return input_terminal()
    if options_menu == "1" or options_menu == 1:
        create_account()
        view.create_confirm()
        return login_terminal()
    if options_menu == "2" or options_menu == 2:
        login()
    if options_menu == "3" or options_menu == 3:
        exitprogram()

def create_account():
    view.create_account_username()
    username = input()
    new_user = model.Account(username)
    while new_user.check_username():
        view.already_exists()
        return login_terminal()
    view.enter_password()
    password = input()
    hashed_pw = new_user.calculatehash(password)
    new_user.pass_hash = hashed_pw
    new_user.balance = 0 
    new_user.type = "USER"
    print(new_user)
    new_user.save()
    
def login():
    view.login()
    login_id = input()
    new_login = model.Account(login_id)
    while not new_login.check_username():
        view.does_not_exist()
        return login_terminal()
    new_login = new_login.set_from_username(login_id)
    view.enter_password()
    password = input()
    while not new_login.check_password((new_login.pass_hash), password):
        view.invalid_password()
        view.enter_password()
        password = input()
    login_menu(new_login)

def login_menu(user_login):
    view.login_menu(user_login)






def run():
    """ Main flow of the program. """
    view.welcome_message()
    login_terminal() 
#    if not userID:
 #       exitprogram()

#    mainloop(userID)
 #   exitprogram()


if __name__ == "__main__":
    run()
