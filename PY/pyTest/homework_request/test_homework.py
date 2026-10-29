import pytest
import requests
#1
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

#2
def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()  
    assert "title" in data
    assert data["userId"] == 1

def test_get_all_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10
    assert "email" in data[0]

def test_get_nonexistent_post(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404
#3
def test_save_user_to_file(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    data = response.json()

#4
def test_response_headers(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200

    content_type = response.headers["Content-Type"]
    assert "application/json" in content_type

    print(response.headers)