lst=[]
n=int(input("enter the number of elements: "))
print("start enerting elements")
for i in range(n):
    ele=int(input())
    lst.append(ele)

lst.sort()
low=0
upp=len(lst)-1
num=int(input("enter num"))
print("list is :",lst)
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==num):
        print("pair :","(",lst[low],",",lst[upp],")")
        break;
    elif(data>num):
        upp=upp-1
    else:
        low=low-1