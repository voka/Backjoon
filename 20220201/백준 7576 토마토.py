import sys
from collections import deque

# deque 짱짱 맨 ㅋㅋㅋ
M,N = map(int,sys.stdin.readline().split())
maps = []
dp = [[-1]*(M) for _ in range(N)]
myque = deque()
for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if temp[j] == 1:
            myque.append((i,j))
            dp[i][j] = 0
    maps.append(temp)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 1
while True:
    t = len(myque)
    for _ in range(t):
        cur_x,cur_y = myque.popleft()
        for i in range(4):
            nx,ny = cur_x + dx[i], cur_y + dy[i]
            if (nx < 0) | (nx >= N) | (ny < 0) | (ny >= M) :
                continue
            if (dp[nx][ny] >= 0) | (maps[nx][ny] == 1) | (maps[nx][ny] == -1):
                continue
            dp[nx][ny] = count
            maps[nx][ny]  = 1
            myque.append((nx,ny))
    if len(myque) == 0:
        break
    count += 1

##pprint.pprint(maps)
##pprint.pprint(dp)
answer = -1
for i in range(N):
    if 0 in maps[i]:
        print(-1)
        exit()
    answer = max(answer,max(dp[i]))
print(answer)