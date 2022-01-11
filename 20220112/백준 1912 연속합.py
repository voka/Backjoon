from sys import stdin 
N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [0]*(N)
dp[0] = nums[0]
answer = -5000
for i in range(1,N):
    dp[i] = max(dp[i-1] + nums[i],nums[i])
    answer = max(answer,dp[i])
answer = max(answer,dp[0])
print(answer)