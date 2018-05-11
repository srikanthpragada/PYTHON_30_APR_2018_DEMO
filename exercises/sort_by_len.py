
names = [ 'Bill','Larry','Kim','Ben','John','Joe','Armstrong']

for n in sorted(names, key  = lambda x : (len(x),x) ):
    print(n)