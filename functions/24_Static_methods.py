
from datetime import datetime

class Calender():

    def __init__(self) -> None:
        self.events =[]

    def add_events(self,event_name):
        self.events.append(event_name)

    def display_events(self) -> None:
        print(f"Events = {self.events}")



    @staticmethod
    def is_weekend(date:datetime):
        if date.weekday() > 4:
            print("It is a weekend")
        else:
            print("It is a weekday")


obj1 = Calender()
obj1.add_events("DSA")
obj1.add_events("Python")
obj1.add_events("Coding")
obj1.display_events()


current_date = datetime.now()
print(current_date)
Calender.is_weekend(current_date)