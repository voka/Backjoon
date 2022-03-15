import sys
from collections import deque
ip = sys.stdin.readline
N = int(ip())
maps1 = []
maps2 = []
for i in range(N):
    tmp = ip().rstrip()
    maps1.append(list(tmp))
    maps2.append(list(tmp.replace('G','R')))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(maps,sx,sy):
    color = maps[sx][sy]
    myque = deque()
    myque.append((sx,sy))
    visited[sx][sy] = 1
    while myque:
        cur_x,cur_y = myque.popleft()
        for i in range(4):
            next_x,next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_x > N-1 or next_y < 0 or next_y > N-1:
                continue
            if visited[next_x][next_y] == 1:
                continue
            if maps[next_x][next_y] == color:
                visited[next_x][next_y]  = 1
                myque.append((next_x,next_y))    

visited = [[0]*N for _ in range(N)]
c1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(maps1,i,j)
            c1 += 1

visited = [[0]*N for _ in range(N)]

c2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(maps2,i,j)
            c2 += 1

print(c1,c2)