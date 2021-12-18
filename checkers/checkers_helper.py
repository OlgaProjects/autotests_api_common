from checkers.regions_check import CheckerRegions
from checkers.users_check import Users
from checkers.flatgramms_check import Flatramms
from checkers.validate_items import ValidateItems

class Checkers:
    def __init__(self):
        self.regions = CheckerRegions()
        self.users = Users()
        self.flatgramms = Flatramms()
        self.validate_items = ValidateItems()