from socket import *
import re

portNumber = 999
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",portNumber))
print("Waiting for message from UDP Client...")

while(1):
    (data, clientAddr) = s.recvfrom(1024)
    expr = str(data)
    if (expr == "x"):
        print("Working")
        break
    else:
        print ("No")

    print("Received from client: ", data)
    s.sendto(bytes("Message received", "utf-8"), clientAddr)

    exprGroup = re.search("(\d+)(.)(\d+)", expr)
    print(exprGroup.group(1), exprGroup.group(2), exprGroup.group(3))

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

    result = "The result of " + str(x) + " " + operator + " " + str(y) + " is " + str(result)
    result = result.encode()
    s.sendto(result, clientAddr)
    print (result, "sent to UDP client.")

input("Press enter to exit");