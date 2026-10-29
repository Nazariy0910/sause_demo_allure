class BankAccount:
    def __init__(self, owner, initial_balance = 0):
        self.owner = owner              #Публічний - доступний всюди
        self._account_number = 'CZ123456' # Захищений - __некивай
        self.__balance = initial_balance    # Приватний - пряче атрибут

    def deposit(self, amount):
        if amount <=0:
            raise ValueError('NONONONON')
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('nonononono')
        if amount > self.__balance:
            raise ValueError(f"NNNNNNNNNOOOOOOOOO{self.__balance}")
        self.__balance -= amount
        print(f"знято {amount} balance {self.__balance}")

    def get_balance(self):
        return self.__balance

    def get_info(self):
        return(f"{self.owner},{self.account},{self.__balance}")


account = BankAccount("Oleg", initial_balance=1001)
print(account.owner)
print(account._account_number)

account.deposit(500)
account.withdraw(200)
print(account.get_info())
print(account.get_balance())

try:
    account.withdraw(9999)
except ValueError as e:
    print(f'no = {e}')



