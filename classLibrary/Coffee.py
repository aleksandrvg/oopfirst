class Coffee:
    _name: str
    _size: str
    _price: float

    def __init__(self, name, size, price):
        self._name = name
        self._size = size
        self._price = price

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def getPrice(self):
        return self._price

