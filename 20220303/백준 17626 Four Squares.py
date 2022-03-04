import sys

ip = sys.stdin.readline 
n = int(ip())

dp = [0]*50001

dp[1]  = 1

for i in range(1,n+1):
    dp[i] = dp[1] + dp[i-1]
    for j in range(2,i):
        if j * j > i :
            break
        dp[i] = min(dp[i], 1 + dp[i-j*j])
print(dp[n])