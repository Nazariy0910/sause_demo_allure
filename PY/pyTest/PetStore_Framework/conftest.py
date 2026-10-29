# conftest.py

import pytest
from API.api_client import PetstoreAPI

@pytest.fixture
def api():
    return PetstoreAPI()

@pytest.fixture
def test_pet_data():
    return {
        "id": 999111,
        "name": "QA_Step",
        "status": "available"
    }