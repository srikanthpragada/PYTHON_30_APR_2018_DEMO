# Largest of 5 numbers

largest = 0
for i in range(1, 6):
    num = int(input("Enter a number :"))
    if num > largest:
        largest = num


print("Largest of numbers is : ", largest)
