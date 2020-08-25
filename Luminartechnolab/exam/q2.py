lst=['x','y','z','x']
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if(lst[i]!=lst[j]):
            print(lst[i], lst[j])



