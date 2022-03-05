import heapq
pq = []
for i in range(99,0,-11):
    heapq.heappush(pq,(i%2,(i+1)%2,-i))

while pq:
    cur = heapq.heappop(pq)
    print(cur)

