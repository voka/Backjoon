import sys
ip = sys.stdin.readline
N, M = map(int, ip().split())
dp = [[0]*(201) for _ in range(M+1)]
for i in range(1, M+1):
    day, page = map(int, ip().split())
    for j in range(1, N+1):
        if j - day >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[M][N])
