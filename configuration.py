import pathlib



class Config:
    url = ""
    api_method_users = "/api/v3/users?limit=1"
    api_method_devices = '/api/v4/devices?limit='
    exp_status = "Российская Федерация"
    exp_status_type = 'master'
    api_method_regions = "/api/v4/configs/regions"
    # base_path_1 = Path(pathlib.Path.cwd(), "schemas", "regions.json")
    base_path = 'C:/Users/user/PycharmProjects/autotests_api_common/schemas/'

    token = ""
