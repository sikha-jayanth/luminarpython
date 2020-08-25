from re import *
rule='[a-zA-Z0-9]+[@]gmail[.]com'
mail=input("enter mail id")
matcher=fullmatch(rule,mail)
if matcher!=None:
    print("valid")
else:
    print("invalid")