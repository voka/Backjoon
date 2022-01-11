from sys import stdin 
N = int(stdin.readline())
lines = []
for i in range(N):
    lines.append(int(stdin.readline()))
dp = [1]*(N)
for i in range(N):
    for j in range(i):
        if lines[i] > lines[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(N - max(dp))
