import requests
from src.api.base_api import BaseApi
from src.models.pet_model import PetModel, PetResponse


class APIPet(BaseApi):

    def get_pet_by_id(self, pet_id: int):
        return self.get(path=f"/pet/{pet_id}")

    def create_pet(self, pet_data: dict):
        return self.post(path="/pet", json_data=pet_data)

    def delete_pet_by_id(self, pet_id: int):
        return self.delete(path=f"/pet/{pet_id}")

