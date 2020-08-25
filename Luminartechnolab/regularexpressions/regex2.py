from re import *
pattern='[A-Z]'
matcher=finditer(pattern,"abAb 05@X")
for match in matcher:
    print(match.start())
    print(match.group())

pattern='[a-zA-Z0-9]'
matcher=finditer(pattern,"abAb 05@X")
for match in matcher:
    print(match.start())
    print(match.group())


pattern='[^0-9]'  #except 0-9
matcher=finditer(pattern,"abAb 05@X")
for match in matcher:
    print(match.start())
    print(match.group())


pattern='[^a-zA-Z0-9]'  #for only special characters
matcher=finditer(pattern,"abAb 05@X")
for match in matcher:
    print(match.start())
    print(match.group())
