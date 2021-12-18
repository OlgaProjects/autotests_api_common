from configuration import Config


def test_positive_get_flatgramms(base_fixture):
    session_token = Config.token
    response = base_fixture.api.flatgramms.get_flatgramms(session_token)
    resp_dict = response.json()
    status = Config.exp_status_room_type
    print(resp_dict)
    a = resp_dict["data"]["items"]["room_types"][0]["type"]
    print(a)

    # print(Config.base_path)
    # print(resp_dict)

    check_resp = base_fixture.checker.flatgramms.check_room_type_flatgramms(resp_dict, status)
    base_fixture.helper.print_all.request(response)

    assert response.status_code == 200
    assert check_resp is True, f'Поле name не соответствует ожидаемому {status}, ' \
                               f'ожидаемое - {resp_dict["data"]["items"]["room_types"][0]["type"] }'