# Take names from user and write them in sorted order into names.txt
names = set()
while True:
    name = input("Enter a name : ")
    if name == "end":
        break
    names.add(name)

# write names into file
with open(r"e:\classroom\python\names.txt","wt") as f:
   for name in sorted(names):
      f.write(name + "\n")


