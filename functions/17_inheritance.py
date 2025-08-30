class Car:

    def __init__(self):
        print("Car init")


    def set_info(self, color: str, mileage: float, type: str, seat_cap: int):
        self.color = color
        self.mileage = mileage
        self.type = type
        self.seat_cap = seat_cap

    def base_info(self):
        print(f"Color = {self.color}")
        print(f"mileage = {self.mileage}")
        print(f"type = {self.type}")
        print(f"seat_Cap = {self.seat_cap}")


class Audi(Car):

    def __init__(self):
        super().__init__()
        print("Audi Init")

    def set_audi_info(
        self,
        color: str,
        mileage: float,
        type: str,
        seat_cap: int,
        electric: bool,
        city: str,
    ):

        self.set_info(color, mileage, type, seat_cap)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"electric = {self.electric}")
        print(f"city = {self.city}")

    def show_full_details(self):
        self.base_info()
        self.audi_info()

c1 = Audi()
# c1.set_info("black",18.5,"SUV",6)
c1.set_audi_info("black", 18.5, "SUV", 6, True, "Mumbai")

# c1 = Car("black",18.5,"SUV",6)
# c1.base_info()
# c1.audi_info()
c1.show_full_details()
