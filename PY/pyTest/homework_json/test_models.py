# test_models.py

from PY.pyTest.homework_json.models import add, subtract, is_even, check_age
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 3) == 7

def test_is_even_true():
    assert  is_even(4) == True

def test_is_even_false():
    assert  is_even(7) == False

def test_check_age_adult():
    assert check_age(25) == 'Доступ разрешён'

def test_check_age_minor():
    assert check_age(15) == 'Доступ запрещён'

def test_check_age_negative():
    assert check_age(-18) == 'Ошибка: возраст не может быть отрицательным'

def test_check_age_boundary():
    assert check_age(18) == 'Доступ разрешён'
    assert check_age(17) == 'Доступ запрещён'

def test_user_is_logged_in(logged_in_user):
    assert logged_in_user.is_logged_in == True

def test_user_info_while_logged_in(logged_in_user):
    assert logged_in_user.get_info() == 'Alex | залогинен: True'

def test_user_get_info(user):
    user.login()
    assert user.get_info() == 'Alex | залогинен: True'

def test_user_initial_state(user):
    assert user.is_logged_in == False

def test_user_login(user):
    user.login()
    assert user.is_logged_in == True

def test_user_logout(user):
    user.login()
    user.logout()
    assert user.is_logged_in == False

def test_login_empty_password(empty_user_password):
    with pytest.raises(ValueError):
        empty_user_password.login()