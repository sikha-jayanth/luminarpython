line="hello hai hello hai bye"
lst=line.split(" ")
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)