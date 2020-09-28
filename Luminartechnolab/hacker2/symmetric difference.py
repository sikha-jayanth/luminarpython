num1=int(input())
s1=set(map(int,input().split()))
num2=int(input())
s2=set(map(int,input().split()))
sd=set()
sd.update(s1.difference(s2),s2.difference(s1))
for i in sorted(list(sd)):
    print(i)