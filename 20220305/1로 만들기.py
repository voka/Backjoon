import sys
ip = sys.stdin.readline 
N = int(ip())
dp = [999999]*(30001)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 3
dp[8] = min(dp[7],dp[8//2])
dp[9] = min(dp[8],dp[9//3])
for i in range(8,N+1):
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i-1],dp[i//5]) + 1
    elif i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i], dp[i-1] + 1,dp[i//3] + 1,dp[i//2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i-1] + 1,dp[i//3] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i-1] + 1,dp[i//2] + 1)
    else:
        dp[i] = min(dp[i],dp[i-1] + 1)
print(dp[N])
tmp = dp[N]
answer = []
for i in range(tmp):
    if N % 5 == 0 and dp[N] - dp[N//5] == 1:
        answer.append(N)
        N = N // 5
    elif N % 3 == 0 and dp[N] - dp[N//3] == 1:
        answer.append(N)
        N = N // 3
    elif N % 2 == 0 and dp[N] - dp[N//2] == 1:
        answer.append(N)
        N = N // 2
    elif dp[N] - dp[N-1] == 1:
        answer.append(N)
        N -= 1
    #print(N)
answer.append(1)
print(*answer)