lst=[1,2,3,4,5]
num=int(input("enter a number"))
flag=0
for i in lst:
    if(num==i):
        print("found")
        flag=1
if(flag==0):
    print("not found")
