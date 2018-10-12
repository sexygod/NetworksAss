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

