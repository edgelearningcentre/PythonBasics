class Student:
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self._age = age
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self,newgender):
        self._gender = newgender
         

s1 = Student("Neeraj",100,"Male")
print(s1.gender)
s1.gender = "Female"
print(s1.gender)