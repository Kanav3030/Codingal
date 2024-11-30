class computer:
    def __init__(self):
        self.__maxprice=5000
    def sell(self):
        print("Selling price:{}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price

co=computer()
co.sell()
co.__maxprice=5500
co.sell()
co.setmaxprice(5500)
co.sell()