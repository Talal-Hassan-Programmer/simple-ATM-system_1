#This file is for func in this program.
#importing
import time


# Functions

#creating a account
def create_account():
    global account_number,customer_name
    customer_name = input("PLs enter you name: \n")
    account_number = int(input("pls enter a new account number to create one: \n"))
    default_deposit = int(input("Pls make a deposit : \n"))
    
    with open(f"{account_number} logs.txt","w") as c_a:
        c_a.write(f"This account belongs to {customer_name} \n")

    with open(f"{account_number} logs.txt","a") as c_a:
         c_a.write(f"default deposit is {default_deposit} \n")

    with open(f"{account_number}.txt","w") as c_a:
        c_a.write(f"Balance = {default_deposit}")



#checking balance
def check_balance():
    global account_number,customer_name
    account_number = int(input("Pls enter the account number: \n"))
    
    with open(f"{account_number}.txt","r") as c_a:
        print(f"Your balance is : {c_a.read()}")
    with open(f"{account_number} logs.txt","a") as c_a:
        c_a.write(f"Balnce checked at {time} \n")


#deposit moneu
def deposit_money():
    global account_number,customer_name


#withdraw money
def withdraw_money():
    global account_number,customer_name


#END