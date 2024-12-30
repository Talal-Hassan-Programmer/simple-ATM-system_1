#THis Is the Main file for this project.

#imports

import func as f 



#Main code to run program

while True:
    ch = ["create account", "deposit", "withdraw", "check balance"]
    Choice = input(f"What do you want to do {ch}: \n").lower()

    if Choice in ch:
        if Choice == "create account":
            f.create_account()
        elif Choice == "deposit":
            f.deposit_money()
        elif Choice == "withdraw":
            f.withdraw_money()
        elif Choice == "check balance":
            f.check_balance()
    else:
        print("Invalid Choice")
        print("Pls retry")

