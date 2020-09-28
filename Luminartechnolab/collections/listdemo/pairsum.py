print("enter the number of ")
lst.sort()
low=0
upp=len(lst)-1
num=int(input("enter num"))

while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==num):
        print(lst[low],lst[upp])
        break;
    elif(data>num):
        upp=upp-1
    else:
        low=low+1
