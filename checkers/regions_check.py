import pytest
from configuration import Config
import jsonschema
import json


class CheckerRegions:
    @staticmethod
    def check_regions_service(resp_dict, exp_status):
        if resp_dict['data']['items']['title'] != exp_status:
            return False
        return True

    @staticmethod
    def validate_json(item, schema_name):
        path = Config.base_path + schema_name
        with open(path) as file:
            schema = json.load(file)

        jsonschema.validate(item, schema)
        return True
