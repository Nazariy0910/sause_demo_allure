# import time
# # import random

# # # print('хххххх')
# # # time.sleep(3)
# # # print('XXXXXXXX')

# # random_age= random.randint(18,60)
# # print(random_age)


# # def login_to_site():
# #     print('open browser')
# #     print('enter login and pasword')
# #     print('hjjh')

# # def print_separetor():
# #     print('='*30)
# #     print('new test-cases')
# #     print('='*30)

# # print_separetor
# # print('testing bucket')
# # print_separetor
# # print('testing chec')


# def generate_test_email():
#     unique_number= int(time.time())
#     print(f'test_user{unique_number}@qa-courses.cz')

# generate_test_email()

# def create_link(path, domain= 'https://qa-courses.com'):
#     return f'{domain}/{path}'

# def create_link2(path):
#     domain= 'https://qa-courses.com'
#     return f'{domain}/{path}'

# def create_link3(path, domain):
#     return f'{domain}/{path}'



# print(create_link('test'))
# print(create_link2('test'))
# print(create_link3('api', ))


def log_message(action, status):
    print(f'[QA-Courses] акція {action} | сатус {status.upper()}')

log_message('Клик по кнопке Купить', 'success')
log_message('Поиск товара', 'failed')
