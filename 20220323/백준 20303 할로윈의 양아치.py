import sys
ip = sys.stdin.readline
N,M,K = map(int,ip().split())

parent = [i for i in range(N+1)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


candys = list(map(int,ip().split()))
candys.insert(0,0)

nums = [1 for i in range(N+1)]

for i in range(M):
    a,b = map(int,ip().split())
    union_parent(a,b)
        
for i in range(1,N+1):
    if i != parent[i]:
        p = find_parent(i)
        candys[p] += candys[i]
        nums[p] += nums[i]
        
dp = [0]*K
for i in range(1,N+1):
    if i != parent[i]:
        continue
    for j in range(K-1,nums[i]-1,-1):
        dp[j] = max(dp[j],dp[j-nums[i]]+candys[i])
print(dp[K-1])