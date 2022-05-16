import sys,pprint
from collections import deque
ip = sys.stdin.readline 
M,N,K = map(int, ip().split())
maps = [[0]*N for _ in range(M)]
for i in range(K):
  x1,y1,x2,y2 = map(int, ip().split())
  for y in range(y1,y2):
    for x in range(x1,x2):
      maps[y][x] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(x,y):
  myque = deque()
  myque.append((x,y))
  maps[y][x] = 1 
  total = 1
  while myque:
    cur_x, cur_y = myque.popleft()
    for i in range(4):
      nx,ny = cur_x+dx[i], cur_y+dy[i]
      if 0<=nx<N and 0<=ny<M:
        if maps[ny][nx] == 0:
          maps[ny][nx] = 1
          myque.append((nx,ny))
          total += 1
  return total 

answer = 0
answer_map = []
for i in range(M):
  for j in range(N):
    if maps[i][j] != 1:
      answer_map.append(BFS(j,i))
      answer += 1
print(answer)
answer_map.sort()
print(*answer_map)
  
