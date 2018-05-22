import math
import threading


class PrimeThread(threading.Thread):
    def __init__(self, num, file):
        super().__init__()
        self.num = num
        self.file = file

    def run(self):
        for n in range(2, math.floor(math.sqrt(self.num)) + 1):
            if self.num % n == 0:
                self.file.write("%d is not prime\n" % (self.num))
                break
        else:
            self.file.write("%d is prime\n" % (self.num))


nums = [3987341, 349837498374911173, 5915587277, 398340321022293, 17, 3343434343433443222221111]

f = open(r"e:\classroom\python\primes.txt", "wt")

for n in nums:
    t = PrimeThread(n, f)
    t.start()

print("Waiting for threads to terminate!")
# Wait until all threads except main thread  are terminated
while threading.active_count() > 1:
    pass

f.close()
print("Completed!")
