#program to implement bubble sort


lst=[]
n=int(input("enter the size of the list"))
print("enter elements: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print("input list:",lst)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("list after sorting",lst)

