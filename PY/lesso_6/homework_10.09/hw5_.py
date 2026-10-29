class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        print(f"🛒 Add product: {name} ({price} Kč)")

    def remove_last(self):
        if self.items:
            self.items.pop()
            print("Delete last product")
        else:
            print("Trash is empty")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def checkout(self):
        print(f"Customer: {self.customer_name}")
        for item in self.items:
            print(f"{item['name']}: {item['price']} Kč")
        print(f"Total: {self.get_total()} Kč")


cart = Cart(" Olexander")

cart.add_item("Laptop", 25000)
cart.add_item("Mouse", 500)
cart.add_item("Keyboard", 1500)
cart.add_item("Blanket", 300)

print()

cart.remove_last()

print()

cart.checkout()