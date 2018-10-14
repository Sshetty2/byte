## TerminalTeller

#### Your first application!

* Complete the stub code to have a working application

* You will need to add & import your Luhn algorithm code as a new module

#### The assignment

* You will create an interactive terminal environment simulating a customer interacting with their checking account at a bank teller.

* You will store the data from the program in a json file that is loaded, updated, and re-saved across multiple executions of the program.

* When you first execute the program, present the user with the following menu:

```
1. Create an account

2. Log in

3. Quit
```

* If they enter a valid input and select Log in, present a new view that asks them for a first name, last name, and PIN. This will initialize a new account with a balance of 00 and a new debit card number that is valid under the Luhn algorithm. You can generate this however you want, but they need to be unique no matter how many new users are created.

* This information is stored in the master list of accounts, which is saved in a json file.

* After this they return to the first menu.

* If they enter Log in they are prompted for their account number and PIN. If they enter valid credentials they proceed to the teller menu, otherwise they are told they have entered it incorrectly and are returned to the login menu.

* After logging in they see this menu:

```
Hello, <User Name> #<Account Number>

login menu.

* After logging in they see this menu:

```
Hello, <User Name> #<Account Number>

1. Check Balance

2. Make Deposit

3. Make Withdrawal

4. Log out
```

* Option 1 presents them with the value of their balance

* Option 2 asks them for a dollar amount and adds it to the deposit.

* Option 3 asks them for a dollar amount and deducts it from their balance if there is enough there.

* Option 4 logs out. Any changes to user data should be written to file.
