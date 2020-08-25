str="aabcaaada"
k=3

for i in range(0,len(str),k):
    n_str=str[i:i+k]
    lst = []
    for j in n_str:
        if j not in lst:
            lst.append(j)

    print(''.join(lst))