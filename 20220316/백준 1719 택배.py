import sys
ip = sys.stdin.readline 
n,m = map(int,ip().split())
dist = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,t = map(int,ip().split())
    dist[a][b] = min(dist[a][b],t)
    dist[b][a] = min(dist[b][a],t)
answer = [[j for j in range(1,n+1)] for _ in range(1,n+1)]
for k in range(1,n+1):
    dist[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                answer[i-1][j-1] = answer[i-1][k-1]

for i in range(n):
    for j in range(n):
        if i == j:
            print("-",end = "")
        else:
            print(answer[i][j], end = "")
        if j != n-1:
            print(" ",end="")
        else:
            print()
    
