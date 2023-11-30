from classLibrary.Additional import Additional

def GetAllAdditional():
    additionals = Additional.select().dicts()
    returnAdditionals = []
    for additional in additionals:
        returnAdditionals.append(Additional(id=additional["id"], type=additional["type"], size=additional["size"], price=additional["price"]))
    return returnAdditionals

def GetAdditionalById(Id:int):
    additional = Additional.select().where(Additional.id == Id).get()
    return additional
