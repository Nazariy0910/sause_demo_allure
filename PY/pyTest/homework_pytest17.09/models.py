def check_password(password):
    if not password:
        return "Error: password  cannot be blank" #####Перший варіант
    
    if len(password) < 6:
        return "Weak password"

    if len(password) <= 11:
        return "Normal password"

    if len(password) > 11:
        return "Good password"

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []     #######Дп

    def add_item(self, item_name):
        self.items.append(item_name) 

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
        else:
            raise ValueError('There are no products in basket')

    def get_count(self):
        return len(self.items)

    def clear(self):
        self.items.clear()