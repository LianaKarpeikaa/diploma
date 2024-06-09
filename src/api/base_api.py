import logging
import requests

logger = logging.getLogger(__name__)


class BaseApi:
    def __init__(self):
        self.default_headers = {'accept': 'application/json'}
        self.base_url = 'https://petstore.swagger.io/v2'
        self.entity_path = self.__class__.PATH if hasattr(self.__class__, "PATH") else ""

    def get(self, path: str, headers: dict = None, params: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        url = f"{self.base_url}{self.entity_path}{path}"
        logger.info(f"GET URL = {url}")
        logger.info(f"GET Headers = {self.default_headers}")
        return requests.get(url=url, headers=self.default_headers, params=params)

    def post(self, path: str, json_data: dict = None, headers: dict = None, files: dict = None, params: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        url = f"{self.base_url}{self.entity_path}{path}"
        logger.info(f"POST URL = {url}")
        logger.info(f"POST Headers = {self.default_headers}")
        logger.info(f"POST JSON Data = {json_data}")
        logger.info(f"POST Files = {files}")
        return requests.post(url=url, json=json_data, headers=self.default_headers, files=files, params=params)

    def delete(self, path: str, headers: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        url = f"{self.base_url}{self.entity_path}{path}"
        logger.info(f"DELETE URL = {url}")
        logger.info(f"DELETE Headers = {self.default_headers}")
        return requests.delete(url=url, headers=self.default_headers)

    def put(self, path: str, json_data: dict, headers: dict = None):
        if headers is not None:
            self.default_headers.update(headers)
        url = f"{self.base_url}{self.entity_path}{path}"
        logger.info(f"PUT URL = {url}")
        logger.info(f"PUT Headers = {self.default_headers}")
        logger.info(f"PUT JSON Data = {json_data}")
        return requests.put(url=url, json=json_data, headers=self.default_headers)
