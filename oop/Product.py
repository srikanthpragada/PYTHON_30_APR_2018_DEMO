class Product:
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


c1 = Product("iPhone X", 80000)
print(str(c1))
c1.print()

c2 = Product("Samsung S9")
