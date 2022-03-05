import sys,math
ip = sys.stdin.readline
V = E = int(ip())
parents = [i for i in range(V+1)]
def find_p(x):
    if parents[x] != x:
        parents[x] = find_p(parents[x])
    return parents[x]

def union_p(a,b):
    a = find_p(a)
    b = find_p(b)   
    if a < b :
        parents[a] = b
    else:
        parents[b] = a

def dist(f,s):
    x = f[0]-s[0]
    y = f[1]-s[1]
    if x == 0 and y == 0:
        return 0
    else:
        return math.sqrt(x**2 + y**2)

edges = []
stars = [tuple(map(float,ip().split())) for _ in range(V)]
stars.insert(0,(0,0))
for i in range(1,V+1):
    for j in range(i+1,V+1):
        edges.append((dist(stars[i],stars[j]),i,j))
edges.sort()
answer = 0
for e in edges:
    w,a,b = e
    if find_p(a) != find_p(b):
        union_p(a,b)
        answer += w
print("{0:.2f}".format(answer))