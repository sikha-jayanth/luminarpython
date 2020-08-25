line="hello hai hello hai"
lst=line.split(" ")
dict={}
for i in lst:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
for k,v in dict.items():
    print(k,":",v)