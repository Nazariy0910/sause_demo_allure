class Product:
    def __init__ (self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Stock: {self.quantity}")

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Add {amount} piece. Now in stock {self.quantity}")

    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f'Soll {amount} piece')
        else:
            print(f"Insufficient stock. In stock: {self.quantity}")

dress = Product("Платье", 1500)
dress.show_info()
dress.add_stock(10)
dress.sell(3)
dress.show_info()
dress.sell(10)  

print("-" * 40)

shoes = Product("Кроссовки", 2500, 2)
shoes.show_info()
shoes.add_stock(5)
shoes.sell(4)