class A:
    def print(self):
        print("A")

class B(A):
    def print(self):
        print("B")

class D(A):
    def print(self):
        print("D")

class E(D,B):
    pass

# obj = E()
# obj.print()
print(E.__mro__)