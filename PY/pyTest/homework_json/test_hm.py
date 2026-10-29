from PY.pyTest.homework_json.confitest_rename import two_users, products
import json
# First task
def test_admin_is_logged_in(two_users):
    admin, guest = two_users
    assert admin.is_logged_in == True


def test_guest_is_not_logged_in(two_users):
    admin, guest = two_users
    assert guest.is_logged_in == False


def test_users_have_different_names(two_users):
    admin, guest = two_users
    assert admin.username != guest.username

# Second task
def test_total_products(products):
    assert len(products) == 4


def test_first_product_name(products):
    assert products[0]["name"] == "Ноутбук"


def test_monitor_not_in_stock(products):
    monitor = [product for product in products if product["id"] == 3][0]
    assert monitor["in_stock"] is False


def test_all_prices_positive(products):
    for product in products:
        assert product["price"] > 0


def test_in_stock_count(products):
    in_stock_items = [product for product in products if product["in_stock"] is True]
    assert len(in_stock_items) == 3

# Third task
def test_save_and_reload_results():
    results = {
        "suite": "Smoke Test",
        "passed": 4,
        "failed": 1,
        "success": False,
    }

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    with open("results.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded["suite"] == "Smoke Test"
    assert loaded["passed"] == 4
    assert loaded["success"] is False