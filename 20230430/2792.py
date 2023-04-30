import sys
import math
ip = sys.stdin.readline
N, M = map(int, ip().split())
_list = [int(ip()) for _ in range(M)]


def solve(mid):
    k = float('inf')
    cnt = 0
    for m in _list:
        cnt += math.ceil(m/mid)
    if cnt <= N:
        return True
    else:
        return False


start, end = 1, 10**9
while start <= end:
    mid = (start+end)//2
    if solve(mid):
        end = mid - 1
    else:
        start = mid + 1
print(start)
