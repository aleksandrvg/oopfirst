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

    # def __init__(self, manager):
    #     self._date = datetime.datetime.now().date()
    #     self._timeOpen = datetime.datetime.now().time()
    #     self._manager = manager
    #
    # def getDate(self):
    #     return self._date
    #
    # def getTimeOpen(self):
    #     return self._timeOpen
    #
    # def getManager(self):
    #     return self._manager
    #
    # def getTimeClose(self):
    #     return self._timeClose
    #
    # def setTimeClose(self):
    #     self._timeClose = datetime.datetime.now().time()
    #
    # def getSum(self):
    #     return self._sum
    #
    # def setSum(self, sum):
    #     self._sum = sum

