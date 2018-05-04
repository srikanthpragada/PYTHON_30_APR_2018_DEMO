nums = [10, 2, 35, 4, 15]
names = ['A', 'B','C']

for n in sorted(nums):
    print(n)

for n in enumerate(nums):
    print(n[0] + 1, '->', n[1])

lst = zip(nums,names)

for v in lst:
    print(v)


