import sys,pprint
from collections import deque
sys.setrecursionlimit(10 ** 4)
ip = sys.stdin.readline 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N,M = map(int,ip().split())
maps = [list(map(int,ip().split())) for _ in range(N)]
def BFS(x,y):
    myque = deque()
    myque.append((x,y))
    while myque:
        cur_x,cur_y = myque.popleft()
        cnt = 0
        for i in range(4):
            next_x, next_y = cur_x + dx[i] , cur_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and visited[next_x][next_y] == 0 :
                if maps[next_x][next_y] == 0:
                    cnt += 1
                else:
                    visited[next_x][next_y] = 1 ## 큐에 삽입되기 전에 방문체크를 해야 메모리 초과가 나지 않음 ==> 방문했던 곳을 다시 방문하지 않음. 
                    myque.append((next_x,next_y))
        maps[cur_x][cur_y] = max(0,maps[cur_x][cur_y] - cnt)        
answer = -1           
while True:
    visited = [[0]*M for _ in range(N)]
    c = 0;
    #pprint.pprint(maps)
    for i in range(N-1):
        for j in range(M-1):
            if maps[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                BFS(i,j)
                c += 1
    #pprint.pprint(visited)
    #pprint.pprint(maps)
    #print("C : ", c)
    answer += 1
    if c > 1:
        break
    elif c == 0:
        answer = 0
        break
print(answer)
