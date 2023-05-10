import sys
import heapq
ip = sys.stdin.readline
N = int(ip())
line = []
line = [list(map(int, ip().split())) for _ in range(N)]
for i in range(N):
    line[i].sort()
line.sort(key=lambda x: (x[1], x[0]))
min_que = []
cut = int(ip())
answer = 0
for s, e in line:
    if e - s > cut:
        continue
    heapq.heappush(min_que, s)
    while min_que:
        cur_min = heapq.heappop(min_que)
        if e - cur_min <= cut:
            heapq.heappush(min_que, cur_min)
            break
    answer = max(answer, len(min_que))
print(answer)
