import re
f=open("regex_sum_891723.txt")
new_lst=[]
for lines in f:
    data=lines.strip()
    lst=re.findall('[0-9]+',data)
    if len(lst)<1:
        continue
    if len(new_lst)<1:
        new_lst=[int(i) for i in lst]
    else:
        for i in lst:
            new_lst.append(int(i))
print(sum(new_lst))