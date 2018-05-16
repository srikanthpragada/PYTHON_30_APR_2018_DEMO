class A:
    def print(self):
        print("A")

class B(A):
    def print(self):
        print("B")

class C:
    def print(self):
        print("C")

class D(C):
    def print(self):
        print("D")

class E(B, D):
    def print(self):
        super().print();
    pass
    # def print(self):
    #     print("E")

obj = E()
obj.print()

print(E.__mro__)