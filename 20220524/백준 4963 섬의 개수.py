import sys 
from collections import deque
ip = sys.stdin.readline 

dx,dy = [1,1,1,-1,-1,-1,0,0],[0,1,-1,0,1,-1,1,-1]
def BFS(maps,x,y,w,h):
  myque = deque()
  maps[x][y] = 0 
  myque.append((x,y))
  while myque:
    x,y = myque.popleft()
    for i in range(8):
      nx,ny = x+dx[i], y+dy[i]
      if 0 <= nx < h and 0 <= ny < w:
        if maps[nx][ny] == 1:
          maps[nx][ny] = 0
          myque.append((nx,ny))
  return maps
while True:
  w, h = map(int,ip().split())
  if w == 0 and h == 0 :
    break
  maps = []
  for i in range(h):
    temp = list(map(int,ip().split()))
    maps.append(temp)
  count = 0
  for i in range(h):
    for j in range(w):
      if maps[i][j] == 1:
        maps = BFS(maps,i,j,w,h)
        count += 1
  print(count)