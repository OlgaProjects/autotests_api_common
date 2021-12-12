import pytest
from clients.api_helpers import ApiHousehold
from checkers.checkers_helper import Checkers
from helpers.regions_helper import RegHelp


class Application:
    def __init__(self):
        self.api = ApiHousehold()
        self.helper = RegHelp()
        self.checker = Checkers()
