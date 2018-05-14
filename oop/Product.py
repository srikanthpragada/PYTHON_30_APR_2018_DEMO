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
    def price(self):
        return self.__price

    @property  # Getter
    def netprice(self):
        return self.__price + (self.__price * self.tax / 100)


class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    def print(self):
        super().print()
        print(self.__discount)

    @property  # Getter
    def netprice(self):
        baseprice = super().price
        gross = baseprice - (baseprice * self.__discount // 100)  # subtract discount
        return gross + (gross * Product.tax / 100)  # Add tax


c1 = Product("iPhone X", 80000)
c1.print()

c1 = DiscountProduct("iPhone 7 plus", 60000, 10)
c1.print()
print(c1.netprice)
