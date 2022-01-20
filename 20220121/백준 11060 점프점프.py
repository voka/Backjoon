from sys import stdin 
N = int(stdin.readline())
miro = list(map(int,stdin.readline().split()))
dp = [N+1]*(N)
#print(miro)
dp[0] = 0
for i in range(N):
    for j in range(1,miro[i]+1):
        if i+j >= N:
            break
        #print(i+j)
        dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[N-1] if dp[N-1] != N+1 else -1)