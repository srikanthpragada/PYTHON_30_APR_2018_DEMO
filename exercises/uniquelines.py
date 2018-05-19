# Usage : python uniquelines.py target source1 source2 ...
import sys

if len(sys.argv) < 3:
    print("Usage : python uniquelines.py target source ...")
    sys.exit(1)  # exit program

try:
    lines = set()
    i = 2
    while i < len(sys.argv):
        # open each source file
        try:
           with open(sys.argv[i], "rt") as source:
              for line in source.readlines():
                lines.add(line)
        except:
            print("File :", sys.argv[i]," not processed!")

        i += 1

    # open target file
    with open(sys.argv[1], "wt") as target:
        for line in sorted(lines):
            target.write(line)

    print("Completed!")
except  Exception as ex:
    print("Sorry! Error : ", str(ex))
