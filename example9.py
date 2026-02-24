class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("Minimum balance should be 1000")
        else:
            self.balance -= amount
            print("Balance:", self.balance)

s = SavingsAccount(5000)
s.withdraw(4500)