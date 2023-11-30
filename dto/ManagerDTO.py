from classLibrary.Manager import Manager

def GetManagerByLoginAndPassword(login:str, password:str):
    manager = Manager.select().where((Manager.login == login) & (Manager.password == password)).get()
    return manager
