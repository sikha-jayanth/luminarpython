num1=int(input("enter a number"))
num2=int(input("enter num2"))
lst=[1,2,3]
try:
    res=num1/num2
    n=int(input("enter list position"))
    print(lst[n])

    print("operation completed successfully")
except Exception as e:
    print(e.args)
