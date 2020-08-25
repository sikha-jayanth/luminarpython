str=input("enter a  string")
lst=str.rstrip("\n").split(" ")
for i in lst:
    print(i.capitalize(),end=" ")

