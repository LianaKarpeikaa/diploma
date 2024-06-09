import os

from src.enums.common import PetStatus


class TestAPIPet:

    def test_create_pet(self, api_pet, pet_data):
        response = api_pet.create_pet(pet_data)
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

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


    def test_update_existing_pet(self, api_pet, updated_pet_data):
        response = api_pet.update_pet(updated_pet_data)
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        assert response.status_code == 200

        response_json = response.json()

        assert 'id' in response_json
        assert 'category' in response_json
        assert 'name' in response_json
        assert 'photoUrls' in response_json
        assert 'tags' in response_json
        assert 'status' in response_json

        assert response_json['id'] == updated_pet_data['id']
        assert response_json['category']['id'] == updated_pet_data['category']['id']
        assert response_json['category']['name'] == updated_pet_data['category']['name']
        assert response_json['name'] == updated_pet_data['name']
        assert response_json['photoUrls'] == updated_pet_data['photoUrls']
        assert response_json['tags'][0]['id'] == updated_pet_data['tags'][0]['id']
        assert response_json['tags'][0]['name'] == updated_pet_data['tags'][0]['name']
        assert response_json['status'] == updated_pet_data['status']

    def test_upload_image(self, api_pet, pet_id, image_file):
        file_path = os.path.abspath(image_file)

        files = {'file': (os.path.basename(file_path), open(file_path, 'rb'), 'image/png')}

        response = api_pet.upload_image(pet_id, files)

        assert response.status_code == 200

        response_json = response.json()
        assert response_json['code'] == 200
        assert 'message' in response_json

    def test_find_pet_by_available_status(self, api_pet, pet_id):
        response_available = api_pet.get_pet_by_status(PetStatus.AVAILABLE)
        assert response_available.status_code == 200

    def test_find_pet_by_pending_status(self, api_pet, pet_id):
        response_pending = api_pet.get_pet_by_status(PetStatus.PENDING)
        assert response_pending.status_code == 200

    def test_find_pet_by_sold_status(self, api_pet, pet_id, update_params, updated_pet_data):
        response = api_pet.update_pet_by_id_(pet_id, params=update_params)
        assert response.status_code == 200

        updated_pet_response = api_pet.get_pet_by_id(pet_id)
        assert updated_pet_response.status_code == 200

        updated_pet_data = updated_pet_response.json()
        assert updated_pet_data['name'] == 'Mayyy'
        assert updated_pet_data['status'] == 'sold'

    def test_delete_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 200

    def test_delete_non_existing_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 404



