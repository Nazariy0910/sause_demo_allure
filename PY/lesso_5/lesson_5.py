# # # import helpers
# # from lesso_4.helpers import generate_test_email
# # email= generate_test_email()
# # print(email)  

# # number= int('hii')
# # print("sosooo")

# # from helpers import check_form

# # try:
# #     number= str('enter password')

# #     print(f"sosooo{check_form(password)}")

# # except ValueError:
# #     print("Ошибка: невозможно преобразовать строку в число.")

# try:
#     number= int('hii')
#     print("sosooo")
# except ValueError:
#     print("Ошибка: невозможно преобразовать строку в число.")


# try:
#     file= open("test.txt")
# except FileNotFoundError:
#     print("Ошибка: файл не найден.")


api_users =[
    {"name": "Alice", "45": "25"},       # Всё ОК
    {"name": "Bob", "age": "Двадцать"},   # Ошибка ValueError
    {"name": "Charlie"}                   # Ошибка KeyError (нет ключа age)
]


def chech_user(users_list):
    for user in users_list:
        try:
            age_user = int(user["age"])
            print(f"age name: {age_user}")
        except ValueError as e:
            print(f"Error in user: {e}")
        except KeyError as e:
                print(f"Error in user: {e}")

chech_user(api_users)