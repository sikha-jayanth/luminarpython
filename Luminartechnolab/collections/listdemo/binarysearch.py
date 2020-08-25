lst=[14,12,10,5,6]
n=int(input("enter a number"))
lst.sort()
low=0
upp=len(lst)-1
#mid=(low+upp)//2
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(n>lst[mid]):
        low=mid+1
    elif(n<lst[mid]):
        upp=mid-1
    elif(n==lst[mid]):
        flag=1
        break;
if(flag==0):
    print("not found")
else:
    print("found")
