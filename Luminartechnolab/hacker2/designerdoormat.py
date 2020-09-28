n=int(input("enter rows:(odd number"))
m=3*n
for i in range(1,n,2):
    print((i*".|.").center(m,'-'))

print("WELCOME".center(m,'-'))
for j in range(n-2,0,-2):
    print((j * ".|.").center(m,'-'))