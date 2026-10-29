from models import check_password, ShoppingCart
import pytest 

def test_password_empty():
    assert check_password("") == 'Error: password  cannot be blank'

def test_password_weak():
    assert check_password("12345") == "Weak password"

def test_password_normal():
    assert check_password("18819748") == "Normal password"

def test_password_strong():
    assert check_password("18819748161718") == "Good password"



def test_cart_initial_empty():
    cart = ShoppingCart("Nazarii")
    assert cart.get_count() == 0

def test_cart_add_item():
    cart = ShoppingCart("Nazarii")   
    cart.add_item("milk")

    assert cart.get_count() == 1

def test_cart_add_multiple():
    cart = ShoppingCart("Nazarii")

    cart.add_item("milk")
    cart.add_item("bread")
    cart.add_item("tomato")

    assert cart.get_count() == 3

def test_cart_remove_item():
    cart = ShoppingCart("Nazarii")

    cart.add_item("milk")
    cart.remove_item("milk")

    assert cart.get_count() == 0

def test_cart_remove_missing_item():
    cart = ShoppingCart("Nazarii")

    with pytest.raises(ValueError):
        cart.remove_item("milk")

def test_cart_clear():
    cart = ShoppingCart("Nazarii")

    cart.add_item("milk")
    cart.add_item("bread")
    cart.add_item("tomato")

    cart.clear()

    assert cart.get_count() == 0
    
    