import random
import time
from datetime import datetime


def is_valid_email(email):
    """Проверяет что email содержит @ и точку."""
    if "@" in email and "." in email:
        return True
    return False


def is_valid_password(password):
    """Проверяет что пароль не короче 8 символов."""
    return len(password) >= 8


def generate_test_email():
    """Генерирует уникальный тестовый email на основе текущего времени."""
    unique_number = int(time.time())
    return f"testuser_{unique_number}@qa-course.cz"


def generate_user():
    """Возвращает случайные данные для тестового пользователя."""
    age = random.randint(18, 65)
    browser = random.choice(["Chrome", "Firefox", "Safari", "Edge"])
    date = datetime.now().strftime("%d-%m-%Y")
    return age, browser, date


def build_url(path, domain="https://test.myshop.cz"):
    """Собирает полный URL из домена и пути."""
    if not path:
        return "Ошибка: путь не может быть пустым"
    return domain + "/" + path


def log(action, status):
    """Выводит строку лога с временной меткой."""
    now = datetime.now().strftime("%H:%M:%S")
    icon = "✅" if status.lower() == "passed" else "❌"
    print(f"[{now}] {icon} {status.upper()}: {action}")



def is_valid_phone(phone: str):
    return len(phone) == 9 and phone.isdigit()


def calculate_discount(price, percent):
    try:
        percent < 0 or percent > 100
    except ValueError("Need procent with 0-100%"):
        return price * (1 - percent / 100)


def format_report(title, passed, failed):
    total = passed + failed
    return (
        f"=== {title} ===\n"
        f"Passed: {passed}\n"
        f"Failed: {failed}\n"
        f"Total: {total}"
    )


print(is_valid_phone("777123456"))  
print(is_valid_phone("77712345"))   
print(is_valid_phone("77712345a"))  


print(calculate_discount(100, 20))  

report = format_report("Regression Test Suite", 12, 3)
print("\n" + report)