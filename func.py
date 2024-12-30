import time

# Function to create a new account
def create_account():
    global account_number, customer_name
    customer_name = input("Pls enter your name: \n")
    account_number = int(input("Pls enter a new account number to create one: \n"))
    default_deposit = int(input("Pls make a deposit: \n"))

    with open(f"{account_number} logs.txt", "w") as c_a:
        c_a.write(f"This account belongs to {customer_name} \n")
    with open(f"{account_number} logs.txt", "a") as c_a:
        c_a.write(f"default deposit is {default_deposit} \n")
    with open(f"{account_number}.txt", "w") as c_a:
        c_a.write(f"Your balance is {default_deposit}")


# Function to check balance
def check_balance():
    global account_number, customer_name
    account_number = int(input("Pls enter the account number: \n"))
    with open(f"{account_number}.txt", "r") as c_a:
        print(f"Your balance is: {c_a.read()}")
    with open(f"{account_number} logs.txt", "a") as c_a:
        c_a.write(f"Balance checked at {time.ctime()} \n")

# Function to deposit money
def deposit_money():
    global account_number
    account_number = int(input("Pls enter the account number: \n"))
    deposit_amount = int(input("Pls enter the amount to deposit: \n"))

    with open(f"{account_number}.txt", "r") as c_a:
        current_balance_str = c_a.read()
        current_balance = int(current_balance_str.split()[-1])  # Extract numeric balance

    new_balance = current_balance + deposit_amount

    with open(f"{account_number}.txt", "w") as c_a:
        c_a.write(f"Your balance is {new_balance}")
    
    with open(f"{account_number} logs.txt", "a") as c_a:
        c_a.write(f"Deposited {deposit_amount} at {time.ctime()} \n")
    
    # Debugging print statement
    print(f"Deposit successful. New balance: {new_balance}")

# Function to withdraw money
def withdraw_money():
    global account_number
    account_number = int(input("Pls enter the account number: \n"))
    withdraw_amount = int(input("Pls enter the amount to withdraw: \n"))

    with open(f"{account_number}.txt", "r") as c_a:
        current_balance_str = c_a.read()
        current_balance = int(current_balance_str.split()[-1])  # Extract numeric balance

    if withdraw_amount <= current_balance:
        new_balance = current_balance - withdraw_amount
        with open(f"{account_number}.txt", "w") as c_a:
            c_a.write(f"Your balance is {new_balance}")
        
        with open(f"{account_number} logs.txt", "a") as c_a:
            c_a.write(f"Withdrew {withdraw_amount} at {time.ctime()} \n")
        
        # Debugging print statement
        print(f"Withdrawal successful. New balance: {new_balance}")
    else:
        print("Insufficient funds")


# END of functions
