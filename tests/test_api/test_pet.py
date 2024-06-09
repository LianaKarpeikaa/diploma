
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

    def test_delete_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 200

    def test_delete_non_existing_pet_by_id(self, api_pet, pet_id):
        response = api_pet.delete_pet_by_id(pet_id)
        assert response.status_code == 404

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




