# lst=[]
# even=[]
# odd=[]
#
# for i in range(50,100):
#     lst.append(i)
# print(lst)
# for i in lst:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print("even list",even)
# print("odd list",odd)

num1=[i for i in range(50,100)]
even=[i for i in num1 if i%2==0]
odd=[i for i in num1 if i%2!=0]
print(even,odd)