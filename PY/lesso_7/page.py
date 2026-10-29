class BasePage:
    """Базовый класс для всех страниц. Содержит общие методы."""

    def __init__(self, url):
        self._url       = url      # защищённый
        self._is_loaded = False    # защищённый

    def open(self):
        self._is_loaded = True
        print(f"🌐 Открываем страницу: {self._url}")

    def is_loaded(self):
        return self._is_loaded

    def take_screenshot(self, filename):
        if not self._is_loaded:
            raise RuntimeError("Нельзя сделать скриншот — страница не открыта")
        print(f"📸 Скриншот сохранён: {filename}")


class LoginPage(BasePage):

    def __init__(self):
        # Прописываем атрибуты родителя вручную — наш __init__ заменяет родительский
        self._url        = "https://myshop.cz/login"
        self._is_loaded  = False
        self.__last_login = None

    def enter_credentials(self, email, password):
        if not self.is_loaded():
            raise RuntimeError("Страница не открыта")
        print(f"⌨️  Вводим email: {email}")
        print(f"⌨️  Вводим пароль: {'*' * len(password)}")

    def click_login(self):
        print("🖱️  Кликаем кнопку Войти")

    def login(self, email, password):
        self.open()
        self.enter_credentials(email, password)
        self.click_login()
        self.__last_login = email
        print(f"✅ Выполнен вход как: {email}\n")

    def get_last_login(self):
        return self.__last_login


class CartPage(BasePage):

    def __init__(self):
        self._url       = "https://myshop.cz/cart"
        self._is_loaded = False
        self.__items    = []

    def add_item(self, product_name, price):
        if not self.is_loaded():
            raise RuntimeError("Страница корзины не открыта")
        self.__items.append({"name": product_name, "price": price})
        print(f"🛒 Добавлен товар: {product_name} ({price} Kč)")

    def get_total(self):
        total = 0
        for item in self.__items:
            total += item["price"]
        return total

    def checkout_summary(self):
        print("\n--- КОРЗИНА ---")
        for item in self.__items:
            print(f"  {item['name']}: {item['price']} Kč")
        print(f"  ИТОГО: {self.get_total()} Kč")


# Имитируем сценарий автотеста
print("=" * 40)
print("ТЕСТ: Покупка товара")
print("=" * 40)

login_page = LoginPage()
login_page.login("ivan@test.com", "SuperSecret123")

cart_page = CartPage()
cart_page.open()
cart_page.add_item("Летнее платье", 1500)
cart_page.add_item("Джинсы", 2900)
cart_page.checkout_summary()
cart_page.take_screenshot("cart_final.png")

print(f"\nПоследний вход: {login_page.get_last_login()}")