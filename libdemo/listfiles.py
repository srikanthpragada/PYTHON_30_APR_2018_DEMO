import os

start = r"e:\classroom\python\apr30\demo"

for dir in os.walk(start):
    # ignore directory that contain . (dot)
    if dir[0].find(".") >= 0:
        continue

    print("Directory : ", dir[0])
    for f in dir[2]:
        if f.endswith(".py"):
            print(" " * 5, f)
