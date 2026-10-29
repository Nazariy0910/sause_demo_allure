class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model}: included")

    def turn_off(self):
        print(f"{self.brand} {self.model}: switched off")

    def describe(self):
        print(f"Device: {self.brand}, {self.model}")

class Phone(Device):
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def call(self, contact):
        print(f"{self.brand}: call {contact} with number {self.number}")

    def describe(self):
        super().describe()
        print(f"Number: {self.number}")

device1 = Device("Apple", "MacBook")
device2 = Phone("Samsung", "Galaxy S24", "+ 420999467881" )


device1.describe()
device1.turn_on()
device1.turn_off()

print( 30 * "=" )

device2.describe()
device2.turn_on()
device2.call('vASYA')
device2.turn_off()
