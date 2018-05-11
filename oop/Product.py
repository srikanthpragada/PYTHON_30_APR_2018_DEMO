class Product:
    # class variable
    tax = 15

    @staticmethod
    def set_tax(tax):
        if tax >= 5 and tax <= 50:
            Product.tax = tax

    # constructor
    def __init__(self, name, price=0):
        self.__name = name
        self.__price = price

    # method
    def print(self):
        print(self.__name)
        print(self.__price)

    # special method, called by  str()
    def __str__(self):
        return "%s %10d" % (self.__name, self.__price)

    @property  # Getter
    def netprice(self):
        return self.__price + (self.__price * self.tax / 100)


c1 = Product("iPhone X", 80000)
c1.print()
Product.set_tax(20)  # calling static method
print(str(c1))
print(c1.netprice)
