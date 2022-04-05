import sys
from itertools import permutations
ip = sys.stdin.readline 
N = int(ip())
lst = list(map(int,ip().split()))
pt = permutations(lst)
answer = -1
for p in pt:
    tmp = 0
    for i in range(1,N):
        tmp += abs(p[i] - p[i-1])
    answer = max(tmp,answer)
print(answer)