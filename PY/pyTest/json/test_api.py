import json
import pytest

@pytest.fixture
def user_data():
    with open('user_data.json', 'r') as f:
        return json.load(f)

def test_user_is_active(user_data):

    assert user_data['status'] == 'active'

def test_user_has_enough_balance(user_data): 

    assert user_data['balance'] > 1000

def test_user_has_roles(user_data):   

    assert 'reviewer' in user_data['roles']

bad_response = '{"name": "Alex", "age":25'

try:
    data = json.loads(bad_response)
except json.JSONDecodeError as e:
    print(f'сервер лопнув{e}')

