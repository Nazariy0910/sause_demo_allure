import requests

print('open request in server')
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(f'status code: {response.status_code}')

user = response.json()

print(f'First name:{user["name"]}')
print(f'Email:{user["email"]}')
print(f'City:{user["address"]["city"]}')