import pytest
from clients.api_helpers import ApiHousehold
from configuration import Config

class RegionsHelp:
    @staticmethod
    def get_regions_dict(base_fixture):
        session_token = base_fixture.configs.token
        resp_dict = ApiHousehold().regions.get_configs_regions(session_token)
        return resp_dict