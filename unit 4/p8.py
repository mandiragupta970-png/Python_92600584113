from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Bank):
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def calculate_interest(self):
        return self.__balance * 0.05

a = SavingsAccount(1000)
a.deposit(500)

print("Balance:", a.get_balance())
print("Interest:", a.calculate_interest())
