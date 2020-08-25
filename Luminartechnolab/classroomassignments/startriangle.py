#program to print star triangle

n=int(input("enter the number of rows"))
sp=2*n-2                                  #calculating the space needed
for i in range(1,n+1):
    for j in range(0,sp):
        print(end=" ")
    sp=sp-1
    for k in range(0,i):
        print("*",end=" ")
    print(" ")


