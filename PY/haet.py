# import random
# from datetime import date

# def generate_product():
#     random_cina= round(random.uniform(10, 50), 2)
#     random_spisok= random.choice(["Electronics", "Clothing", "Books", "Home"])
#     random_day= date.today().strftime("%d-%m-%Y")
#     print(f' Product price: {random_cina},\n Category: {random_spisok},\n Date: {random_day}')
#     return random_cina, random_spisok, random_day

# generate_product()


# def calculate_shipping(weight, destination='local'):
#     if weight <= 0:
#         return "Invalid weight"
    
#     if destination == 'local':
#         return weight * 5
#     elif destination == 'international':
#         return weight * 15
#     else:       
#         return weight * 10

# res1 = calculate_shipping(3)
# print(f"Тест 1 (вага 3): {res1}")

# # Тест 2: Доставка за замовчуванням (destination не вказуємо, спрацює "local")
# res2 = calculate_shipping(5)
# print(f"Тест 2 (вага 5, local): {res2}")

# # Тест 3: Міжнародна доставка (перевизначаємо destination)
# res3 = calculate_shipping(5, "local")
# print(f"Тест 3 (вага 3, international): {res3}")

# # Тест 4: Інша країна (наприклад, "Europe")
# res4 = calculate_shipping(5, "local")
# print(f"Тест 4 (вага 3, Albania): {res4}")
    
# Функція, яку ми тестуємо
def calculate_shipping(weight, destination="local"):
    if weight <= 0:
        return "Ошибка: вес должен быть больше 0"
    if destination == "local":
        return weight * 5
    return weight * 15

# Автотести
def test_shipping_local_success():
    result = calculate_shipping(2, "local")
    assert result == 10, f"Очікували 10, але отримали {result}"

def test_shipping_invalid_weight():
    result = calculate_shipping(0)
    assert result == "Ошибка: вес должен быть больше 0"

# Запуск тестів
test_shipping_local_success()
test_shipping_invalid_weight()
print("✅ Всі тести успішно пройдені!")