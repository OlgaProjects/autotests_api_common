from checkers.regions_check import CheckerRegions
from checkers.users_check import Users

class Checkers:
    def __init__(self):
        self.regions = CheckerRegions()
        self.users = Users()