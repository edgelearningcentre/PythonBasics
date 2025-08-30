class Student:


    def __init__(self):      # constructor or initializer
        self.name=input("Enter Name = ")
        self.age =int(input("Enter age = "))
        self.gender =input("Enter gender = ")
        self.roll_number =int(input("Enter roll number = "))

        
    # class attributes
    # name = ''
    # age =0
    # roll_number = 0
    # gender = ""
    # address = ""

    # Methods
    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Roll Number  = {self.roll_number}")


    # def set_info(self):
    #     self.name=input("Enter Name = ")
    #     self.age =int(input("Enter age = "))
    #     self.gender =input("Enter gender = ")

    #     self.roll_number =int(input("Enter roll number = "))


s1 = Student()  # to create an object from the class 
s1.info()
# s1.set_info()

s2 = Student()  # to create an object from the class 
# s2.set_info()

# s1.info()
# s2.info()


