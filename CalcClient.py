''' 815009011
    Asa Yee
'''

from socket import *

portNumber = 999
s = socket(AF_INET,SOCK_DGRAM)
serverName = "localhost"
message = input("Enter infix equation to send to UDP client \"***\" to quit: ")

while (message != "***"):
    s.sendto(message.encode(), (serverName, portNumber))
    print(s.recv(1024).decode())
    print(s.recv(1024).decode())
    message = input("Enter infix equation to send to UDP client \"***\" to quit: ")

s.sendto(message.encode(), (serverName, portNumber))
input("Press enter to exit");