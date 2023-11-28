from classLibrary.BaseModel import BaseModel
from peewee import *

class User(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    name = CharField(column_name="name", max_length=120)
    phone = CharField(column_name="phone", max_length=15)
    bonus = IntegerField(column_name="bonus")
    class Meta:
        table_name = "user"

    # _name: str
    # _phone: str
    # _bonus: str
    #
    # def __init__(self, name, phone, bonus):
    #     self._name = name
    #     self._phone = phone
    #     self._bonus = bonus
    #
    # def getName(self):
    #     return self._name
    #
    # def getPhone(self):
    #     return self._phone
    #
    # def getBonus(self):
    #     return self._bonus

