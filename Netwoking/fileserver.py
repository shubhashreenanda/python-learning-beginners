import socket
from fileinput import filename

import settype
from Netwoking.urllibdemo import content

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("Server listening on port:",port)
s.listen(1)

c,addr = s.accept()

filename = c.recv(1024)

try:
    f = open(filename,'rb')
    content = f.read()
    c.send(content)
    f.close()
except fileNotFoundError:
    c.send(b"File does not exist")

c.close()
