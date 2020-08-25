from re import *
# pattern="a+"
# matcher=finditer(pattern,"abaaaab 05@x")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# pattern="a*"
# matcher=finditer(pattern,"abab 05@x")
# for match in matcher:
#     print(match.start())
#     print(match.group())
    
pattern="a?"
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())