from re import *
str=input("enter a string")
sbstr=input("enter a substring")
count=0
while True:
    pos=str.find(sbstr)
    if pos!=-1:
        count+=1
        str=str[pos+1:]
    else:
        break


# for match in matcher:
#     count+=1
print(count)