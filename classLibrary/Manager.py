from classLibrary.User import User
from classLibrary.BaseModel import BaseModel
from peewee import *

class Manager(User, BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    login = CharField(column_name="login", max_length=29)
    password = CharField(column_name="password", max_length=29)
    class Meta:
        table_name = "manager"

    # def __init__(self, login, password, name, phone, bonus):
    #     super().__init__(name, phone, bonus)
    #     self._login = login
    #     self._password = password
    #
    # def getLogin(self):
    #     return self._login
    #
    # def getPassword(self):
    #     return self._password

