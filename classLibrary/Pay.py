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
    coffe = ForeignKeyField(Coffee, related_name="pay_coffe_coffe_id", to_field="id")
    class Meta:
        table_name = "pay"

