# Armstrong number ex : 153

onum = num = int(input("Enter a number :"))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10


if sum == onum:
    print("Armstrong")
else:
    print("Not an Armstrong")
