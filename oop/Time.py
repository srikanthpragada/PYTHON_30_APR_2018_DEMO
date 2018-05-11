
class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h = h;
        self.m = m;
        self.s = s

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h,self.m, self.s)

    def __eq__(self, other):
        print("__eq__")
        return  self.h == other.h and self.m == other.m and self.s == other.s

    @property
    def totalseconds(self):
        return  self.h * 3600 + self.m * 60 + self.s

    def __gt__(self, other):
        print("__gt__")
        return self.totalseconds > other.totalseconds

    #  time + int
    def __add__(self, seconds):
        return Time(self.h, self.m, self.s + seconds)

t1 = Time(11,20,30)
t2 = Time(10,20,30)
print(str(t1))
print (t1 == t2)   #   __eq__(t1,t2)
print (t1 > t2)   # __gt__(t1,t2)

t3 = t1 + 3000
print(t3)

#  t3 = t1 + "abc"

t1 += 2













