import requests
import copy
from configuration import Config


class ApiUsers:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def get_users(self, token):
        api_method = Config.api_method_users
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response