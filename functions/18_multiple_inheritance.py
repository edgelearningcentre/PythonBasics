class Father:
    father_name = " "

    def displayFatherName(self):
        print(self.father_name)

class Mother:
    Mother_name = " "

    def displayMotherName(self):
        print(self.Mother_name)

class  Child(Father,Mother):
    child_name = " "

    def displayChildName(self):
        print(self.child_name)

c1 = Child()
c1.father_name = "Neeraj"
c1.Mother_name = "Rajni"
c1.child_name = "Monish"
c1.displayFatherName()
c1.displayMotherName()
c1.displayChildName()