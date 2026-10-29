class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"Transport: {self.brand}, max speed {self.speed}")

    def move(self):
        print(f"{self.brand} ride....")



class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery):
            self.brand = brand
            self.speed = speed
            self.battery = battery

    def charge(self):
         self.battery = 100
         print(f"{self.brand} charged to 100%")

    def describe(self):
        print(f"Transport: {self.brand}, max speed {self.speed}, charge battery{self.battery}%")


car1 = Vehicle("Skoda","320")
car2 = ElectricCar("Tesla","120", 50)


car1.describe()
car1.move()

car2.describe()
car2.move()
car2.charge()
car2.describe()