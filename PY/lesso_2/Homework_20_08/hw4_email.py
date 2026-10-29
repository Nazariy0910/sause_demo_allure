email= input('Enter email: ')
email = email.lower()
lenght= len(email)
if "@" in email and lenght > 5:
    print(f'Email look correct:{email}')
else:
    print('nononono')