#program to find whether a number is prime or not

num=int(input("enter a number"))               #num=3
if(num > 1):
    for i in range(2, num):                     #iterate from 2 to 3
        if (num % i) == 0:                      #3%2=1
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")         #3 is prime number

else:
    print(num, "is not a prime number")