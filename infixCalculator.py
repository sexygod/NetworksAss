import re 

strExpr = "asaYee"
m = re.search("(asa)(Yee)", strExpr)
print(m.group()) #t1
print(m.group(1), m.group(2)) #t2

strExpr = "1+1"
m = re.search("(1)", strExpr)
print(m.group()) #t3
m = re.search("(1)(\+)(1)", strExpr)
print(m.group(1), m.group(2), m.group(3)) #t4

m = re.search("(1)(.)(1)", strExpr)
print(m.group(1), m.group(2), m.group(3)) #t5

m = re.search("(\d)(.)(\d)", strExpr)
print(m.group(1), m.group(2), m.group(3)) #t6

strExpr = "2/33"
m = re.search("(\d+)(.)(\d+)", strExpr)
print(m.group(1), m.group(2), m.group(3)) #t7

x = int(m.group(1))
operator = str(m.group(2))
y = int(m.group(3))

if (operator == "+"): 
    print (x+y)
elif (operator == "-"):
    print (x-y)
elif (operator == "*"):
    print (x*y)
else:
    print (x/y)