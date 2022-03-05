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
        dp[i]  = min(dp[i],dp[i-1] + 1,dp[i//2] + 1)
    else:
        dp[i] = min(dp[i],dp[i-1] + 1)
print(dp[X])
tmp = dp[X]
answer = []
for i in range(tmp):
    if X % 3 == 0 and dp[X] - dp[X//3] == 1:
        answer.append(X)
        X = X // 3
    elif X % 2 == 0 and dp[X] - dp[X//2] == 1:
        answer.append(X)
        X = X // 2
    elif dp[X] - dp[X-1] == 1:
        answer.append(X)
        X = X - 1
answer.append(1)
print(*answer)
