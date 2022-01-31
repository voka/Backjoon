N = int(input())
dp = [0]*(36)
dp[0] = 1
dp[1] = 1
for i in range(2,N+1):
    #print(i)
    for j in range(i):
        #print(j,i-1-j,end=" ")
        dp[i] += dp[j]*dp[i-1-j]
    #print()
print(dp[N])