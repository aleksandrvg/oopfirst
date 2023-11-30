from classLibrary.Coffee import Coffee

def GetAllCoffe():
    coffes = Coffee.select().dicts()
    returnCoffe = []
    for coffe in coffes:
        returnCoffe.append(Coffee(id=coffe["id"], type=coffe["type"], size=coffe["size"], price=coffe["price"]))
    return returnCoffe

def GetCoffeById(Id:int):
    coffe = Coffee.select().where(Coffee.id == Id).get()
    return coffe
