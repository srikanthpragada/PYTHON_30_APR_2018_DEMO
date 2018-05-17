

f = open(r"e:\classroom\python\names.txt","rt")

for name in sorted(f.readlines()):
    print(name, end='')

f.close()