
def  even_odd(l1,l2):
    nums =[]
    for n in l1 + l2:
        if n % 2 == 0:
            nums.insert(0,n)
        else:
            nums.append(n)

    return nums

print (even_odd([11,23,8,32], [14,5,7,9,10]))

