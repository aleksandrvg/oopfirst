from classLibrary.Manager import Manager
from classLibrary.BaseModel import BaseModel
from peewee import *
import datetime

class Smena(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    date = DateField(column_name="date")
    timeOpen = TimeField(column_name="timeOpen")
    timeClose = TimeField(column_name="timeClose")
    sum = FloatField(column_name="sum")
    manager = ForeignKeyField(Manager, related_name="smena_manager_manager_id", to_field="id")
    class Meta:
        table_name = "smena"

