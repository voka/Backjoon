import sys,heapq
N = int(input())
mylist = list(map(int,sys.stdin.readline().split()))
heapq.heapify(mylist)
for i in range(N-1):
    tmp = list(map(int,sys.stdin.readline().split()))
    for t in tmp:
        heapq.heappush(mylist,t)
        heapq.heappop(mylist)
print(min(mylist))