import sys
ip = sys.stdin.readline
N = int(ip())
Lose = list(map(int,ip().split()))
Joy = list(map(int,ip().split()))
dp = [[0]*101 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(100):
        if j < Lose[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-Lose[i-1]] + Joy[i-1])

print(dp[N][99])
    
