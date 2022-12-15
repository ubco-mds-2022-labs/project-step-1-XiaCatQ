# Bank Account System

This is a simple bank account system that allows you to perform the essential functions of banking software.
It allows you to create a bank account, deposit money, withdraw money, and check your balance. It also allows you to 
create multiple accounts and switch between them. The program is written in a way that allows for easy expansion and
modification. 

The 4 main purposes of this program are:
1. Create a new account 
2. Make deposits and withdrawals 
3. Exchange money 
4. View the account’s records 


## Sub-Package 1: Structure is mainly for establishing account objects and define functions for account value.

### Module 1 Establishing Objects:
Define class User for bank account user. 
Define subclass newUser inherits User. 
Define subclass eUser inherits User.

#### Functions: User.py
genAccNum(): generate a random account number range from 10000 to 99999.
User(): initialize the user’s information.
newUser(): initialize the new user’s information.
eUser(): initialize the existing user’s information.
information(self, date): print the user’s information.
store(self): store the user’s information.
deposit(self, amount, date): deposit money into the account, with a date. And print out the deposit amount and the new
balance.
withdraw(self, amount, date): withdraw money from the account, with a date. And print out the withdraw amount and the
new balance. If the balance is not enough, print out the message that the balance is not enough.
information(self, date): print the user’s account information.

### Module 2 Define Functions for Account Value Calculation:
Get interest rate and exchange rate online.
Create functions for calculating account balance.

#### Functions: calculation.py
getIntRates(): get interest rate from the website.
getExRates(): get exchange rate from the website.
interest(balance): calculate the interest of the account.
service(x): calculate the service fee of the account. While withdraw money, deduct CAD $3 for service fee.


## Sub-Package 2: UI and Data Storage Design the interface for user and data storage for the bank.

### Module 1 Design user interface:
Create a friendly interface for user.

#### Functions: bankingUI.py
main(): create the main interface for user.
signup(): create the interface for user to sign up.
finish_signup(): create the interface for user to finish sign up.
signin_session(): create the interface for user to sign in.
personal_details(): create the interface for user to view personal details.
deposit(): create the interface for user to deposit money.
finish_deposit(): create the interface for user to finish deposit.
withdraw(): create the interface for user to withdraw money.
finish_withdraw(): create the interface for user to finish withdraw.
signin(): create the interface for user to sign in.

### Module 2 Data Storage:
Record Account Information (e.g. name, account number) 
Record Transactions (e.g. date, amount, action,..)

#### Functions: bankingDS.py
addAccount(n, aN, iA, B): add a new account to the database.
validate(n, aN): validate the account number and name.
delAccount(n, aN): delete the account from the database.


## How to use
1. Download the project
2. Open the project in your IDE
3. Run the project
4. Follow the instructions on the screen
5. Enjoy!
6. If you have any questions, please contact us at: [email protected]
7. Thank you for using our product!
8. Have a nice day!

## Contributors
Chen, Ziying\
Ju, Zhijia

