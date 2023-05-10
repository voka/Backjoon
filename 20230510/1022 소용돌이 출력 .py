import sys
from collections import deque
ip = sys.stdin.readline
r1, c1, r2, c2 = map(int, ip().split())

maps = [[-1]*(50) for _ in range(5)]
