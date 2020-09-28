n = int(input("enter the no of scores"))
arr = map(int, input().split())
print(arr)
sort_arr=sorted(arr)
n_set=set(sort_arr)
print(n_set)
print(n_set.pop())


# print(n_tuple[-2])