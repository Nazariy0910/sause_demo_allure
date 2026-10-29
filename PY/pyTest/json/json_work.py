import json

# bad_response = '{"name": "Alex", "age":25}'

# try:
#     data = json.loads(bad_response)
# except json.JSONDecodeError as e:
#     print(f'сервер лопнув {e}')

response = """[
    {"product": "iPhone",  "available": true},
    {"product": "Samsung", "available": false},
    {"product": "Pixel",   "available": true}
]"""

products = json.loads(response)
print(type(response))

for product in products:
    if product['available']:
        print(f'in stock: {product["product"]}')
    else:
        print(f'not in stock: {product["product"]}')