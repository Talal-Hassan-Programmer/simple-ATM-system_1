# Simple ATM System

## Overview
This is a simple ATM system implemented in Python. The system allows users to create accounts, deposit money, withdraw money, and check their balance. The account data is stored in text files for simplicity.

## Features
- **Create Account**: Users can create a new account with a unique account number and make an initial deposit.
- **Deposit Money**: Users can deposit money into their account.
- **Withdraw Money**: Users can withdraw money from their account if sufficient funds are available.
- **Check Balance**: Users can check the current balance of their account.

## Getting Started
### Prerequisites
- Python 3.x
- A text editor or IDE for running Python scripts

### Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/simple-atm-system.git
    cd simple-atm-system
    ```

2. **Create Two Files**:
    - `banking_functions.py`
    - `main_script.py`

### Usage
1. **Run the Main Script**:
    ```bash
    python main_script.py
    ```

2. **Follow the On-Screen Prompts**: 
    - Choose an action (create account, deposit, withdraw, check balance) by typing the corresponding choice.
    - Enter the required information when prompted (e.g., account number, amount to deposit/withdraw).

### Example
```plaintext
What do you want to do ['create account', 'deposit', 'withdraw', 'check balance']:
create account
Pls enter your name:
John Doe
Pls enter a new account number to create one:
12345
Pls make a deposit:
500
Action create account completed.

What do you want to do ['create account', 'deposit', 'withdraw', 'check balance']:
deposit
Pls enter the account number:
12345
Pls enter the amount to deposit:
100
Deposit successful. New balance: 600

What do you want to do ['create account', 'deposit', 'withdraw', 'check balance']:
check balance
Pls enter the account number:
12345
Your balance is: Your balance is 600
Balance checked at Mon Dec 30 16:30:00 2024
