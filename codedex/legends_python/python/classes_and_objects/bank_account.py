"""
Instructions
It's time to open up a bank account! 🏦

Create a file called bank_accounts.py.

Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

first_name (string)
last_name (string)
account_id (integer)
account_type (string)
pin (integer)
balance (float)
Next, let's create three methods:

.deposit(): Add money into the account and return the new balance.
.withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
.display_balance(): Print the current value of balance.
Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

Deposit $96 into the account.
Withdraw $25 from the account.
Print the current account balance.

"""


class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Balance after deposit of ${amount}:  {self.balance}"
  
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return f"Balance after withdrawal of ${amount}: {self.balance}"
  
    def display_balance(self):
        return f"Current Balance: ${self.balance}"

bank_account = BankAccount("Jerry", "Stone", 872143, "Checking", 9962, 3174.56)

print(bank_account.display_balance())
print()

print(bank_account.deposit(100))
print(bank_account.withdraw(50.92))

print()
print(bank_account.display_balance())

