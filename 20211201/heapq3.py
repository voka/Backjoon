import heapq
def solution(operations):
    answer = []
    myheap = []
    
    for i in operations:
        Op, num = i.split(" ")
        num = int(num)
        if Op == "I":
            heapq.heappush(myheap,num)
        else:
            if len(myheap) > 0:
                if num == 1:
                    myheap.pop(myheap.index(heapq.nlargest(1,myheap)[0]))
                else:
                    heapq.heappop(myheap)
    
    if(len(myheap) == 0):
        answer = [0,0]
    else:
        answer = [heapq.nlargest(1,myheap)[0], heapq.heappop(myheap)]
    return answer