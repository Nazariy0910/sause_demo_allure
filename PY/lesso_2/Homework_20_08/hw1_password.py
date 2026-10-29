password = input("Enter your password: ")
lenght = len(password)
if lenght < 8:
    print("❌ The password is too short. It must be at least 8 characters long.")
elif lenght <= 12:
    print("✅ The password is valid. It meets the length requirements.")
else:
    print("✅ The password is strong.")

print(f"Password length: {lenght} characters.")