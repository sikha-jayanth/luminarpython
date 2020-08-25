num1=int(input("enter number 1"))
num2=int(input('enter number 2'))
# sum=0
quo=0
prod=0
while prod<num1:
    quo+=1
    prod+=num2
    #print(quo,prod)
if prod>num1:
    quo-=1
    prod-=num2
print("quotient :",quo,"remainder :",num1-prod)