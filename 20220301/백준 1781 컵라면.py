import sys,heapq
ip = sys.stdin.readline
N = int(ip())
studys = []
studys = [tuple(map(int,ip().split())) for _ in range(N)]
studys.sort()

myque = []

for DL,Cup in studys:
    heapq.heappush(myque,Cup)
    if DL < len(myque):
        heapq.heappop(myque)
print(sum(myque)) 
