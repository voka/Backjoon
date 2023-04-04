from itertools import permutations
import sys
ip = sys.stdin.readline
N = int(ip())
maps = []
for _ in range(N):
    maps.append(list(map(int, ip().split())))
weights = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        weights[i][j] = maps[i][j]
loop = permutations([i for i in range(N)], N)
answer = float('inf')
for _list in loop:
    n = len(_list)
    pre = _list[0]
    tmp = 0
    for i in range(1, n):
        cur = weights[pre][_list[i]]
        if cur == 0:
            break
        tmp += cur
        pre = _list[i]
    if pre != _list[-1]:
        continue
    else:
        cur = weights[pre][_list[0]]  # 시작점으로 돌아오는 것
        if cur != 0 and answer > tmp + cur:
            answer = tmp + cur
print(answer)
