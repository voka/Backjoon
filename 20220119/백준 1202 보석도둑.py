from sys import stdin 
from queue import PriorityQueue
import heapq
N,K = map(int,stdin.readline().split())
bags = [0]*(K)
jewelrys = []
for i in range(N):
    jewelrys.append(tuple(map(int,stdin.readline().split())))
#print(jewelrys)
for i in range(K):
    bags[i] = int(stdin.readline())
used = [0]*(N)
bags.sort() # 무게가 가벼운 순 
jewelrys = sorted(jewelrys, key = lambda x : (-x[0],x[1])) # 무게가 가볍고 가격이 비싼 순서대로 
#print(jewelrys)
answer,hq = 0,[]
# 우선순위 큐 사용하면 시간초과 남 ... heapq 쓰면 통과함 .. -->  heapq는 우선순위 큐보다 좋음 -> List 형태로 되어 있어서 정렬 상태를 print로 확인 가능 !!! 
myque = PriorityQueue()
for flag in bags:
    while jewelrys:
        w,v = jewelrys.pop() # 맨 오른쪽거 부터 꺼낸다 
        if w > flag:
            jewelrys.append((w,v))
            break
        #print(w,v)
        heapq.heappush(hq,(-v,w))
    if hq:
        v,w = heapq.heappop(hq)
        #print(w,v)
        if w > flag:
            heapq.heappush(hq,(v,w))
            continue
        answer += -v

print(answer)
    """
    while True:
        if idx == N or flag < jewelrys[idx][0]:
            break
        else:
            if used[idx] == 0:
                #print("큐에 들어가는 보석 가치 : " , jewelrys[idx][1])
                myque.put(-jewelrys[idx][1])
                used[idx] = 1
        idx += 1
    
    if not myque.empty():
        #print("큐에서 나오는 보석 가치 : " ,Q)
        answer += -myque.get()
    """
        
        
    
# 이분탐색 --> 시간 초과
"""
def lower_bound(k):
    l = 0
    r = K
    while l < r:
        m = (l+r)//2
        if bags[m] >= k:
            r = m
        else:
            l = m + 1
    return l

#print(bags)
#print(jewelrys)
for m,v in jewelrys:
    b_i = lower_bound(m) 
    #print(b_i)
    if b_i == -1 or b_i >= K:
        continue
    if used[b_i] == 0:
        steals[b_i] = v
        used[b_i] = 1
    else:
        if min(used[b_i : K]) != 0:
            continue
        next_i = b_i + 1
        while True:
            if next_i == K:
                break
            else:
                #print(next_i,steals[next_i],v)
                if steals[next_i] < v:
                    steals[next_i] = v
                    used[next_i] = 1
                    break
            next_i += 1
"""
    