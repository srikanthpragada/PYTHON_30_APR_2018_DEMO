import os

dirname = r"e:\classroom\python\apr30\demo"


def printfile(filename):
    fobj = open(filename, "rt")
    print("\nFilename : " + filename)
    print('-' * 70)
    for lineno, line in enumerate(fobj.readlines()):
        print("%4d: %s" % (lineno + 1, line), end='')


for f in os.listdir(dirname):
    if f.endswith(".py"):
        printfile(dirname + "\\" + f)
