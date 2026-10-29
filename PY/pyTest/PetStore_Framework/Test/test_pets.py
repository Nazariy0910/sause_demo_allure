
from API.api_client import PetstoreAPI

def test_create_pet(api, test_pet_data):
    response = api.create_pet(test_pet_data)

    assert response.status_code == 200
    assert response.json["name"] == "beka"

def test_update_pet_status(api, test_pet_data):
    test_pet_data["status"] = "sold"

    response = api.update_pet(test_pet_data)

    assert response.status_code == 200
    assert response.json["name"] == "sold"

def test_get_non_existend_pet(api):
    response = api.get_pet(0)

    assert response.status_code == 404
