N = int(input())
dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]
if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    print(2*(dp[N]+dp[N-1]+dp[N-1]+dp[N-2]) )