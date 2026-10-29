class Car:
    def __init__(self, brand, speed):
        self.brand= brand
        self.speed= speed

    def describe(self):
        print(f"Машина: {self.brand}, max speed:{self.speed}")


car1 = Car("Toyota", 2400)
car2 = Car("BMW", 120)

car1.describe()
car2.describe()