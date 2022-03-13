import sys
ip = sys.stdin.readline
N,R = map(int,ip().split())
dp = [[1 if j == 0 else 0 for j in range(R+2) ] for i in range(N+2)]
dp[1][1] = 1
dp[1][0] = 1
for i in range(1,N+1):
    for j in range(1,R+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp)
print(dp[N][R])