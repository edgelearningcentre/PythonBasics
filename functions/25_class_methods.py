class Student:
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    
    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


    @classmethod
    def create_student_using_params(cls,name,age,gender):
        obj = cls(name,age,gender)
        return obj
    


    @classmethod
    def create_student_from_file(cls,file_name):
        f = open(file_name,"r")
        studentdata = f.read()
        name, age, gender = studentdata.split()
        f.close()
        obj = cls(name,age,gender)
        return obj 



s1 = Student.create_student_using_params("Neeraj",20,"Male")
s1.display()
print("---------------------------------------------")
s2 = Student.create_student_from_file("student.txt")
s2.display()