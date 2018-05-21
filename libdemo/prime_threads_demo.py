import math
import threading


class PrimeThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        for n in range(2, math.floor(math.sqrt(self.num)) + 1):
            if self.num % n == 0:
                print(self.num, " is not prime")
                break
        else:
            print(self.num, " is prime")


nums = [3987341, 349837498374911173, 5915587277, 398340321022293, 17, 3343434343433443222221111]

for n in nums:
    t = PrimeThread(n)
    t.start()
