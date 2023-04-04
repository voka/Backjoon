import sys
ip = sys.stdin.readline
inf = float('inf')
N = int(ip())
maps = []
weights = [[0]*(1 << N) for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, ip().split())))


def TSP(cur, visited):
    c = weights[cur][visited]
    if c != 0:  # 처음 방문하는 곳이 아님
        return weights[cur][visited]
    if visited == ((1 << N) - 1):  # 모든 점을 다 방문 했을 경우
        if maps[cur][0] == 0:  # 이동 불가능한 경로일때
            return inf
        else:
            weights[cur][visited] = maps[cur][0]
            return weights[cur][visited]
    tmp = inf
    for i in range(N):
        if maps[cur][i] == 0:  # 갈 길이 없을때
            continue
        if visited & (1 << i):  # 이미 방문한 점일 경우
            continue
        else:
            tmp = min(tmp, TSP(i, (visited | ((1 << i)))) + maps[cur][i])
    weights[cur][visited] = tmp
    return tmp


print(TSP(0, 1))
