import sys,string
def process():
    mystr = list(sys.stdin.readline())
    lowercases = list(string.ascii_lowercase)
    lowerdict = {}
    numlowdict = {}
    for i in range(len(lowercases)):
        lowerdict[lowercases[i]] = i
        numlowdict[i] = lowercases[i]
    uppercases = list(string.ascii_uppercase)
    upperdict = {}
    numupperdict = {}
    for i in range(len(uppercases)):
        upperdict[uppercases[i]] = i
        numupperdict[i] = uppercases[i]
    for i in range(len(mystr)):
        cur = mystr[i]
        if cur in lowercases:
            tmp = lowerdict[cur]
            tmp += 13
            tmp = tmp % 26
            mystr[i] = numlowdict[tmp]
        elif cur in uppercases:
            tmp = upperdict[cur]
            tmp += 13
            tmp = tmp % 26
            mystr[i] = numupperdict[tmp]
    return mystr
            
answer = process()
print("".join(answer))