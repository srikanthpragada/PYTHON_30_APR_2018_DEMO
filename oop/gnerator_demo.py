# Generator that produces even number up to given number
def even_nums(end):
    for i in range(2, end + 1, 2):
        # print("Providing value")
        yield i



for n in even_nums(20):
    print(n)
