num1=int(input("enter a number"))
num2=int(input("enter num2"))
lst=[1,2,3]
try:
    res=num1/num2

    print("operation completed successfully")
except Exception as e:
    num1 = int(input("enter a number"))
    num2 = int(input("enter num2"))
    lst = [1, 2, 3]
    try:
        res = num1 / num2
    except Exception as e:
        print(e.args)

finally:
    print("successfull")
