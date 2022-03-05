import sys
ip = sys.stdin.readline
N,M = map(int,ip().split())
coins = [int(ip()) for _ in range(N)]
dp = [10001]*(10001)
dp[0] = 0
for c in coins :
    dp[c] = 1
for i in range(M+1):
    for c in coins:
        if i - c < 0 :
            break
        dp[i] = min(dp[i],dp[i-c] + 1)
if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
print(dp[:M+1])
tmp = dp[M]
answer = [M]
for i in range(tmp):
    hubo = []
    for c in coins:
        if dp[M] == dp[M-c] + 1 :
            hubo.append(c)
    answer.append(max(hubo))
    M -= max(hubo)
print(*answer)