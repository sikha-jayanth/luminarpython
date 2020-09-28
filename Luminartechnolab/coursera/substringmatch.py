import re
# patt="ababa"
# lst=re.findall('aba',patt)
# print(len(lst))
stri="From stephen.marquard@uct.ac.za" \
     "Sat Jan  5 09:14:16 2008"
lst=re.findall('\$',stri)
print(lst)