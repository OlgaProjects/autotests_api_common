from clients.regions import ApiRegions
from clients.users import ApiUsers
from clients.devices import ApiDevices


class ApiHousehold:
    def __init__(self):
        self.regions = ApiRegions()
        self.users = ApiUsers()
        self.devices = ApiDevices()
