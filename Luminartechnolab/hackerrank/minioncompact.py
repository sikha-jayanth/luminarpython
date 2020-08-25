


def minion_game(str):
    vowel =['a','e','i','o','u','A','E','I','O','U']
    stuart=0
    kevin=0
    for i in range(len(str)):
        #print(str[i])

        if str[i] in vowel:
            kevin+=len(str)-i
            #print("k",K)
        else:
            stuart+=len(str)-i
            #print("s",S)

    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")

str=input("enter a string")
minion_game(str)


n = int(input())
print(hash(tuple(map(int, input().rstrip("\n").split()))))