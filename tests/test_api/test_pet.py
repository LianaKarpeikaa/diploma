import requests
import json
import allure
from src.models.pet_model import PetModel, Category, Tag


class TestAPIPet:

    def test_create_pet(self, api_pet, pet_data):
        response = api_pet.create_pet(pet_data)

        assert response.status_code == 200

        assert 'id' in response.json()
        assert 'category' in response.json()
        assert 'name' in response.json()
        assert 'photoUrls' in response.json()
        assert 'tags' in response.json()
        assert 'status' in response.json()

    def test_get_pet_by_id(self, api_pet, pet_id):
        response = api_pet.get_pet_by_id(pet_id)
        assert response.status_code == 200

    def test_delete_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 200

    def test_delete_non_existing_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 404


