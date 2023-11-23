import datetime
from classLibrary.User import User
from classLibrary.Coffee import Coffee
from classLibrary.Additional import Additional

class Pay:
    _date: datetime.date
    _eMoney: bool
    _client: User
    _sum = 0.0
    _coffees: list[Coffee]
    _additionals: list[Additional]

    def __init__(self, eMoney, client, coffees = None, additionals = None):
        if additionals is None:
            additionals = []
        if coffees is None:
            coffees = []
        self._eMoney = eMoney
        self._client = client
        self._coffees = coffees
        self._date = datetime.datetime.now().date()
        self._additionals = additionals
        if len(coffees) != 0:
            for coffee in coffees:
                self._sum += coffee.getPrice()
        if len(additionals) != 0:
            for additional in additionals:
                self._sum += additional.getPrice()

    def getSum(self):
        return self._sum

