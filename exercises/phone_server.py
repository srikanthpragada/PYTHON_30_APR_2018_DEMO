# Phone server running at 1234

import socket

phones = {}
f = open(r"e:\classroom\python\phones.txt","rt")
for line in f.readlines():
    parts = line.split(":")
    if len(parts) == 2:
        phones[parts[0]] = parts[1]

f.close()


s = socket.socket()          # Create a socket object
host = "localhost"
port = 1234                  # Reserve a port for your service.
s.bind((host, port))         # Bind to the port

s.listen(1)  # Now wait for client connection.
print("Phone server is waiting ....")
while True:
    client, addr = s.accept()  # Establish connection with client. It returns connection and address of client
    print("Connected to client on :", addr)
    while True:
        # Receive name from client
        name = client.recv(100).decode()
        if name == "end":
            break
        if name in phones:
            client.send(phones[name].encode())
        else:
            client.send("Error".encode())

    print("Closed connection with client!")
    client.close()
