from re import *
rule='[a-k][369][a-zA-Z0-9]*'
var=input("enter variable")
match=fullmatch(rule,var)
if match!=None:
    print("valid")
else:
    print("Invalid")