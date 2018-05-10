v = 1
def  fun():
    #print("In fun()")
    v = 10
    def fun2():
        #print("In fun2()")
        nonlocal v
        v =  100
        print(v)

    fun2()

fun()
print(v)