class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount > 0:
            self.__balance -= amount
            print("Withdrew:", amount)
        else:
            print("Invalid withdrawal amount")
    
    def display_balance(self):
        print("Current balance:", self.__balance)


acc = BankAccount(12000)
acc.deposit(5000)
acc.withdraw(2000)
acc.display_balance()

    