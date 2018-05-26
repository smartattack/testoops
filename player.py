import random
import mud

class Player():
    _age = None  # type: int
    _name = None  # type: string
    _mud = None  # type: object

    def __init__(self, name):
        self._name = name
        self._age = random.random() * 10 + 18

    def get_name(self):
        assert isinstance(self._name, string)
        return self._name

    def get_age(self):
        assert isinstance(self._age, int)
        return self._age

