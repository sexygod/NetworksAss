from socket import *

portNumber = 25565
s = socket(AF_INET,SOCK_STREAM)
s.bind(("", portNumber))
s.listen(1)
print("Listening...")

while(1):
    (c, addr) = s.accept()
    print("Connected to ", addr)
    msg = "Your mother is a whore"
    c.send(msg.encode("ascii"))
    c.close()
    print("Disconnected from ", addr)
    break

input("Press enter to exit.")