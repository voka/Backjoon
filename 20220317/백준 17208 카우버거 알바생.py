import sys
ip = sys.stdin.readline 
N,M,K = map(int,ip().split())
orders = []
for i in range(N):
    orders.append(tuple(map(int,ip().split())))
dp = [[0]*(K+1) for _ in range(M+1)]
for i in range(N):
    for j in range(M,0,-1):
        for k in range(K,0,-1):
            if k >= orders[i][1] and j >= orders[i][0]:
                dp[j][k] = max(dp[j][k], dp[j-orders[i][0]][k-orders[i][1]] + 1)
print(dp[-1][-1])