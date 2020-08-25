lst=[]
lst1=[]
n=int(input("enter the no of elements: ")) #n=3
print("enter the numbers")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print("the list is: ",lst)       #[2,4,6]

for i in range(0,n-1):           #i=0 to 2
    lst1.append(lst[i]+lst[i+1]) #i=0 lst1[0]= 2+4=6
                                 #i=1  lst1[1]=4+6=10
lst1.append(lst[-1]+lst[0])  #lst1[2]=6+2=8   lst1=[6,10,8]
lst1.sort(reverse=True)      #lst1=[10,8,6]
print("new list: ",lst1)