handle = open("mbox-short")
hours={}
for lines in handle:
    if not lines.startswith("From "):
        continue
    data = lines.rstrip().split()
    tme=data[5].split(":")
    hr=tme[0]

    if hr not in hours:
        hours[hr]=1
    else:
        hours[hr]+=1

for k,v in sorted(hours.items()):
    print(k,v)