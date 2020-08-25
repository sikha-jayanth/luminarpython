def factNum(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
data=factNum(5)
print(data)

