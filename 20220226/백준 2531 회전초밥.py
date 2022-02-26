import sys
ip = sys.stdin.readline
N,d,k,c = map(int,ip().split())
cont = [int(ip()) for _ in range(N)]
max_ = -1
for i in range(N):
    mydict = {}
    mydict[c] = 1
    for j in range(i,i+k):
        j = j % N
        mydict[cont[j]] = 1
    max_ = max(max_,len(mydict))
    if max_ == d:
        print(d)
        exit()
print(max_)
