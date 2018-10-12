from socket import *

portAddress = "localhost"
portNumber = 25565
s = socket(AF_INET,SOCK_STREAM)
s.connect((portAddress,portNumber))

msg = s.recv(1024)
print(str(msg))
input("Press enter to exit.")