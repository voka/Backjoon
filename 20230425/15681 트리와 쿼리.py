import sys
sys.setrecursionlimit(10**5)
ip = sys.stdin.readline
n, r, q = map(int, ip().split())
grahp = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, ip().split())
    grahp[a].append(b)
    grahp[b].append(a)
tree = [1]*(n+1)
visited = [0]*(n+1)


def make_tree(idx):
    visited[idx] = 1
    for child in grahp[idx]:
        if visited[child] == 1:
            continue
        make_tree(child)  # 자식 노드들이 먼저 자기가 root인 트리의 사이즈를 측정
        tree[idx] += tree[child]  # 그 다음 부모 사이즈에 더하기


make_tree(r)

for _ in range(q):
    node = int(ip())
    print(tree[node])
