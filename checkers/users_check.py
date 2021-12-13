import json


class Users:
    @staticmethod
    def check_users_type(resp_dict, exp_status):
        if resp_dict['data']['items'][0]['type'] != exp_status:
            return False
        return True