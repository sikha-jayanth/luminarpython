n=int(input("enter a number"))
if(n%2==0):
    if(2<n<5):
        print("not weird")
    elif(6<n<20):
        print("weird")
    else:
        if(n>20):
            print()