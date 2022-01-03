from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9) # python의 defalut 최대 재귀수를 10^9번으로 바꾼다.

N = int(stdin.readline()) 
dx = [1,0,-1,0]
dy = [0,1,0,-1]
maps = [[] for _ in range(N)]
dp = [[0]*N for _ in range(N)]
for i in range(N):
    maps[i] = list(map(int,stdin.readline().split()))
    
def DFS(x,y):
    if dp[x][y] != 0: return dp[x][y]
    
    dp[x][y] = 1
    
    for k in range(4):
        
        n_i,n_j = x+dy[k],y+dx[k]
        
        if (n_i >= N) or (n_i<0) or (n_j >= N) or (n_j<0): continue
        
        if maps[x][y] < maps[n_i][n_j]:
            dp[x][y] = max(dp[x][y], DFS(n_i,n_j)+1)
            
    return dp[x][y]

answer = 0  
for i in range(N):
    for j in range(N):
        answer = max(answer,DFS(i,j))
print(answer)