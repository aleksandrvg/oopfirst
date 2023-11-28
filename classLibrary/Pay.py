import datetime
from classLibrary.User import User
from classLibrary.Coffee import Coffee
from classLibrary.Additional import Additional
from classLibrary.BaseModel import BaseModel
from peewee import *

class Pay(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    date = DateField(column_name="date")
    eMoney = BooleanField(column_name="e_money")
    client = ForeignKeyField(User, related_name="pay_user_client_id", to_field="id")
    sum = FloatField(column_name="sum")
    additionals = ForeignKeyField(Additional, related_name="pay_additional_additional_id", to_field="id")
    class Meta:
        table_name = "pay"

    # type = CharField(column_name="type", max_length=100)
    # size = CharField(column_name="size", max_length=2)
    # price = FloatField(column_name="price", null=False)
    # _date: datetime.date
    # _eMoney: bool
    # _client: User
    # _sum = 0.0
    # _coffees: list[Coffee]
    # _additionals: list[Additional]
    #
    # def __init__(self, eMoney, client, coffees = None, additionals = None):
    #     if additionals is None:
    #         additionals = []
    #     if coffees is None:
    #         coffees = []
    #     self._eMoney = eMoney
    #     self._client = client
    #     self._coffees = coffees
    #     self._date = datetime.datetime.now().date()
    #     self._additionals = additionals
    #     if len(coffees) != 0:
    #         for coffee in coffees:
    #             self._sum += coffee.getPrice()
    #     if len(additionals) != 0:
    #         for additional in additionals:
    #             self._sum += additional.getPrice()
    #
    # def getSum(self):
    #     return self._sum

