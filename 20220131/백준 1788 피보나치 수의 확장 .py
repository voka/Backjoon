N = int(input())
dp = [0]*(1000001)
dp[0] = 0
dp[1] = 1
f = 0
if N < 0:
    f = 1
    N = -N
for i in range(2,N+1):
    dp[i] = (dp[i-1]%1000000000 + dp[i-2]%1000000000)
if dp[N] == 0:
    print(0)
else:
    if f == 1:
        if N%2 == 0 :
            print(-1)
        else:
            print(1)
    else:
        print(1)
print(dp[N]%1000000000)