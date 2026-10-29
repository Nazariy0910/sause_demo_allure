def is_valid_email(email):
    return  "@" in email and '.' in email    

def is_valid_password(password):
    return len(password) >=8

def is_valid_age(age):
    return 18 <= age <= 99

def check_form(email, password, age):
    email_ok= is_valid_email(email)
    pass_ok= is_valid_password(password)
    age_ok= is_valid_age(age)

    print(f"Email: {email_ok}")
    print(f"Password: {pass_ok}")
    print(f"Age: {age_ok}")

    return email_ok and pass_ok and age_ok

print("--- Test 1: All correct ---")
result1 = check_form("test@mail.com", "supersecret123", 25)
print(f"Form is valid: {result1}\n")

print("--- Test 2: Email without @ ---")
result2 = check_form("testmail.com", "supersecret123", 25)
print(f"Form is valid: {result2}\n")

print("--- Test 3: Short password and young age ---")
result3 = check_form("test@mail.com", "12345", 15)
print(f"Form is valid: {result3}\n")