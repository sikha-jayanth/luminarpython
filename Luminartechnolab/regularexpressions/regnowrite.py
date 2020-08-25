from re import *
rule='[kK][lL][0-9]{2}[a-z]{1,2}\d{4}'
f=open("regno","r")
lst=[]
for line in f:
    regno=line.rstrip("\n")
    matcher = fullmatch(rule, regno)
    if matcher != None:
        lst.append(regno)
    else:
        continue
print(lst)