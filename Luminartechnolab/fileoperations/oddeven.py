f=open("numbers","r")
evenlst=[]
oddlst=[]
for i in f:
    if(int(i)%2==0):
        evenlst.append(i.rstrip("\n"))
    else:
        oddlst.append(i.rstrip("\n"))
print("evenlist :",evenlst)
print("oddlist:",oddlst)