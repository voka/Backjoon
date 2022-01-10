from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
N = int(stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    u,v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
dp = [[0]*(2) for _ in range(N+1)] # dp[i][0] : 얼리어답터일 경우 , dp[i][1] : 일반인일 경우 
visited = [0]*(N+1)
def search(x):
    visited[x] = 1
    dp[x][0] = 1
    for i in graph[x]:
        if(visited[i]): continue
        search(i)
        dp[x][1] += dp[i][0] # 자신이 일반인이라면 주변의 자식들이 모두 얼리어답터여야 한다. 
        dp[x][0] += min(dp[i][1],dp[i][0]) # 자신이 얼리어답터일경우  주변이 일반인이든 얼리어답터이든 관계가 없으므로 둘중 작은 값을 더해준다.
    
search(1)
print(min(dp[1]))
