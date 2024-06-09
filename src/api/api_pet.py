import requests
from src.api.base_api import BaseApi
from src.enums.common import PetStatus
from src.models.pet_model import PetModel, PetResponse


class APIPet(BaseApi):
    PATH = "/pet"

    def get_pet_by_id(self, pet_id: int):
        return self.get(path=f"/{pet_id}")

    def create_pet(self, pet_data: dict):
        headers = {'Content-Type': 'application/json'}
        return self.post(path="/", json_data=pet_data)

    def delete_pet_by_id(self, pet_id: int):
        return self.delete(path=f"/{pet_id}")

    def update_pet(self, pet_data: dict):
        headers = {'Content-Type': 'application/json'}
        return self.put(path=f"/", json_data=pet_data)

    def upload_image(self, pet_id: int, files: dict):
        headers = {'Content-Type': 'multipart/form-data'}
        return self.post(path=f"/{pet_id}/uploadImage", files=files)

    def get_pet_by_status(self, status: PetStatus):
        params = {'status': status.value}
        return self.get(path="/findByStatus", params=params)

    def update_pet_by_id_(self, pet_id, params: dict):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return self.post(path=f"/{pet_id}", headers=headers, params=params)
