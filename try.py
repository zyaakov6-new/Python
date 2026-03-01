class Bank:
    def __init__(self, owner:str, balance:float = 0.0):
        self.owner = owner.strip().title()
        self.balance = balance
        
    def withdraw(self, amount:float):
        if self.balance < amount:
            print("Insufficient Funds!")
            return
        if amount < 0:
            print("Amount must be positive!")
            return
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
            
    def deposit(self, amount: float):
        if amount < 0:
            print("Amount must be positive!")
        else:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")    
            
    def get_balance(self):
        return self.owner + "'s current balance is " + str(self.balance)
        
        

owner = input("What's the name of the owner? ")
bank1 = Bank(owner)
while True:
    try:
        prompt = int(input("\n1 = withdraw | 2 = deposit | 3 = show balance | 0 = quit\n>").strip())
    except ValueError:
        print("Invalid input!")
        continue
    if prompt == 0:
        print(f"Goodbye, {bank1.owner}")
        break
    if prompt not in (1,2,3):
        print("Invalid input!")
        continue
    elif prompt == 1:
        try:
            amount = float(input("How much money would you like to withdraw ? "))
        except ValueError:
            print("Invalid input!")
            continue
        bank1.withdraw(amount)
    elif prompt == 2:
        try:
            amount = float(input("How much money would you like to deposit ? "))
        except ValueError:
            print("Invalid input!")
            continue
        if amount < 0:
            print("Amount must be positive!")
        else:
            bank1.deposit(amount)
    elif prompt == 3:
        print(bank1.get_balance())