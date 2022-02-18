import sys
ip = sys.stdin.readline
N = int(input())
mydict = {}

for i in range(N):
    s = ip().strip()
    if s in mydict:
        mydict[s] += 1
    else:
        mydict[s] = 1

answer = sorted(mydict.items(), key = lambda x : (-x[1],x[0]))
print(answer[0][0])
    
    
    