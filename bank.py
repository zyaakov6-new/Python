# A simple bank account class with deposit and withdraw methods
class BankAcount:
    def __init__(self, owner):
        self.balance = 0
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


owner = input("Enter the account owner's name: ")
account = BankAcount(owner)
while True:
    order = input(
        "Enter 'd' to deposit, 'b' to check balance, 'w' to withdraw, or 'q' to quit: ")
    if order == 'q':
        break
    elif order == 'b':
        print(f"{account.owner}'s balance is {account.balance}")
    elif order == 'd':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif order == 'w':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    else:
        print("Invalid order")

print(f"{account.owner}'s balance is {account.balance}")
