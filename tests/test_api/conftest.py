import pytest
from src.api.api_pet import APIPet


@pytest.fixture(scope="session")
def api_pet():
    return APIPet()


@pytest.fixture
def pet_id():
    return 12


@pytest.fixture
def pet_data():
    pet_data = {
        "id": 12,
        "category": {
            "id": 0,
            "name": "category 1"
        },
        "name": "May",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "tags"
            }
        ],
        "status": "available"
    }
    return pet_data


@pytest.fixture
def updated_pet_data():
    updated_pet_data = {
        "id": 12,
        "category": {
            "id": 0,
            "name": "category 2"
        },
        "name": "May Edited",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "tags"
            }
        ],
        "status": "available"
    }
    return updated_pet_data


@pytest.fixture(scope="session")
def image_file():
    return "C:/Users/ulyan/Desktop/Images/Cats/2023-03-29_14h59_04.png"


@pytest.fixture
def update_params():
    return {'name': 'Mayyy', 'status': 'sold'}