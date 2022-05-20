import sys,pprint
from collections import deque
ip = sys.stdin.readline 
N = int(ip())
maps = []
MAX_H = -1
for i in range(N):
  temp = list(map(int,ip().split()))
  MAX_H = max(MAX_H,max(temp))
  maps.append(temp)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(x,y,visited):
  myque = deque()
  myque.append((x,y))
  visited[x][y] = 1 
  while myque:
    cur_x, cur_y = myque.popleft()
    for i in range(4):
      nx,ny = cur_x+dx[i], cur_y+dy[i]
      if 0<=nx<N and 0<=ny<N:
        if visited[nx][ny] == 0:
          visited[nx][ny] = 1
          myque.append((nx,ny))
  return visited
def Fill(num):
  visited = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      visited[i][j] = 1 if maps[i][j] <= num else 0
  return visited
answer = 0
for T in range(MAX_H+1):
  cur = 0
  visited = Fill(T)
  for i in range(N):
    for j in range(N):
      if visited[i][j] != 1:
        visited = BFS(i,j,visited)
        #pprint.pprint(visited)
        #print("--------------------------------------------\n")
        cur += 1
  #print(T,cur)
  answer = max(answer,cur)
print(answer)
  
