import socket


s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 2000 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port
s.listen(5) # Now, wait for client connection.
print("Server is ready and waiting for clients ...")
while True:
   # Establish connection with client. # It returns connection and address of client
   c, addr = s.accept()
   print("Connted to client", addr, c)
   c.send( "Hello!".encode())
   c.close()



