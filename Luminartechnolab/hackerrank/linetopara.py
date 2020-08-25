str=input("enter a string :")
wid=int(input("width"))
nstr=""
for i in range(0,len(str),wid):
    nstr=nstr+str[i:wid+i]+"\n"
print(nstr)