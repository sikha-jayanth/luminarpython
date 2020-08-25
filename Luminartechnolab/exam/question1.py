str="ABABABC"
dict={}
max=0
for i in str:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for k,v in dict.items():
    if v > max:
        max = v
        max_key = k

print("most frequent character: ",max_key)