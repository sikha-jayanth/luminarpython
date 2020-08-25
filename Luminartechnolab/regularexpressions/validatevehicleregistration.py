from re import *
rule='[kK][lL][0-9]{2}[a-z]{1,2}\d{4}'
regno=input("enter reg no")
matcher=fullmatch(rule,regno)
if matcher!=None:
    print("valid")
else:
    print("invalid")