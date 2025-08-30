
class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter Father Name")
        self._bank_balance = int(input("Enter Father bank_balance"))
        self.__phone = input("Enter Phone Model = ")


    # def __str__(self) -> str:
    #     return "I am a string dunder method"


    def __str__(self) -> str:
        return f" Father Name = {self.father_name} \nFather bank_balance  = {self._bank_balance} \n Father phone  = {self.__phone}"



    def display(self) -> None:
        print(f" Father Name = {self.father_name}")
        print(f" Father bank_balance  = {self._bank_balance}")
        print(f" Father phone  = {self.__phone}")


obj = Father()
print("-------------")
print(obj)