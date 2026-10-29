# models.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def is_even(n):
    return n % 2 == 0

def check_age(age):
    if age < 0:
        return 'Ошибка: возраст не может быть отрицательным'
    if age < 18:
        return 'Доступ запрещён'
    return 'Доступ разрешён'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    def login(self):
        if not self.password:
            raise ValueError('Пароль не может быть пустым')
        self.is_logged_in = True

    def logout(self):
        self.is_logged_in = False

    def get_info(self):
        return f'{self.username} | залогинен: {self.is_logged_in}'