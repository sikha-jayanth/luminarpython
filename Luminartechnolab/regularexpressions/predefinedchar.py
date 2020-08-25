from re import *

pattern="\s"  #spaces
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())

pattern="\d"  #[0-9]
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())

pattern="\D"   #[^0-9]
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())


pattern="\w"  #[a-zA-Z0-9] all words except special characters
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())

pattern="\W"  #special characters
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())