
class Location():

    _sequence = 0
    _vnum = 0

    def __init__(self, name):
        self.vnum = self._sequence
        Location.sequence += 1
        self.name = name

    def get_num(self):
        return self._vnum

    def get_name(self):
        return self.name

