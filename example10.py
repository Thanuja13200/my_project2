class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show(self):
        print("Balance:", self.__balance)

a = Account(2000)
a.deposit(500)
a.withdraw(300)
a.show()