import sys
ip = sys.stdin.readline

V,E = map(int,ip().split())
parents = [i for i in range(V+1)]
Edges = []
def Find_P(a):
    if parents[a] != a:
        parents[a] = Find_P(parents[a])
    return parents[a]

def union_P(a,b):
    a = Find_P(a)
    b = Find_P(b)
    if a < b: # 큰 놈이 작은 놈을 가리키게 하던 작은 놈이 큰 놈을 가리키게 하던 똑같다.
        parents[b] = a
    else:
        parents[a] = b

for _ in range(E):
    a,b,w = map(int,ip().split())
    Edges.append((w,a,b))
Edges.sort()
answer = 0
max_w = 0
for e in Edges:
    w,a,b, = e
    if Find_P(a) != Find_P(b):
        union_P(a,b)
        answer += w
        max_w = max(max_w,w)
print(answer - max_w)
