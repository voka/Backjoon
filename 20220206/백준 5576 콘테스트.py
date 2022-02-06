import heapq
heap_w = []
heap_k = []

w_a = 0
k_a = 0
for i in range(20):
    if i < 10:
        heapq.heappush(heap_w,int(input()))
    else:
        heapq.heappush(heap_k,int(input()))
for i in range(7):
    heapq.heappop(heap_k)
    heapq.heappop(heap_w)
print(sum(heap_w),sum(heap_k))