from sys import stdin 

N = int(stdin.readline())
cards = list(map(int,stdin.readline().split()))
dp = [max(cards)]*(N+1)
for i in range(1,N+1):
    dp[i] = cards[i-1]
    for j in range(1,i+1):
        dp[i] = min(dp[i],cards[j-1] + dp[i-j])
print(dp[N])