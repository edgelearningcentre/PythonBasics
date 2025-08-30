# data hiding using access modifiers
# Three methods 
# 1. Public  Bi default all are in public state
# 2. Protected
# 3. Private  access within in the class and put __name of the variable
from random import randint

class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.__account = randint(100000,9999999)
        self.__balance = 0


    def display_balance(self) -> None:
        "values getter from private values"
        print(self.__balance)

    def set_balance(self,new_amount):
        "setter"
        self.__balance = new_amount

    def display(self) -> None:
        print(f"Account Number  = {self.__account}")
        print(f"Name = {self.name}")

        print(f"balance = {self.__balance}")



obj = Bank()
obj.display()
print("=---------------=")
print(obj._Bank__balance)    # Yes in theoritical and strictly followed Never do this ( Name mangling)