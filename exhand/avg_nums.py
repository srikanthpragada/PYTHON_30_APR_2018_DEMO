sum = 0
i = 1
while (i <= 5):
    try:
        num = int(input("Enter a number : "))
        sum += num
        i += 1
    except:
        print("Sorry! Invalid number. Please try again!")

print("Average = ", sum // 5)
