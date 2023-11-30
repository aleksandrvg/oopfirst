from classLibrary.Additional import Additional
from classLibrary.Coffee import Coffee
from classLibrary.Manager import Manager

def CreateAdditional():
    additional = Additional(size="XL", type="Сироп", price=30.0)
    additional.save()
    additional1 = Additional(size="L", type="Сироп", price=20.0)
    additional1.save()
    additional2 = Additional(size="M", type="Сироп", price=10.0)
    additional2.save()

def CreateCofee():
    coffe = Coffee(type="Латте", size="M", price=120.0)
    coffe.save()
    coffe1 = Coffee(type="Капучино", size="M", price=130.0)
    coffe1.save()
    coffe2 = Coffee(type="Раф", size="M", price=140.0)
    coffe2.save()

def CreateManager():
    manager = Manager(login="123", password="123", name="Oleg", phone="8800555355", bonus=0)
    manager.save()

if __name__ == "__main__":
    CreateAdditional()
    CreateCofee()
    CreateManager()

