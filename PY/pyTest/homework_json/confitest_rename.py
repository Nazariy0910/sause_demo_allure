# conftest.py
import pytest
from models import User
import json

@pytest.fixture()
def user():
    return User('Alex', 'pass123')

@pytest.fixture()
def empty_user_password():
    return User('Alex', '')

@pytest.fixture()
def logged_in_user():
    print('\n[SETUP] Создаём пользователя и логиним его')
    user = User('Alex', 'pass123')
    user.login()

    yield user

    print('\n[TEARDOWN] Разлогиниваем пользователя')
    user.logout()


@pytest.fixture
def two_users():
 admin = User("Admin", "admin_pass")
 guest = User("Guest", "guest_pass")
 admin.login()
 return admin, guest

@pytest.fixture
def products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)


