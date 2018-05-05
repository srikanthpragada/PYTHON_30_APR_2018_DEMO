# print each word in reverse

st = input("Enter a string : ")

words = st.split()

for w in words:
    for c in reversed(w):
        print(c, end='')

    print(' ', len(w))



