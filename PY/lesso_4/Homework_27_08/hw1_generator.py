import random
import datetime

def generate_user():
    random_age= random.randint(18, 65)
    random_browser= random.choice(['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera'])
    random_data= datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f' User age: {random_age},\n Browser: {random_browser},\n Date: {random_data}')
    return random_age, random_browser, random_data

generate_user()