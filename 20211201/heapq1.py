from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        cur = heappop(scoville)
        mix = heappop(scoville)
        heappush(scoville, cur + mix*2)
        answer += 1
        if(scoville[0] >= K):
            break
        if(len(scoville) == 1):
            answer = -1
            break
        
    return answer