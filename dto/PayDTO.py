from classLibrary.Pay import Pay
from classLibrary.User import User
from classLibrary.Additional import Additional
from classLibrary.Coffee import Coffee
import datetime

def CreatePay(user:User,additional:Additional,coffe:Coffee):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    summ = additional.price + coffe.price
    user.bonus += summ * 0.1
    pay = Pay(date=date, additionals=additional, client=user, eMoney=False, sum=summ)
    user.save()
    pay.save()
    return pay
