from classLibrary.User import User
from classLibrary.Additional import Additional
from classLibrary.Pay import Pay


if __name__ == "__main__":
    User.create_table()
    Additional.create_table()
    Pay.create_table()
    print("Migration Done")

