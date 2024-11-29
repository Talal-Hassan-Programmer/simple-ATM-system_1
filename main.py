#THis Is the Main file for this project.

#imports

import func as f 



#Main code to run program

ch = ["create account","deposit","withdraw"]

Choice = input(f"What do you want to do {ch} : \n").lower()

if Choice in ch:
    if Choice == "create account":
        f.create_account()
    elif Choice == "deposit":
        f.deposit_money()
    elif Choice == "withdraw":
        f.withdraw_money()
elif Choice not in ch:
    print("Invalid Choice")
    print("pls retry")
