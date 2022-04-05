import sys 
from itertools import permutations
ip = sys.stdin.readline 
N = int(ip())
pt = permutations([i for i in range(1,N+1)])
for p in pt:
    print(*p)