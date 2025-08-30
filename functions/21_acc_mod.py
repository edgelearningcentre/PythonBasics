# protected
# write single underscore before the variable 

class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter Father Name")
        self._bank_balance = int(input("Enter Father bank_balance"))
        self.__phone = input("Enter Phone Model = ")

    def display(self) -> None:
        print(f" Father Name = {self.father_name}")
        print(f" Father bank_balance  = {self._bank_balance}")
        print(f" Father phone  = {self.__phone}")



class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter Child name")

    def displayChildInfo(self):
        print(f"Child name = {self.child_name}")
        print(f"my father has {self._bank_balance} amount")


child = Child()
child.displayChildInfo()