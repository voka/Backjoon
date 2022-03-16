import sys
ip = sys.stdin.readline 
n,m,r  = map(int,ip().split())
dist = [[16]*(n+1) for _ in range(n+1)]
items = list(map(int,ip().split()))
for i in range(r):
    a,b,l = map(int,ip().split())
    dist[a][b] = min(dist[a][b],l)
    dist[b][a] = min(dist[b][a],l)

for k in range(1,n+1):
    dist[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
answer = 0
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if dist[i][j] <= m:
            tmp += items[j-1]
    answer = max(answer,tmp)
print(answer) 
