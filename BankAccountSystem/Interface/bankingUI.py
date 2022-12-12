# import 
import tkinter as tk
import os

# Main Screen
master = tk.Tk()
master.title("MDS Banking")

# Functions
def finish_signup():
    name = temp_name.get()
    accountNum = temp_accountNum.get()
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
            new_file = open(name, "w")
            new_file.write(name + '\n')
            new_file.write(accountNum + '\n')
            new_file.write(initialAmount + '\n')
            new_file.close()
            notif.config(fg = "green", text = "Account has been created.")
            
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
    Button(signup_screen, text="Sign up", command = signup, width = 15, font = ("Calibri", 11)).grid(row = 3, sticky = N, pady = 10)
    
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
                account_dashboard.title("Dashboard")
                
                #Labels
                Label(account_dashboard, text = "Account Dashboard", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
                Label(account_dashboard, text = "Welcome" + name, font = ("Calibri", 11)).grid(row = 1, sticky = N, pady = 5)
                
                #Buttons
                Button(account_dashboard, text = "Personal Details", font = ("Calibri", 11), width = 30).grid(row = 2, sticky = N, padx = 10)
                Button(account_dashboard, text = "Deposit", font = ("Calibri", 11), width = 30).grid(row = 3, sticky = N, padx = 10)
                Button(account_dashboard, text = "Withdraw", font = ("Calibri", 11), width = 30).grid(row = 4, sticky = N, padx = 10)
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
    details_initial = user_data[2]
    details_balance = user_data[3]
    
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    
    #Labels
    Label(personal_details_screen, text = "Personal Details", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(personal_details_screen, text = "Name: " + details_name, font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(personal_details_screen, text = "Initial Deposit: CAD" + details_initial, font = ("Calibri", 11)).grid(row = 2, sticky = W)
    Label(personal_details_screen, text = "Balance: CAD" + details_balance, font = ("Calibri", 11)).grid(row = 3, sticky = W)
    
def deposit():
    print("deposit")
def withdraw():
    print("withdraw")
    
        
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
    # Labels
    Label(signin_screen, text = "Sign in to your account", font = ("Calibri", 11)).grid(row = 0, sticky = N, pady = 10)
    Label(signin_screen, text = "User Name", font = ("Calibri", 11)).grid(row = 1, sticky = W)
    Label(signin_screen, text = "Account Number", font = ("Calibri", 11)).grid(row = 2, sticky = W)
    # Entry
    Entry(signin_screen, textvariable = temp_signin_name).grid(row = 1, column = 1, padx = 5)
    Entry(signin_screen, textvariable = temp_signin_accountNum, show = "*").grid(row = 2, column = 1, padx = 5)
    # Button
    Button(signin_screen, text="Signin", command = signin_session, width = 15, font = ("Calibri", 11)).grid(row = 3, sticky = W, pady = 5, padx = 5)
     
          
    
