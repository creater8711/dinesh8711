accounts = {}

def create_account(account_number, initial_balance=0):
    if account_number in accounts:
        print("Account already exists.")
    else:
        accounts[account_number] = initial_balance
        print("Account created successfully.")

def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        if amount <= accounts[account_number]:
            accounts[account_number] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

def check_balance(account_number):
    if account_number in accounts:
        return accounts[account_number]
    else:
        print("Account not found.")

create_account("12345", 1000)
deposit("12345", 500)
withdraw("12345", 200)

print("Balance:", check_balance("12345"))

