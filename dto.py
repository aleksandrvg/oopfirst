from classLibrary.User import User
from classLibrary.Additional import Additional
from classLibrary.Pay import Pay

def FillUser():
    user = User(name="Oleg", phone="+79226434755", bonus=0)
    user.save()

def SelectUser():
    users = User.select()
    print(users)
    for user in users:
        print(user.id, user.name, user.phone, user.bonus)

def ChangeUserByPhone(phone:str):
    user = User.select().where(User.phone == phone).get()
    user.name = "Вадим"
    user.save()

def CreateAdditional():
    additional = Additional(size="XL", type="Сироп", price=30.0)
    additional.save()
    additional1 = Additional(size="L", type="Сироп", price=20.0)
    additional1.save()
    additional2 = Additional(size="M", type="Сироп", price=10.0)
    additional2.save()

def CreatePay(user:User,additional:Additional):
    import datetime
    date = datetime.date
    pay = Pay(date='2022-09-11', additionals=additional, client=user, eMoney=False, sum=additional.price)
    pay.save()

def SelectPay(id:int):
    pay = Pay.select().where(Pay.id == id).get()
    print(pay.additionals.type, pay.sum)

if __name__ == "__main__":
    pass
    # SelectPay(1)
    # user = User.select().where(User.phone == "+79226434755").get()
    # additional = Additional.select().where((Additional.type == "Сироп") & (Additional.size == "L")).get()
    # CreatePay(user, additional)
    # CreateAdditional()
    # SelectUser()
    # ChangeUserByPhone('+79226434755')
    # SelectUser()

