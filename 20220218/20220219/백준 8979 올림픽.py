import sys
ip = sys.stdin.readline
N,K = map(int,ip().split())
mylist = {}
for i in range(N):
    tmp = list(map(int,ip().split()))
    mylist[tmp[0]] = tmp[1:]
sorting = sorted(mylist.items(),key = lambda x : (-x[1][0],-x[1][1],-x[1][2]))
nums = 1
rank = [0]*(N+1)
rank[sorting[0][0]] = 1
for i in range(1,N):
    if sorting[i-1][1] == sorting[i][1]:
        rank[sorting[i][0]] = rank[sorting[i-1][0]]
    else:
        rank[sorting[i][0]] = i+1
    if K == sorting[i][0]:
        break
print(rank[K])