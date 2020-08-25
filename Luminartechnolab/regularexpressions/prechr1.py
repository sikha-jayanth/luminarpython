from re import *
pattern="a{2}" #two noes of a
pattern="a{2,3}" #min 2 noes max 3 noes of a
matcher=finditer(pattern,"abaaabaaaaa 05@x")
for match in matcher:
    print(match.start())
    print(match.group())