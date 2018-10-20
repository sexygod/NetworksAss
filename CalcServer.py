''' My program fits 100% the requirements asked on the assignment sheet. 
    815009011
    Asa Yee
'''

from socket import *
import re

portNumber = 999
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",portNumber))
print("Waiting for message from UDP Client...")

while(1):
    (data, clientAddr) = s.recvfrom(1024)
    expr = data.decode()
    
    if (expr == "***"):
        print("Client disconnected.")
        break
 
    print("Received from client: ", expr)
    s.sendto("Message Received by server".encode(), clientAddr)

    exprGroup = re.search("(\d+)(.)(\d+)", expr)

    x = int(exprGroup.group(1))
    operator = str(exprGroup.group(2))
    y = int(exprGroup.group(3))

    if (operator == "+"): 
        result = x+y
    elif (operator == "-"):
        result = x-y
    elif (operator == "*"):
        result = x*y
    elif (operator == "/"):
        result = x/y
    else:
        result = "Unexpected result."

    result = "The result of %d %s %d is %d" %(x, operator, y, result)
    s.sendto(result.encode(), clientAddr)
    print ("\"%s\" sent to UDP client." %(result))

input("Press enter to exit");