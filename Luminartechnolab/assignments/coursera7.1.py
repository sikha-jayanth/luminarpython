largest = None
smallest = None
fnum=0
while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            fnum = int(num)
        except:
            print("Invalid input")
        if smallest is None:
            smallest = fnum
        if fnum < smallest:
            smallest = fnum
        if largest is None:
            largest = fnum
        if fnum > largest:
            largest = fnum





print("maximum is",largest)
print("Minimum is",smallest)
