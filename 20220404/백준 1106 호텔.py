import sys,math
ip = sys.stdin.readline 
C,N = map(int,ip().split())
dp = [math.inf]*(C+100)
# C 명을 늘리기 위해 들여야 하는 돈의 최솟값 
# b 명을 늘리기위 위해 i 번째 도시에서 지불해야하는 Cost 

dp[0] = 0
info = [tuple(map(int,ip().split())) for _ in range(N)]
info.sort()

for cost,people in info:
    for i in range(people, C + 100):
        dp[i] = min(dp[i],dp[i-people] + cost)
print(min(dp[C:]))