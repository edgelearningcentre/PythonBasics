# Many forms # Method over riding 

class Animal():
    
    def sound(self):
        print("Animal Speaking")


class Dog(Animal):
    pass
    # def sound(self):
    #     print("Bhaw bhaw")


class Cat(Animal):
    def sound(self):
        print("mew mew")


obj = Dog()
obj.sound()  # it will print bhaw bhaw ie. overriding 


# over loading is not in python 

