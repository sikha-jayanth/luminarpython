#program to check whether a given sequence is palindrome or not


num=int(input("enter a number"))
temp=num
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
#print(rev)
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")

