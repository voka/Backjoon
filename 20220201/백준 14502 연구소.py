
import sys
from itertools import combinations,product
from collections import deque
from copy import copy

N,M = map(int,sys.stdin.readline().split())
a = [i for i in range(N)]
b = [i for i in range(M)]
k = [a,b]
product_list = list(product(*(k)))
#print(product_list)
check_list = list(combinations(product_list,3))
#print(len(check_list))
max_size = 0
maps = []
myque = deque()
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if tmp[j] == 2:
            myque.append((i,j))
    maps.append(tmp)
#print(maps)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for cur in check_list:
    f = 1
    for i in cur:
        x,y = i
        if maps[x][y] == 1 or maps[x][y] == 2:
            f = -1
            break
    if f == -1:
        continue
    temp = [copy(maps[i]) for i in range(N) ]
    tmpque = myque.copy()
    #print(tmpque)
    for i in cur:
        x,y = i
        temp[x][y] = 1
    while True:
        if len(tmpque) == 0:
            break
        cx,cy = tmpque.popleft()
        for k in range(4):
            nx,ny = cx + dx[k],cy + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >=M:
                continue
            if temp[nx][ny] == 2 or temp[nx][ny] == 1:
                continue
            temp[nx][ny] = 2 
            tmpque.append((nx,ny))
    mc = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                mc += 1
    max_size = max(max_size,mc)
#print(maps)
print(max_size)