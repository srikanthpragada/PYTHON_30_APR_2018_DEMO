import pickle

class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def __str__(self):
        return "{0}-{1}".format(self._name, self._email);

# Pickle
p = Person("jack","jack@gmail.com")
f = open(r"e:\classroom\python\jack.dat","wb")
pickle.dump(p,f)
f.close()


# Unpickle
f = open(r"e:\classroom\python\jack.dat","rb")
p = pickle.load(f)
print(p)
