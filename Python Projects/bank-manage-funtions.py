balance = 2500

def create_account(initial_deposit):
    global balance
    balance = initial_deposit

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        return amount
    else:
        return "Insufficient funds"

def check_balance():
    return balance

create_account(2500)
print("Initial balance:", check_balance())

deposit(500)
print("After deposit:", check_balance())

withdraw(200)
print("After withdrawal:", check_balance())
