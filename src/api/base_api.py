import logging
import requests

logger = logging.getLogger(__name__)


class BaseApi:
    default_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    base_url = 'https://petstore.swagger.io/v2'

    def get(self, path: str, headers: dict = None, params: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        logger.info(f"GET URL = {self.base_url}{path}")
        logger.info(f"GET Headers = {self.default_headers}")
        return requests.get(url=f"{self.base_url}{path}", headers=self.default_headers, params=params)

    def post(self, path: str, json_data: dict, headers: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        logger.info(f"POST URL = {self.base_url}{path}")
        logger.info(f"POST Headers = {self.default_headers}")
        logger.info(f"POST JSON Data = {json_data}")
        return requests.post(url=f"{self.base_url}{path}", json=json_data, headers=self.default_headers)

    def delete(self, path: str, headers: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        logger.info(f"DELETE URL = {self.base_url}{path}")
        logger.info(f"DELETE Headers = {self.default_headers}")
        return requests.delete(url=f"{self.base_url}{path}", headers=self.default_headers)