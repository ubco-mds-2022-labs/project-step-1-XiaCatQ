# import
import os

# Functions
def addAccount(n, aN, iA, B):
    """
    Store new account information
    
    n: name
    aN: accountNum
    iA: initial amount
    B: Balance
    
    """
    
    all_accounts = os.listdir() 
    if n == "" or aN == "":
        print("All fields required!")
        return

    for name_check in all_accounts:
        if n == name_check:
            print("Account Already Exists!")
            return
        else:
            new_file = open(n, "w")
            new_file.write(n + '\n')
            new_file.write(str(aN) + '\n')
            new_file.write(str(iA) + '\n')
            new_file.write(str(B) + '\n')
            new_file.close()
            
# Read (e.g. for validation)
def validate(n, aN):
    all_accounts = os.listdir()
    if n in all_accounts:
        try:
            file = open(n, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            accountNum = file_data[1]
            assert str(aN) == accountNum
            print("Validation Pass!")
            return True
        except:
            print("Please check your account number!")
    else:
        print("Please check your spell of name!")
    return
    

# Delete an existing account
def delAccount(n, aN):
    if validate(n, aN) == True:
        os.remove(n)
    

            

    
