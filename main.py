from classLibrary import Manager, Smena, User, Pay, Coffee, Additional

def OpenSmena(manager:Manager.Manager):
    return Smena.Smena(manager)

def LoginManager(login, password):
    valLogin = "123"
    valPassword = "123"
    name = "Alexey"
    phone = "89123644673"
    bonus = 100
    if valLogin == login and valPassword == password:
        manager = Manager.Manager(login, password, name, phone, bonus)
        return manager
    else:
        return None

_mainMenu: str
_buyMenu: str
_smenaMenu: str

while True:
    password = input("Введите пароль от кассы: ")
    if password == "qwerty":
        login = input("Введите логин: ")
        passwordManager = input("Введите пароль: ")
        manager = LoginManager(login, passwordManager)
        if manager is None:
            break
        _mainMenu = f"{manager.getName()}\n 1 - Открыть смену "
        choice = input(_mainMenu)
        if choice == "1":
            smena = OpenSmena(manager)
            payList = []
            while True:
                _mainMenu = f"{manager.getName()}\n 1 - Закрыть смену \n 2 - Покупка "
                choice = input(_mainMenu)
                if choice == "2":
                    additionals = []
                    coffees = []
                    while True:
                        _buyMenu = (f" 1 - Латте {' ' * 12} 4 - Oreo \n 2 - Капучино {' ' * 9} 5 - Пончик"
                                    f" {' ' * 12} \n 3 - Американо {' ' * 12} \n 6 - Выход ")
                        choice = input(_buyMenu)
                        if choice in ['1', '2', '3']:
                            size = input("Выберите размер M, L, XL ")
                            if size in ['M', 'L', 'XL']:
                                if choice == "1":
                                    name = "Латте"
                                    coffeePrice = 160
                                elif choice == "2":
                                    name = "Капучино"
                                    coffeePrice = 140
                                elif choice == "3":
                                    name = "Американо"
                                    coffeePrice = 100
                                _buyMenu = f"1 - Сироп, 2 - Сливки, 3 - без добавок "
                                choice = input(_buyMenu)
                                if choice == "1":
                                    type = "Сироп"
                                    price = 40
                                    additionals.append(Additional.Additional(type, size, price))
                                elif choice == "2":
                                    type = "Сливки"
                                    price = 60
                                    additionals.append(Additional.Additional(type, size, price))
                                coffees.append(Coffee.Coffee(name, size, coffeePrice))
                        elif choice in ['4', '5']:
                            if choice == "4":
                                count = int(input("Количество: "))
                                for i in range(count):
                                    additionals.append(Additional.Additional("Oreo", "N/A", 150))
                            elif choice == "5":
                                count = int(input("Количество: "))
                                for i in range(count):
                                    additionals.append(Additional.Additional("Пончик", "N/A", 100))
                        elif choice == "6":
                            break
                        else:
                            continue
                        pay = Pay.Pay(eMoney=True, client=User.User(bonus=100, name="Andrey", phone=""),
                                    additionals=additionals, coffees=coffees)
                        payList.append(pay)
                elif choice == "1":
                    summ = 0
                    for payItem in payList:
                        summ += payItem.getSum()
                    smena.setSum(summ)
                    smena.setTimeClose()
                    break
        print(payList)
        break
    else:
        continue

