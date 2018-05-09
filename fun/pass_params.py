def clearall(list):
    print(id(l))
    list.clear()
    print(id(l))

# def swap(a,b):
#     print(id(a), id(b))
#     a,b = b, a
#     print(id(a), id(b))
#
# n1 = 10
# n2 = 20
#
# print(id(n1), id(n2))
# swap(n1,n2)
#
# print(n1,n2)

l = [10,20]
print ( id(l))
clearall(l)
print(l)

