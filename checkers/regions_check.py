import pytest
from configuration import Config



class CheckerRegions:
    @staticmethod
    def check_regions_service(resp_dict, exp_status):
        exp_status = Config.exp_status

        for item in resp_dict:
            if item['service'] != exp_status:
                return False
        return True