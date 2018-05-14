# uses command line arguments
import sys
import math

# Do this only when run as script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python prime.py  <number>")
        sys.exit()  # stop program

    if not sys.argv[1].isdigit():
        print("Invalid input. Please provide a valid number")
        sys.exit()  # stop program

    num = int(sys.argv[1])
    for i in range(2, math.ceil(math.sqrt(num)) + 1 ):
        if  num % i == 0 :
            print("Not a prime number!")
            sys.exit()

    print("Prime number!")
