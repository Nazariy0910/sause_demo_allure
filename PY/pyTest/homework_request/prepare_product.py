# import json
# import random

# with open("template.json", "r", encoding="utf-8") as f:
#         product = json.load(f)

# new_price = random.randint(10000, 50000)
# product["price"] = new_price

# with open('product_ready.json', 'w') as f:
#     json.dump(product, f, indent=4)

# print(f'Complete! Price product: {new_price}')

import json
import random

# 1. Читаємо template.json через json.load
with open("template.json", "r", encoding="utf-8") as f:
    product = json.load(f)

# 2. Змінюємо ціну на випадкове число від 10000 до 50000
new_price = random.randint(10000, 50000)
product["price"] = new_price

# 3. Зберігаємо результат у product_ready.json з indent=4
with open("product_ready.json", "w", encoding="utf-8") as f:
    json.dump(product, f, indent=4)

# 4. Друкуємо повідомлення про успіх
print(f"Готово! Цена товара: {new_price}")