import sys
from collections import deque
ip = sys.stdin.readline
N, M = map(int, ip().split())
maps = [list(ip().strip()) for _ in range(N)]
myque = deque()
myque.append((0, 0, 1))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[0]*(M) for _ in range(N)]
dp[0][0] = 1
flag = False
while myque:
    cx, cy, c = myque.popleft()
    if c > N * M:
        flag = True
        break
    mul = int(maps[cy][cx])
    for i in range(4):
        nx, ny = cx + dx[i]*mul, cy + dy[i]*mul
        if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] != 'H':
            if dp[ny][nx] < c+1:
                dp[ny][nx] = c + 1
                myque.append((nx, ny, c+1))
if flag:
    print(-1)
else:
    answer = 0
    for i in dp:
        answer = max(answer, max(i))
    print(answer)
