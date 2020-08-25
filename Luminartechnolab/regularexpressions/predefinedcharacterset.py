from re import *

# pattern='[abc]'
# matcher=finditer(pattern,"abab 05@x")
# for match in matcher:
#     print(match.start())
#     print(match.group())


pattern='[a-z]'
matcher=finditer(pattern,"abab 05@x")
for match in matcher:
    print(match.start())
    print(match.group())