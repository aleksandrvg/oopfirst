from classLibrary.User import User

def GetUserByPhone(phone:str):
    user = User.select().where(User.phone == phone).get()
    return user

def RegistrationUser():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    user = User(name=name, phone=phone, bonus=0)
    user.save()
