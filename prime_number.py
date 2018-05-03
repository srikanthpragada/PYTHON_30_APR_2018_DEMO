# Prime number check

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(num, "Not a prime! ")
        break
else:
    print(num, "Prime number!")



