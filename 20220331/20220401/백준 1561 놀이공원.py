import sys, heapq
ip = sys.stdin.readline
N,M = map(int,ip().split())
lst = list(map(int,ip().split()))
temp = []
for i in range(M):
    heapq.heappush(temp,(0,i+1))
for i in range(N):
    time, num  = heapq.heappop(temp)
    if i == N-1:
        print(num)
        break
    next_time = time + lst[num-1]
    heapq.heappush(temp, (next_time,num))
    



