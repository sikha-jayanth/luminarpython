employees=[[1001,"ann",15000],[1002,"bnn",21000],[1003,"cnn",31000]]
sum=0
for emp in employees:
    sum=sum+emp[2]
print(sum)
for emp in employees:
    if(emp[2]>17000):
        print(emp[1])