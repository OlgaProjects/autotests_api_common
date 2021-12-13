from configuration import Config


def test_users_positive(base_fixture):
    session_token = Config.token
    response = base_fixture.api.users.get_users(session_token)
    resp_dict = response.json()
    status = Config.exp_status_type
    print(resp_dict)
    a = resp_dict['data']['items'][0]['type']
    print(a)

    # print(Config.base_path)
    # print(resp_dict)

    check_resp = base_fixture.checker.users.check_users_type(resp_dict, status)

    assert response.status_code == 200
    assert check_resp is True, f'Поле name не соответствует ожидаемому {status}, ' \
                               f'ожидаемое - {resp_dict["data"]["items"][0]["type"]}'


def test_users_positive_validate(base_fixture):
    session_token = Config.token
    response = base_fixture.api.users.get_users(session_token)
    resp_dict = response.json()
    b = base_fixture.checker.regions.validate_json(resp_dict, 'users.json')
    assert b is True, f'Validation Failed'