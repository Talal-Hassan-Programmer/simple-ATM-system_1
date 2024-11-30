#This file is for func in this program.


# Functions

#creating a account
def create_account():
    global account_number,customer_name
    customer_name = input("PLs enter you name: \n")
    account_number = int(input("pls enter a new account number to create one: \n"))
    default_deposit = int(input("Pls make a deposit : \n"))
    
    with open(f"{account_number} logs","w") as c_a:
        c_a.write(f"This account belongs to {customer_name} ")

    with open(f"{account_number} logs","a") as c_a:
         c_a.write(f"default deposit is {default_deposit}")

    with open(f"{account_number}","w") as c_a:
        c_a.write(f"x = {default_deposit}")



#checking balance
def check_balance():
    global account_number,customer_name


#deposit moneu
def deposit_money():
    global account_number,customer_name


#withdraw money
def withdraw_money():
    global account_number,customer_name


#END