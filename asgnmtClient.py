from socket import *

portNumber = 999
s = socket(AF_INET,SOCK_DGRAM)
serverName = "localhost"
message = input("Enter infix equation to send to UDP client \"***\" to quit: ")

while (message != "***"):
    s.sendto(bytes(message,"utf-8"), (serverName, portNumber))
    print(str(s.recv(1024)))
    print(str(s.recv(1024)))
    message = input("Enter infix equation to send to UDP client \"***\" to quit: ")

s.sendto(bytes(message,"utf-8"), (serverName, portNumber))
input("Press enter to exit");