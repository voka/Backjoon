import sys
ip = sys.stdin.readline 
N = int(ip())
lst = list(map(int,ip().split()))
dp = [-1]*2001
dp[0] = 1
for i in range(N):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i],dp[j] + 1)

#print(dp)
print(N-max(dp))

