import sys
ip = sys.stdin.readline 
INF = int(1e9)
n = int(ip())
m = int(ip())

dp = [[INF]*(n) for _ in range(n)]
for i in range(m):
    a,b,c = map(int,ip().split())
    dp[a-1][b-1] = min(c,dp[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for answers in dp:
    for ans in answers:
        if ans == INF:
            print(0,end=" ")
        else:
            print(ans,end=" ")
    print()