import sys
ip = sys.stdin.readline
N = int(ip())
Ps = list(map(int,ip().split()))
M = int(ip())
dp = [-50001 for _ in range(M+1)]
for i in range(N-1,-1,-1):
    my = Ps[i] 
    for j in range(my,M+1):
        dp[j] = max(dp[j-my]*10+i, i, dp[j]) # (현재돈 - my)로 살수있는 최대 방번호  * 10 + 현재 방 번호 , 현재 방번호 , 현재돈으로 살수있는 최대 방번호 
    #print(dp)

print(dp[M]) 
        