from re import *
rule='[0-9]{10}'
phno=input("enter ph no")
matcher=fullmatch(rule,phno)
if matcher!=None:
    print("valid")
else:
    print("invalid")