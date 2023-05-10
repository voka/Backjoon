import sys
import heapq
ip = sys.stdin.readline
N = int(ip())
works = []
works = [tuple(map(int, ip().split())) for _ in range(N)]
works.sort(key=lambda x: (x[1], x[0]))

myque = []

for p, deadLine in works:
    heapq.heappush(myque, p)
    if deadLine < len(myque):
        heapq.heappop(myque)
print(sum(myque))
