import sys
ip = sys.stdin.readline

while True:
    N = int(ip())
    if N == 0:
        break
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            if i == 0:
                dp[j][i] = 1
            else:
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
    print(dp[N][N])
