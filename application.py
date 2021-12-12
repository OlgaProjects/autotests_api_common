import pytest
from clients.api_helpers import ApiHousehold
from checkers.checkers_helper import Checkers
from helpers import RegionsHelp


class Application:
    def __init__(self):
        self.api = ApiHousehold()
        self.helper = RegionsHelp()
        self.checker = Checkers()
