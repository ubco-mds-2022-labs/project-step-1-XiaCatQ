import random

# generate account number
available_acc_num = [i for i in range(10000,99999)]
def genAccNum():
    acc_num = random.choice(available_acc_num)
    available_acc_num.remove(acc_num)
    return acc_num

class User():
    def __init__(self, name, acc_num):
        self.name = name
        self.acc_num = acc_num

class newUser(User):
    def __init__(self, name, acc_num, init_dps):
        super().__init__(name, acc_num)
        self.balance = 0
        self.init_dps = init_dps
        
    def deposit(self, date):
        self.balance = self.balance + self.init_dps
        print(f"You successfully deposit first deposit: {self.balance} on {date}")
        
    def information(self, date):
        print("Here is your account information")
        print(f'Name: {self.name}')
        print(f'Account Number: {self.acc_num}')
        print(f'Open Date: {date}')
        print(f'Account Balance: {self.balance}')

class eUser(User):
    def __init__(self, name, acc_num, balance):
        super().__init__(name, acc_num)
        self.balance = balance
        
    def deposit(self, amount, date):
        self.balance = self.balance + amount
        print(f"You successfully deposit {amount} on {date}")
        print(f'Your account balance is now: {self.balance}')
        
    def withdraw(self, amount, date):
        if amount > self.balance:
            print("You cannot withdraw the amount over your balance")
            print(f'Your account balance is {self.balance}')
        else:
            self.balance = self.balance - amount
            print(f'You withdraw {amount} on {date}')
            print(f'Your account balance is {self.balance}')
    
    def information(self, date):    
        print("Here is your account information")
        print(f'Name: {self.name}')
        print(f'Account Number: {self.acc_num}')
        print(f'Date: {date}')
        print(f'Account Balance: {self.balance}')
