import sys
from collections import deque
# 직관적이고 좋은 풓이 !! -> 출처 : https://www.acmicpc.net/source/38577816
durumary = deque(sys.stdin.readline().strip())
angel = deque(sys.stdin.readline().strip())
devil = deque(sys.stdin.readline().strip())
goal = len(durumary)
N = len(angel)
dpD = [[0 for j in range(N)] for _ in range(goal)]
dpA = [[0 for j in range(N)] for _ in range(goal)]

for i in range(N):
    if devil[i] == durumary[0]:
        dpD[0][i] = 1
    if angel[i] == durumary[0]:
        dpA[0][i] = 1
for d in range(1,goal):
    for j in range(1,N):
        if devil[j] == durumary[d]:
            for t in range(j):
                dpD[d][j] += dpA[d-1][t]
        if angel[j] == durumary[d]:
            for t in range(j):
                dpA[d][j] += dpD[d-1][t]
print(sum(dpA[-1]) + sum(dpD[-1]))

