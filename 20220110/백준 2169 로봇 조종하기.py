from sys import stdin 
N,M = map(int,stdin.readline().split())
maps = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    maps[i] = list(map(int,stdin.readline().split()))
    maps[i].insert(0,0)
dp = [[0]*(M+1) for _ in range(N+1)]
check = [[0]*(M+1) for _ in range(N+1)]
dx = [0,-1,1]
dy = [1,0,0]
dp[1][1] = maps[1][1]
for j in range(2,M+1): # 시작을 1,1에서 부터 하므로 첫째줄은 무조건 왼쪽에서 오른쪽으로 진행한다. 
    dp[1][j] = dp[1][j-1] + maps[1][j]
for i in range(2,N+1):
    fromleft = [0]*(M+1)
    fromRight = [0]*(M+1)
    fromleft[1] = dp[i-1][1] + maps[i][1]
    fromRight[M] = dp[i-1][M] + maps[i][M]
    for j in range(2,M+1): # 왼쪽에서 오는 경우
        fromleft[j] = max(dp[i-1][j],fromleft[j-1])+maps[i][j] # 위쪽에서 오는 값과 왼쪽에서 오는 값 비교 
    
    for j in range(M-1,0,-1): # 오른쪽에서 오는 경우
        fromRight[j] = max(dp[i-1][j],fromRight[j+1])+maps[i][j] # 위쪽에서 오는 값과 왼쪽에서 오는 값 비교 
    for j in range(1,M+1):
        dp[i][j] = max(fromleft[j],fromRight[j]) # 왼쪽값 오른쪽값 비교

print(dp[N][M])
    
    
# 처음에는 큐로 풀어보려고 했다가 정답이 요상하게 나와서 구글링을 했습니다..
