
lst=[]
fh = open("mbox-short")
count = 0
for lines in fh:
    if not lines.startswith("From "):
        continue
    data=lines.rstrip().split()
    print(data[1])
    count+=1


    # if dat[0]!="From":
    #     continue
    # else:
    #     print(dat[1])
    #     count+=1


    # print(dat)
    # count+=1



print("There were",count, "lines in the file with From as the first word")
