import sys
sys.setrecursionlimit(10**7)
ip = sys.stdin.readline
N = int(ip())
weights = []
for i in range(N):
    weights.append(list(map(int, ip().split())))
dists = [[-1 for _ in range(1 << N)] for _ in range(N)]


def TSP(cur, visited):
    if visited == ((1 << N) - 1):
        if weights[cur][0] == 0:
            return 1e7
        dists[cur][visited] = weights[cur][0]
        return weights[cur][0]

    c = dists[cur][visited]
    if c != -1:
        return c

    tmp = 1e7
    for i in range(N):
        if weights[cur][i] == 0:  # 길 X
            continue
        if visited & (1 << i):  # 이미 방문
            continue
        tmp = min(tmp, TSP(i, (visited | 1 << i)) + weights[cur][i])
    dists[cur][visited] = tmp
    return tmp


'''
N == 4
10000 -1 
1111
'''
print(TSP(0, 1))
