import json


class Flatramms:
    @staticmethod
    def check_room_type_flatgramms(resp_dict, exp_status):
        if resp_dict['data']['items']['room_types'][0]['type'] != exp_status:
            return False
        return True