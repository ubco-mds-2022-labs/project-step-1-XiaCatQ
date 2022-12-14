import random
import calculation as cal
import sys
sys.path.append('C:\\Users\\sophiechen\\2022MDS\\Block 3\\Data-533\\project-step-1-XiaCatQ\\BankAccountSystem\\Interface')
import bankingDS as ds

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
        self.balance = init_dps
        self.init_dps = init_dps
        
    def information(self, date):
        print("Here is your account information")
        print(f'Name: {self.name}')
        print(f'Account Number: {self.acc_num}')
        print(f'Open Date: {date}')
        print(f'Account Balance: {self.balance}')
        
    def store(self):
        ds.addAccount(self.name, self.acc_num, self.init_dps, self.balance)

class eUser(User):
    def __init__(self, name, acc_num, balance):
        super().__init__(name, acc_num)
        self.balance = balance
        
    def deposit(self, amount, date):
        self.balance = self.balance + amount
        print(f"You successfully deposit {amount} on {date}")
        print(f'Your account balance is now: {self.balance}')
        return self.balance
        
    def withdraw(self, amount, date):
        amount = cal.service(amount)
        if amount > self.balance:
            print("You cannot withdraw the amount over your balance after service fee")
            print(f'Your account balance is {self.balance}, Service fee is CAD 3')
        else:
            self.balance = self.balance - amount
            print(f'You withdraw {amount} on {date}')
            print(f'Your account balance is {self.balance}')
            return self.balance
    
    def information(self, date):         
        return f"Here is your account information \nName: {self.name}\nAccount Number: {self.acc_num}\nDate: {date}\nAccount Balance: {self.balance}"  
    
