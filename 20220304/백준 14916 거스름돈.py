import math
n = int(input())
dp = [100001]*(n+1)
dp[0] = 0
i_max = math.floor(n / 5) +1
j_max = math.floor(n / 2) +1
if n%5 == 0:
    print(n//5)
    exit()
for i in range(i_max,-1,-1):
    for j in range(j_max):
        cur = i*5 + j*2
        if cur > n:
            break
        if dp[cur] < i + j:
            break
        dp[cur] = i+j
if dp[n] == 100001:
    print(-1)
else:
    print(dp[n])