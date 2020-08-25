from re import *
rule='\w+[@]gmail[.]com'
f=open("gmailaddress","r")
file1=open("valid","w")
for line in f:
    mail=line.rstrip("\n")
    match=fullmatch(rule,mail)
    if match!=None:
        file1.write(mail)
        file1.write("\n")
        print(mail)
    else:
        continue
file1.close()
