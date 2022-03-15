import sys
from collections import deque
ip = sys.stdin.readline 
N,L,R = map(int,ip().split())
maps = [list(map(int,ip().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(sx,sy):
    myque = deque()
    myque.append((sx,sy))
    visited_dict = {}
    visited[sx][sy] = 1
    temp = [(sx,sy)]
    while myque:
        cur_x,cur_y = myque.popleft()
        for i in range(4):
            next_x,next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x > N-1 or next_y > N-1 or visited[next_x][next_y] == 1:
                continue
            diff = abs(maps[next_x][next_y] - maps[cur_x][cur_y])
            if L <= diff <= R:
                visited[next_x][next_y] = 1
                myque.append((next_x,next_y))
                temp.append((next_x,next_y))
    total = 0
    count = len(temp)
    if count > 1:
        for x,y in temp:
            total += maps[x][y]

        if count != 0 : avg = total // count 

        for x,y in temp:
            maps[x][y] = avg

        return count 
    else:
        return 0
    
                

travel = 0
while True:
    flag = 0
    visited = [[0]*(N) for _ in range(N)]
    for i in range(N): #  탐색에서 조건을 만족하는 모든 영역에서 
        for j in range(N):
            if visited[i][j] == 0:
                if BFS(i,j) > 0:
                    flag = 1
    #print(maps)
    if flag == 0 :
        break
    travel += 1
print(travel)

