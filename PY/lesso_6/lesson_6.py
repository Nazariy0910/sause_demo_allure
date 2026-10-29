
class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, amount):
        self.stock += amount
        print(f"Added {amount} units of {self.name}. Total stock: {self.stock}")

    def sell(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            print(f"Sold {amount} units of {self.name}. Remaining stock: {self.stock}") 
        else:
            print(f"Insufficient stock for {self.name}. Available stock: {self.stock}")

    def get_info(self):
        return f"Product: {self.name} | Price: ${self.price} | Stock: {self.stock}"

product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 25)



product1.add_stock(5)
product2.add_stock(10)


product1.sell(2)
product2.sell(5)

print(product1.get_info())
print(product2.get_info())