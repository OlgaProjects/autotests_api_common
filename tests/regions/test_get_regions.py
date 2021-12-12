import pytest
from configuration import Config
from helpers import RegionsHelp


def test_positive(base_fixture):
    session_token = base_fixture.configs.token
    response = base_fixture.api.regions.get_configs_regions(session_token)

    check_resp = base_fixture.checker.regions.check_regions_service(RegionsHelp.get_regions_dict, Config.exp_status)

    assert response.status_code == 200
    assert check_resp is True, f'Поле name не соответствует ожидаемому {Config.exp_status}, ожидаемое - {RegionsHelp.get_regions_dict["service"]}'