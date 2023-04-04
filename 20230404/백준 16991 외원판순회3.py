import sys
import math
ip = sys.stdin.readline
INF = float('inf')
tmps = []
N = int(ip())
maps = [[0]*N for _ in range(N)]
weights = [[0]*(1 << N) for _ in range(N)]
for i in range(N):
    tmps.append(list(map(int, ip().split())))
for i in range(N):
    for j in range(i+1, N):
        cur = math.sqrt((tmps[i][0] - tmps[j][0])**2 +
                        (tmps[i][1] - tmps[j][1]) ** 2)
        maps[i][j] = cur
        maps[j][i] = cur


def TSP(cur, visited):
    if visited == ((1 << N) - 1):  # 모든 점을 방문한 경우 -> 시작점으로 가는 길만 있으면 된다.
        if maps[cur][0] != 0:
            weights[cur][visited] = maps[cur][0]
            return weights[cur][visited]
        else:
            return INF
    c = weights[cur][visited]
    if c != 0:  # 한 번이라도 방문한 경우
        return weights[cur][visited]
    tmp = INF
    for i in range(N):
        if visited & (1 << i):  # 방문한 경우
            continue
        if maps[cur][i] == 0:  # 깅리 없는 경우
            continue
        tmp = min(tmp, TSP(i, visited | (1 << i)) + maps[cur][i])
    weights[cur][visited] = tmp
    return tmp


print(TSP(0, 1))
