import sys
ip = sys.stdin.readline 
N,K = map(int,ip().split())
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(1,K+1):
        if i == 0 or j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[N][K])
            