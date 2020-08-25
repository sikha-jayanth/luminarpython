ls=[1,2,3,4]
def square(num):
    return num*num
sq=list(map(square,ls))
print(sq)

def evens(num):
    return num%2==0
el=list(filter(evens,ls))
print(el)