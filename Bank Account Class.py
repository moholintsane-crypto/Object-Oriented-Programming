class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Creating objects 
account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob")

# Using methods
account1.deposit(50)
account1.withdraw(30)
account2.deposit(200)
account2.withdraw(250)