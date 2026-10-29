from helpers import is_valid_email
from helpers import is_valid_phone

test_data = [
 {"email": "user@test.com", "phone": "123456789", "age":
"25"},
 {"email": "notanemail", "phone": "987654321", "age":
"30"},
 {"email": "qa@course.cz", "phone": "12345", "age":
"двадцать"},
 {"email": "admin@test.com", "phone": "555555555", "age":
"-5"},
 {"email": "dev@shop.cz", "phone": "777777777", "age":
"42"},
]
for i, user in enumerate(test_data, 1):
    print(f"\n--- Проверка записи #{i}: {user['email']} ---")
    if is_valid_email(user["email"]):
        print("Email correct")
    else:
        print("Email not correct")

    if is_valid_phone(user["phone"]):
        print("Phone correct")
    else:
        print("Phone not correct")

    try:
        age = int(user['age'])
        if 18 <= age <= 99:
            print('Age is correct')
        else:
            print('Age is not correct')
    except ValueError:
        print('PROOOOOblem')