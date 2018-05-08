
# Telephone directory
teldir = {}

while True:
    name = input("Enter name : ")
    if name == 'end':
        break

    phone = input("Enter mobile :")

    if name in  teldir:
        teldir[name].add(phone)
    else:
        teldir[name] = {phone}


for  name,phones in sorted(teldir.items()):
    print(name)
    for p in phones:
        print(p, end=' ')

    print()





