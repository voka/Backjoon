from collections import deque
import sys
ip = sys.stdin.readline
N = int(ip())
maps = [list(map(int, ip().split())) for _ in range(N)]
'''
dp 초기상태
0 1 0
0 0 0
0 0 0

0 1 0
0 0 1
0 0 1

0 1 0 0
0 0 0 0
0 0 0 0
0 0 0 0

0 1 1 0
0 0 1 0
0 0 0 0
0 0 0 0

0 1 1 0
0 0 1 1
0 0 1 2
0 0 0 0

0 1 1 0
0 0 1 1
0 0 1 2
0 0 0 3



'''
# dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]  # x,y 방향
# myque = deque()
# myque.append((2, 1, 0))
# my_dict = {}
# while myque:
#     cx, cy, dir = myque.popleft()  # x, y 방향
#     dp[cy][cx][dir] += 1  # 나온 횟수 만큼 + 1
#     nx, ny = cx + 1, cy + 1
#     if (dir == 0 or dir == 2) and nx <= N and maps[cy-1][nx-1] == 0:  # 가로로
#         myque.append((nx, cy, 0))
#     if (dir == 1 or dir == 2) and ny <= N and maps[ny-1][cx-1] == 0:  # 세로로
#         myque.append((cx, ny, 1))
#     if nx <= N and ny <= N and maps[ny-1][nx-1] == 0 and maps[ny-1][cx-1] == 0 and maps[cy-1][nx-1] == 0:  # 대각선
#         myque.append((nx, ny, 2))
# print(sum(dp[N][N]))
result = 0


def dfs(cx, cy, dir):
    global result
    if cx == N and cy == N:
        result += 1
    nx, ny = cx + 1, cy + 1
    if (dir == 0 or dir == 2) and nx <= N and maps[cy-1][nx-1] == 0:  # 가로로
        dfs(nx, cy, 0)
    if (dir == 1 or dir == 2) and ny <= N and maps[ny-1][cx-1] == 0:  # 세로로
        dfs(cx, ny, 1)
    if nx <= N and ny <= N and maps[ny-1][nx-1] == 0 and maps[ny-1][cx-1] == 0 and maps[cy-1][nx-1] == 0:  # 대각선
        dfs(nx, ny, 2)


if maps[N-1][N-1] == 1:
    print(0)
else:
    dfs(2, 1, 0)
    print(result)
