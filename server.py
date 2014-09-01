# A simple server
import socket
s = socket.socket()             # create a socket object
host = socket.gethostname()     # get local machine name
port = 12345                    # reverse a port for your service
s.bind((host, port))            # bind to the port

s.listen(5)                     # wait for client connection

while True:
    c, addr = s.accept()
    print 'Got connection from,', addr
    c.send('Thank you for connecting')
    c.close()
    

# in the terminal we type 
# python server.py &
# python client.py


