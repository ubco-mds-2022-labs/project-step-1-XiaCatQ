# import 
from tkinter import *
import os
import bankingDS as ds
import sys
sys.path.append('C:\\Users\\sophiechen\\2022MDS\\Block 3\\Data-533\\project-step-1-XiaCatQ\\BankAccountSystem\\Structure')
import User as U
import calculation as Cal

from tkinter import *
    
master = Tk()
master.title("MDS Banking")
master.geometry('400x300')

def main():
    #Labels
    Label(master, text = "MDS Banking", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(master, text = "What would you like to do today?" , font = ("Calibri", 11)).grid(row = 1, sticky = N, pady = 5)

    #Buttons
    Button(master, text = "Sign Up", command = signup, font = ("Calibri", 11), width = 30).grid(row = 2, sticky = N, padx = 10)
    Button(master, text = "Sign In", command = signin,font = ("Calibri", 11), width = 30).grid(row = 3, sticky = N, padx = 10)
    master.mainloop()
    
def signup():
    # Vars
    global temp_name
    global temp_accountNum
    global temp_initialAmount
    global notif
    temp_name = StringVar()
    temp_acountNum = StringVar()
    temp_initialAmount= StringVar()
    
    # signup screen
    signup_screen = Toplevel(master)
    signup_screen.title("Sign up")
    signup_screen.geometry('400x300')
    
    # Labels
    Label(signup_screen, text = "Please enter the following information", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(signup_screen, text = "Name", font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(signup_screen, text = "initial deposit", font = ("Calibri", 11)).grid(row = 2, sticky = W)
    notif = Label(signup_screen, font = ("Calibri", 11))
    notif.grid(row = 3, sticky = N, pady = 10)
    
    # Entry
    Entry(signup_screen, textvariable = temp_name).grid(row = 1, column = 0)
    Entry(signup_screen, textvariable = temp_initialAmount).grid(row = 2, column = 0)
    
    # Button
    Button(signup_screen, text="Sign up", command = finish_signup, width = 15, font = ("Calibri", 11)).grid(row = 4, sticky = N, pady = 10)

def finish_signup():
    name = temp_name.get()
    accountNum = U.genAccNum()
    initialAmount = temp_initialAmount.get()
    all_accounts = os.listdir()
    
    if name == "" or accountNum == "":
        notif.config(fg = "red", text = "All fields required!")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg = "red", text = "Account Already Exists!")
            return
        else:
            C = U.newUser(name, accountNum, initialAmount)
            C.store()
            notif.config(fg = "green", text = "Account has been created.")   
            notif.config(fg = "green", text = f"Account Number is {accountNum}.")  
    
def signin_session():
    global signin_name
    
    all_accounts = os.listdir()
    signin_name = temp_signin_name.get()
    signin_accounntNum = temp_signin_accountNum.get()
    
    for name in all_accounts:
        if name == signin_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            accountNum = file_data[1]
            
            if signin_accounntNum == accountNum:
                signin_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Options")
                account_dashboard.geometry('400x300')
                
                #Labels
                Label(account_dashboard, text = "Account Options", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
                Label(account_dashboard, text = "Welcome " + name, font = ("Calibri", 11)).grid(row = 1, sticky = N, pady = 5)
                
                #Buttons
                Button(account_dashboard, text = "Personal Details", command = personal_details, font = ("Calibri", 11), width = 30).grid(row = 2, sticky = N, padx = 10)
                Button(account_dashboard, text = "Deposit", command = deposit, font = ("Calibri", 11), width = 30).grid(row = 3, sticky = N, padx = 10)
                Button(account_dashboard, text = "Withdraw", command = withdraw, font = ("Calibri", 11), width = 30).grid(row = 4, sticky = N, padx = 10)
                Label(account_dashboard).grid(row = 5, sticky = N, pady = 10)
                return
            else:
                signin_notif.config(fg = "red", text = "Password Incorrect")
                return
    signin_notif.config(fg = "red", text = "No Account Found ")

def personal_details():
    # Vars
    file = open(signin_name, "r")
    file_data = file.read()
    user_data = file_data.split("\n")
    details_name = user_data[0]
    details_accNum = user_data[1]
    details_initial = user_data[2]
    details_balance = user_data[3]
    E = U.eUser(details_name, details_accNum, details_balance)
    
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.geometry('400x300')

    #Labels
    Label(personal_details_screen, text = "Personal Details", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(personal_details_screen, text = E.information(20120112), font = ("Calibri", 11)).grid(row = 1, sticky = W)
    
def deposit():
    global temp_dep_amount
    global temp_dep_date
    temp_dep_amount = StringVar()
    temp_dep_date = StringVar()
    
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    deposit_screen.geometry('400x300')
    #Labels
    Label(deposit_screen, text = "Deposit Page", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(deposit_screen, text = "Amount", font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(deposit_screen, text = "Date", font = ("Calibri", 11)).grid(row = 2, sticky = W)
    
    # Entry
    Entry(deposit_screen, textvariable = temp_dep_amount).grid(row = 1, column = 1, padx = 5)
    Entry(deposit_screen, textvariable = temp_dep_date).grid(row = 2, column = 1, padx = 5)
                
    #Buttons
    Button(deposit_screen, text = "Confirm Deposit", command = finish_deposit, font = ("Calibri", 11), width = 30).grid(row = 3, sticky = N, padx = 10)
       
def finish_deposit():    
    file = open(signin_name, "r")
    file_data = file.read()
    user_data = file_data.split("\n")
    print(user_data)
    details_name = user_data[0]
    details_accNum = user_data[1]
    details_initial = user_data[2]
    details_balance = user_data[3]
    file.close()
    E = U.eUser(details_name, details_accNum, int(details_balance))
    
    file =  open(signin_name, "w") 
    file.write(details_name + '\n')
    file.write(details_accNum + '\n')
    file.write(details_initial + '\n')
    file.write(str(E.deposit(int(temp_dep_amount.get()), temp_dep_date)) + '\n')  # renew balance
    file.write("Deposit " + temp_dep_date.get() +": " + temp_dep_amount.get() + '\n')  # record transaction
    file.close()

    
def withdraw():
    global temp_w_amount
    global temp_w_date
    global temp_w_currency
    temp_w_amount = StringVar()
    temp_w_date = StringVar()
    temp_w_currency = StringVar()
    
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry('400x300')
    #Labels
    Label(withdraw_screen, text = "Withdraw Page", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(withdraw_screen, text = "Amount", font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(withdraw_screen, text = "Date", font = ("Calibri", 11)).grid(row = 2, sticky = W)
    Label(withdraw_screen, text = "Currency (CAD/TWD)", font = ("Calibri", 11)).grid(row = 3, sticky = W) # CAD or TWD
    
    # Entry
    Entry(withdraw_screen, textvariable = temp_w_amount).grid(row = 1, column = 1, padx = 5)
    Entry(withdraw_screen, textvariable = temp_w_date).grid(row = 2, column = 1, padx = 5)
    Entry(withdraw_screen, textvariable = temp_w_currency).grid(row = 3, column = 1, padx = 5)
                
    #Buttons
    Button(withdraw_screen, text = "Confirm Withdraw", command = finish_withdraw, font = ("Calibri", 11), width = 30).grid(row = 4, sticky = N, padx = 10)
    
def finish_withdraw(): 
    file = open(signin_name, "r")
    file_data = file.read()
    user_data = file_data.split("\n")
    details_name = user_data[0]
    details_accNum = user_data[1]
    details_initial = user_data[2]
    details_balance = user_data[3]
    file.close() 
    
    E = U.eUser(details_name, details_accNum, int(details_balance))
    if temp_w_currency.get() == "TWD":
        print(Cal.getEXRates())
        WM = E.withdraw(round(int(temp_w_amount.get()) / Cal.getEXRates(),0), temp_w_date)
    else:
        WM = E.withdraw(int(temp_w_amount.get()), temp_w_date)
    
    file =  open(signin_name, "w") 
    file.write(details_name + '\n')
    file.write(details_accNum + '\n')
    file.write(details_initial + '\n')
    file.write(str(WM) + '\n')  # renew balance
    file.write("Withdraw " + temp_w_date.get() +": " + temp_w_amount.get() + '\n')  # record transaction
    file.close()
        

    
def signin():
    # Vars
    global signin_screen
    global temp_signin_name
    global temp_signin_accountNum
    temp_signin_name = StringVar()
    temp_signin_accountNum = StringVar()
    # screen
    signin_screen = Toplevel(master)
    signin_screen.title("Sign In")
    signin_screen.geometry('400x300')
    # Labels
    Label(signin_screen, text = "Sign in to your account", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(signin_screen, text = "User Name", font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(signin_screen, text = "Account Number", font = ("Calibri", 11)).grid(row = 2, sticky = W)
    # Entry
    Entry(signin_screen, textvariable = temp_signin_name).grid(row = 1, column = 1, padx = 5)
    Entry(signin_screen, textvariable = temp_signin_accountNum, show = "*").grid(row = 2, column = 1, padx = 5)
    # Button
    Button(signin_screen, text="Signin", command = signin_session, width = 15, font = ("Calibri", 11)).grid(row = 3, sticky = W, pady = 5, padx = 5)
          
    
