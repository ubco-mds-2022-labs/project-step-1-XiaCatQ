# Bank Account System

This is a simple bank account system that allows you to perform the essential functions of banking software.
It allows you to create a bank account, deposit money, withdraw money, and check your balance. It also allows you to 
withdraw money in different currency. The program is written in a way that allows for easy expansion and
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
genAccNum(): generate a random account number range from 10000 to 99999. Input: nothing, output: 5-digit integer.\
User(): initialize the user’s information. Input: name (str) and account number (int), output: nothing.\
newUser(): initialize the new user’s information. Input: name (str), output: nothing.\
eUser(): initialize the existing user’s information. Input: name (str) and account number (int), output: nothing.\
information(self, date): print the user’s information. Input: date (str), output: nothing.\
store(self): store the user’s information. Input: name (str) and account number (int), a, output: information (txt).\
deposit(self, amount, date): deposit money into the account, with a date. And print out the deposit amount and the new
balance. Input: amount (float) and date (str), output: balance (int).\
withdraw(self, amount, date): withdraw money from the account, with a date. And print out the withdraw amount and the
new balance. If the balance is not enough, print out the message that the balance is not enough. Input: amount (float) and
date (str), output: balance (int).\
information(self, date): print the user’s account information. Input: date (str), output: account information (str).\


### Module 2 Define Functions for Account Value Calculation:
Get interest rate and exchange rate online.
Create functions for calculating account balance.

#### Functions: calculation.py
getIntRates(): get interest rate from the website. Input: nothing, output: interest rate (float).\
getExRates(): get exchange rate from the website. Input: nothing, output: exchange rate (float).\
interest(balance): calculate the interest of the account. Input: balance (float), output: interest (float).\
service(x): calculate the service fee of the account. While withdraw money, deduct CAD $3 for service fee. Input: amount
(int), output: withdraw amount plus service fee (int).\


## Sub-Package 2: UI and Data Storage Design the interface for user and data storage for the bank.

### Module 1 Design user interface:
Create a friendly interface for user.

#### Functions: bankingUI.py
main(): create the main interface for user. Input: nothing, output: screen with two options.\
signup(): create the interface for user to sign up. Input: temp_name (str), temp_initialAmount (str), output: name (str), initial deposit (str), temp_accountNum (str),.\
finish_signup(): create the interface for user to finish sign up. Input: temp_name (str), temp_accountNum (str), temp_initialAmount (str), output: account information (text).\
signin(): create the interface for user to sign in. Input: temp_signin_name (str), temp_signin_accountNum (str), output: temp_signin_name (str), temp_signin_accountNum (str).\
signin_session(): create the interface for user who successfully sign in. Input: temp_signin_name (str), temp_signin_accountNum (str), output: new screen with options.\
personal_details(): create the interface for user to view personal details. Input: object from eUser and use information function, output: texts on screen.\
deposit(): create the interface for user to deposit money. Input: temp_dep_amount (str), temp_dep_date (str), output: temp_dep_amount (str), temp_dep_date (str).\
finish_deposit(): create the interface for user to finish deposit (renew balance and record transaction). Input: temp_dep_amount (str), temp_dep_date (str), output: account information(text).\
withdraw(): create the interface for user to withdraw money. Input: temp_w_amount (str), temp_w_date (str), temp_w_currency (str), output: temp_w_amount (str), temp_w_date (str), temp_w_currency (str).\
finish_withdraw(): create the interface for user to finish withdraw (renew balance and record transaction). Input: temp_w_amount (str), temp_w_date (str), temp_w_currency (str), output: account information(text).\


### Module 2 Data Storage:
Record Account Information (e.g. name, account number) 
Record Transactions (e.g. date, amount, action,..)

#### Functions: bankingDS.py
addAccount(n, aN, iA, B): add a new account to the database. Input: name (str), account number (int), initial amount
(float), balance (float), output: text file.\
validate(n, aN): validate the account number and name. Input: name (str) and account number (int), output: True or False.\
delAccount(n, aN): delete the account from the database. Input: name (str) and account number (int), output: nothing.\


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

