n,m=map(int,input().split())
ls=map(int,input().split())
sa=set(map(int,input().split()))
sb=set(map(int,input().split()))

hp=[1 if i in sa else -1 if i in sb else 0 for i in ls]
print(sum(hp))