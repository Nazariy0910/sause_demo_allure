import json
import random

with open('template.json', 'r') as f:
    user_data = json.load(f)

print(user_data)

random_num = random.randint(1000, 9999)
user_data['email'] = f'test_{random_num}@gmail.com'

with open('new_user.json', 'w') as f:
    json.dump(user_data, f, indent=4)