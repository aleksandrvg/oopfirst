class User:
    _name: str
    _phone: str
    _bonus: str

    def __init__(self, name, phone, bonus):
        self._name = name
        self._phone = phone
        self._bonus = bonus

    def getName(self):
        return self._name

    def getPhone(self):
        return self._phone

    def getBonus(self):
        return self._bonus

