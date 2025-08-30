class Bank:
    def __init__(self) -> None:
        self.__balance = 0

    def display(self) -> None:
        print(f"Your balance = {self.__balance}")


obj = Bank()
obj.display()
obj.__balance =100
obj.display()