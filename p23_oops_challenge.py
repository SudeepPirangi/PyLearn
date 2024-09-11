"""
A Challenge question on Python Classes
"""

# 1. Create a bank "Account" with 
# attributes as "owner" and "balance"
# methods as "deposit" and "withdraw"
# Condition: Withdrawals may not exceed available balance

print("\n1. Bank Account")

class Account():
    """A Bank Account class"""

    def __init__(self, owner = "", balance = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Hi {self.owner}! Your available balance - ${self.balance}"

    def deposit(self, amount):
        """Adds given money into account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount ${amount}. Available balance is ${self.balance}")
        else:
            print(f"Deposit is declined as given amount ${amount} is invalid.")

    def withdraw(self, amount):
        """Withdraws amount and returns balance after withdrawal"""
        if amount > self.balance:
            print(f"Withdrawal of ${amount} declined due to insufficient balance - ${self.balance}.")
        elif amount <= 0:
            print(f"Withdrawal declined as amount ${amount} is invalid.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} is successful. Remaining balance - ${self.balance}")

acc1 = Account('Sudeep', 1000000)

print(acc1)
print(acc1.owner)
print(acc1.balance)

acc1.deposit(500000)
acc1.withdraw(750000)
acc1.withdraw(5000000)
