class BankAccount: 
    def __init__(self, name, balance): 
        self.name = name 
        self.balance = balance 
 
    def deposit(self, amount): 
        self.balance += amount 
 
    def withdraw(self, amount): 
        if amount <= self.balance: 
            self.balance -= amount 
        else: 
            print("Insufficient balance") 