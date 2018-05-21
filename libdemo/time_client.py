import socket

c = socket.socket()
host = socket.gethostname()
c.connect((host,2000))

data = c.recv(100)
print(data)
print(data.decode())
c.close()
