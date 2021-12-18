from configuration import Config


def test_positive(base_fixture):
    session_token = Config.token
    response = base_fixture.api.regions.get_configs_regions(session_token)
    resp_dict = response.json()
    status = Config.exp_status
    # print(resp_dict)
    # a = resp_dict['data']['items']['title']
    # print(a)

    # print(Config.base_path)
    # print(resp_dict)

    check_resp = base_fixture.checker.regions.check_regions_service(resp_dict, status)
    base_fixture.helper.print_all.request(response)

    assert response.status_code == 200
    assert check_resp is True, f'Поле name не соответствует ожидаемому {status}, ' \
                               f'ожидаемое - {resp_dict["data"]["items"]["title"]}'


def test_positive_validate(base_fixture):
    session_token = Config.token
    response = base_fixture.api.regions.get_configs_regions(session_token)
    resp_dict = response.json()
    a = base_fixture.checker.regions.validate_json(resp_dict, 'regions.json')
    assert a is True, f'Validation Failed'
