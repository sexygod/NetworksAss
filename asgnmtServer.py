from socket import *

portNumber = 999
s = socket(AF_INET,SOCK_STREAM)
s.bind((""),portNumber)
s.listen(1)

while(1):
    (c, addr) = s.accept()