class Additional:
    _type: str
    _size: str
    _price: float

    def __init__(self, type, size, price):
        self._type = type
        self._size = size
        self._price = price

    def getType(self):
        return self._type

    def getSize(self):
        return self._size

    def getPrice(self):
        return self._price

