f=open("numbers","r")
lst=[]
sum=0
for i in f:
    #lst.append(int(i))
    lst.append(i.rstrip("\n"))
    sum=sum+int(i)
print(lst)
print(sum)