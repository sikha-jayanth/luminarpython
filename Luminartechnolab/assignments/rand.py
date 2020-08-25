handle = open("mbox-short")
bigname = None
bigvalue = None
mails = {}
for lines in handle:
    if not lines.startswith("From "):
        continue
    data = lines.rstrip().split()
    addr = data[1]
    if addr not in mails:
        mails[addr]=1
    else:
        mails[addr]+=1

for k, v in mails.items():
    if bigvalue is None or v > bigvalue:
        bigvalue = v
        bigname = k
print(bigname, bigvalue)
