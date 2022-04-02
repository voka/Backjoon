
from collections import deque
from itertools import product
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# ? ? ? ? ? ? ? ? ? 
# a a a a a a a a a 
# ...
# c c c c c c c c c 
def solution(grid):
    N,M = len(grid),len(grid[0])
    qcount = 0
    answer = 0
    qindex = []

    Myground = {}

    for i in range(N):
        if 'a' in grid[i]:
            Myground['a'] = 0
        if 'b' in grid[i]:
            Myground['b'] = 0
        if 'c' in grid[i]:
            Myground['c'] = 0
        grid[i] = list(grid[i])

        for j in range(M):
            if grid[i][j] == '?':
                qcount += 1
                qindex.append([i,j])
    testcase = product(['a','b','c'],repeat=qcount)
    pools = [tuple(pool) for pool in testcase]
    for pool in pools:
        new_key = {}
        for key in Myground:
            new_key[key] = 0
        if 'a' not in new_key and  'a' in pool :
            new_key['a'] = 0
        if 'b' not in new_key and 'b' in pool:
            new_key['b'] = 0
        if 'c' not in new_key and 'c' in pool:
            new_key['c'] = 0

        for i in range(qcount):
            grid[qindex[i][0]][qindex[i][1]] = pool[i]

        visited = [[0]*(M) for _ in range(N)]

        def BFS(x,y):
            target = grid[x][y]
            myque = deque()
            myque.append((x,y))
            while myque:
                cur_x,cur_y = myque.popleft()
                for i in range(4):
                    next_x,next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < N and 0 <= next_y < M:
                        if visited[next_x][next_y] == 0 :
                            if grid[next_x][next_y] == target :
                                visited[next_x][next_y] = 1
                                myque.append((next_x,next_y))
        count = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    BFS(i,j)
                    new_key[grid[i][j]] += 1

        cnt = 0
        for key in new_key:
            if new_key[key] == 1:
                continue
            else:
                cnt = -1
                break
        if cnt == 0 : 
            answer += 1

    return answer
