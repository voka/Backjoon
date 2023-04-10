import sys
import math
ip = sys.stdin.readline
N = int(ip())
maps = []
weights = [[0]*(1 << N) for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, ip().split())))


def TSP(cur, visited):
    if visited == (1 << N)-1:
        return 0
    c = weights[cur][visited]
    if c != 0:  # 한 번이라도 방문한 경우
        return c
    tmp = 0
    for i in range(N):
        if visited & (1 << i):  # 방문한 경우
            continue
        if maps[cur][i] == 0:  # 길이 없는 경우
            continue
        tmp = max(tmp, TSP(i, visited | (1 << i)) + 1)
    weights[cur][visited] = tmp
    return tmp


def backtrace(cur, visited):
    print(cur+1, end=" ")
    for i in range(N):
        if maps[cur][i] and not visited & (1 << i):
            if weights[cur][visited] == weights[i][visited | (1 << i)] + 1:
                backtrace(i, visited | (1 << i))
                break


print(TSP(0, 1) + 1)
backtrace(0, 1)
