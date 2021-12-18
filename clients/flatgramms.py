import requests
import copy
from configuration import Config


class ApiFlatgramms:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def get_flatgramms(self, token):
        api_method = Config.api_method_flatgramms
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token


        response = requests.get(url, headers=headers)
        return response