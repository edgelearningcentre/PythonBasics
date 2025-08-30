from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def sound(self):
        pass


class Audi(Car):
    def __init__(self,engine)-> None:
        self.engine = engine

    def sound(self):
        print("Sports Sound ")


obj = Audi("1200")
obj.sound()
