# Phone client connected to 1234

import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = "localhost"  # Get local machine name
port = 1234  # Reserve a port for your service.

s.connect((host, port))

while True:
    name = input("Enter name :")
    s.send(name.encode())
    if name == 'end':
        break
    # receive data from server
    number = s.recv(100).decode()
    if number == "Error":
        print("Sorry! Name not found!")
    else:
        print("Phone Number  :", number)

s.close
