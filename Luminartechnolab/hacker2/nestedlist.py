lst=[]
nlst=[]
lst.append([[input(),float(input())] for _ in range(3)])
# print(lst)
#
# # print(second_larg)
# for i in lst:
#     for k in i:
#         print(k[1])
second_low=sorted(list(set([k[1] for i in lst for k in i])))[1]
print(second_low)
for names in [k[0] for i in lst for k in i if k[1]==second_low]:
    print(names)