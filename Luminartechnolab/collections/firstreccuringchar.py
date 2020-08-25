line="ABBCCC"
dict={}

for i in line:
    if i not in dict:
        dict[i]=1
    else:
        print("first reccurring character",i)
        break