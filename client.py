# A simple client
import socket
s = socket.socket()             # create a socket object
host = socket.gethostname()     # get local machine name
port = 12345                    # reverse a port for your service
s.connect((host, port))
print s.recv(1024)
s.close()

# in the terminal we type 
# python server.py &
# python client.py