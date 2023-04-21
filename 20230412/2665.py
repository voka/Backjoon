import sys
from collections import deque
ip = sys.stdin.readline
N = int(ip())
maps = []
dp = [[1e9]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    _list = list(map(int, ip().strip()))
    for j in range(N):
        _list[j] = 0 if _list[j] == 1 else 1
    maps.append(_list)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
myque = deque()
dp[0][0] = maps[0][0]
visited[0][0] = 1
myque.append((0, 0))
while myque:
    cx, cy = myque.popleft()
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            cur = dp[cy][cx] + maps[cy][cx]
            if dp[ny][nx] > cur:
                dp[ny][nx] = cur
                myque.append((nx, ny))
print(dp[N-1][N-1])
