class Student:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter Age = "))

    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")


    def change_name(self,new_name:str):    # parameterized constructor
        self.name = new_name


s1 = Student()
s1.display()
s1.change_name("xyz")
s1.display()
