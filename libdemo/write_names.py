

f = open(r"e:\classroom\python\names.txt","wt")
names = ["Python","C#","Java","JavaScript","C++"]
for name in names:
    f.write(name + "\n")

f.close()