num1=int(input("enter number 1"))
num2=int(input('enter number 2'))
sum=0
quo=0
while sum<num1:
    sum+=num2
    quo+=1
    print(sum,quo)
# if(sum>num1):
#     quo-=1
#     sum-=num2
print("quotient :",quo)
print("remainder :",num1-sum)






