import sys
ip = sys.stdin.readline
sys.setrecursionlimit(10**5)


def solution():
    n = int(ip())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, ip().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n+1)
    depth = [0]*(n+1)
    p = [-1]*(n+1)

    def get_depth_with_parent(x, count):
        visited[x] = 1
        depth[x] = count
        for a in graph[x]:
            if visited[a] == 0:
                p[a] = x
                get_depth_with_parent(a, count+1)
    get_depth_with_parent(1, 1)
    m = int(ip())
    for _ in range(m):
        n1, n2 = map(int, ip().split())
        while depth[n1] != depth[n2]:
            if depth[n1] > depth[n2]:
                n1 = p[n1]
            else:
                n2 = p[n2]
        while (n1 != n2):
            n1 = p[n1]
            n2 = p[n2]
        print(n1)


solution()
