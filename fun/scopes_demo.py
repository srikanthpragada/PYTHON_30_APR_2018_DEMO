g = 100


def fun():
    l = 10
    print(l, g)  # access global variable g


def fun1():
    g = 20  # create local variable called g
    print(g)


def fun2():
    global g
    g = 20  # assign value to global variable g
    print(g)


print(g)
fun()
print(g)
