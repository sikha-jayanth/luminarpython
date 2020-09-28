str="abcdefghijklmnopqrstuvwxyz"
n=5
lst=list(str[:n])
print(lst)
lst.reverse()
print(lst)
wid=4*n-3
for i in range(1,n+1):
    nlst=lst[:i-1]
    nlst.reverse()
    print('-'.join(lst[:i]+nlst).center(wid,'-'))
for j in range(n,0,-1):
    nlst=lst[:j-1]
    nlst.reverse()
    print('-'.join(lst[:j]+nlst).center(wid,'-'))



import string

alpha = string.ascii_lowercase

num = int(input())

def srange(N):
    return list(range(N))+list(range(N-2,-1,-1))

for i in srange(num):
    print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*(num-1)+1,'-'))