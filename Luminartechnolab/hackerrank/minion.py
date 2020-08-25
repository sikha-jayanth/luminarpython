def minion(s):
    stuart=0
    kevin=0
    vow=['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            subs=s[i:j]
            if subs[0] in vow:
                kevin+=1
            else:
                stuart+=1
    if stuart>kevin:
        print("stuart",stuart)
    elif kevin>stuart:
        print("kevin", kevin)
    else:
        print("its a tie")

str=input("enter a string:")
minion(str)


