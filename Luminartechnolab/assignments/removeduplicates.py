lst=[]
newlst=[]
n=int(input("enter the size of list"))
print("enter elements:")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
for i in lst:
    if i not in newlst:
        newlst.append(i)
print(newlst)
