import sys
ip = sys.stdin.readline
X = int(ip())
dp = [1000001] * (1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4,X+1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i],dp[i-1] + 1,dp[i//2] + 1,dp[i//3] + 1)
    elif i % 3 == 0:
        dp[i]  = min(dp[i],dp[i-1] + 1,dp[i//3] + 1)
    elif i % 2 == 0:
        dp[i]  = min(dp[i],dp[i-1]+ 1,dp[i//2]+ 1) 
    else:
        dp[i] = min(dp[i],dp[i-1] + 1)
print(dp[X])