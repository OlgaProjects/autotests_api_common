import pytest
from clients.api_helpers import ApiHousehold
from configuration import Config



class RegionsHelp:
    @staticmethod
    def get_regions_dict(base_fixture):
        session_token = Config.token
        resp = base_fixture.api.regions.get_configs_regions(session_token)
        resp_dict = resp.json()
        return resp_dict