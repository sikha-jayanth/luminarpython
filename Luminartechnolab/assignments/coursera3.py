fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if not line.startswith("From"):
        continue
    data=line.rstrip().split()
    print(data)
print(lst)
lst.sort()
print(lst)
