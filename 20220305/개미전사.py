import sys
ip = sys.stdin.readline
N = int(ip())
storage = list(map(int,ip().split()))
dp = [0]*(N+1)
dp[0] = storage[0]
dp[1] = max(dp[0],storage[1])
for i in range(2,N):
    dp[i] = max(storage[i] + dp[i-2],dp[i-1])
print(dp[N-1])