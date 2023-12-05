from classLibrary import Manager, Smena, User, Pay, Coffee, Additional
from dto import ManagerDTO, CoffeDTO, AdditionalDTO, PayDTO, SmenaDTO, UserDTO

def LoginManager(login, password):
    valManager = ManagerDTO.GetManagerByLoginAndPassword(login, password)
    if valManager.login == login and valManager.password == password:
        return valManager
    else:
        return None

_mainMenu: str
_buyMenu: ""
_smenaMenu: str

while True:
    password = input("Введите пароль от кассы: ")
    if password == "qwerty":
        login = input("Введите логин: ")
        passwordManager = input("Введите пароль: ")
        manager = LoginManager(login, passwordManager)
        if manager is None:
            break
        _mainMenu = f"{manager.name}\n 1 - Открыть смену "
        choice = input(_mainMenu)
        if choice == "1":
            smena = SmenaDTO.CreateSmena(manager)
            payList = []
            while True:
                _mainMenu = f"{manager.name}\n 1 - Закрыть смену \n 2 - Покупка "
                choice = input(_mainMenu)
                if choice == "2":
                    while True:
                        cofees = CoffeDTO.GetAllCoffe()
                        _buyMenu = ""
                        for coffe in cofees:
                            _buyMenu += f"{coffe.id} {coffe.type} {coffe.price}\n"
                        _buyMenu += "6 - выход "
                        choice = input(_buyMenu)
                        additional = None
                        if choice != "6":
                            coffe = CoffeDTO.GetCoffeById(int(choice))
                            _buyMenu = ""
                            additionals = AdditionalDTO.GetAllAdditional()
                            for additional in additionals:
                                _buyMenu = f"{additional.id} {additional.size} {additional.type}\n"
                            _buyMenu += "6 - выход "
                            choice = input(_buyMenu)
                            if choice != "6":
                                additional = AdditionalDTO.GetAdditionalById(int(choice))
                            else:
                                pass
                        elif choice == "6":
                            break
                        else:
                            continue
                        phone = input("Введите номер телефона пользователя: ")
                        user = UserDTO.GetUserByPhone(phone)
                        pay = Pay.Pay(eMoney=True, client=User.User(bonus=100, name="Andrey", phone=""),
                                    additionals=additionals, coffees=coffe)
                        payList.append(pay)
                elif choice == "1":
                    summ = 0
                    for payItem in payList:
                        summ += payItem.coffe.price()
                        if not payItem.additionals is None:
                            summ += payItem.additionals.price()
                    smena.sum(summ)
                    SmenaDTO.CreateSmena(smena, summ)
                    break
        break
    else:
        continue
