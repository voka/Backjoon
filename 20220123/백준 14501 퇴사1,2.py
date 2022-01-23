import sys
# 점화식 

# dp[N] = max(dp[N],dp[N - T[i]] + P[i] )
# dp[i+T[i]] = max(dp[i] + P[i], dp[i+T[i]])
N = int(sys.stdin.readline())
T = [0]*(N+1)
P = [0]*(N+1)
dp = [0]*(N+2)
for i in range(1,N+1):
    T[i],P[i] = map(int,sys.stdin.readline().split())
cur_max = 0
for i in range(1,N+1):
    #print(i+T[i],P[i])
    cur_max = max(cur_max,dp[i])
    if i+T[i] <= N+1:
        dp[i+T[i]] = max(cur_max+P[i], dp[i+T[i]])
    
print(max(dp))


"""  
"""