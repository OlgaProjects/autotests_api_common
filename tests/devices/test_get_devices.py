import pytest
from configuration import Config


@pytest.mark.parametrize("limit", ['1', '3', '5'])
def test_get_devices_positive(base_fixture, limit):
    response = base_fixture.api.devices.get_devices(limit)
    resp_dict = response.json()
    print(resp_dict)
    base_fixture.helper.print_all.request(response)

    assert response.status_code == 200, "Код ответа не соответствует ожидаемому."


def test_devices_positive_validate(base_fixture):
    response = base_fixture.api.devices.get_devices('1')
    resp_dict = response.json()
    b = base_fixture.checker.regions.validate_json(resp_dict, 'devices.json')
    assert b is True, f'Validation Failed'

def test_get_devices_positive_validate_items(base_fixture):

    response = base_fixture.api.devices.get_devices('3')
    resp_dict = response.json()

    base_fixture.checker.regions.validate_json(resp_dict['data']['items'], 'devices_3.json')



