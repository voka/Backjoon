import sys
from collections import deque
ip = sys.stdin.readline
N,K = map(int,ip().split())
lst = list(map(int,ip().split()))
answer = 0
cur_muti = []
for i in range(K):
    cur = lst[i]
    # 1. 이미 멀티탭에 있는 경우 PASS
    if cur in cur_muti:
        continue
    elif len(cur_muti) < N:
        cur_muti.append(cur)
    else: # 3. 빈 자리가 없는 경우 가장 늦게 사용되는 거 뽑기 
        cur_ = [1001]*N # 가장 늦게 사용되는 거 초기화 
        for j in range(i+1,K): # 남은 사용순서에서 
            for d in range(N): # 현재 멀티탭 수만큼 반복하면서 
                if lst[j] == cur_muti[d]: #멀티탭에 있는게 다시 사용되는 
                    cur_[d] = min(j,cur_[d]) # 최소 순서를 찾는다.
        change_id = -1 # 멀티탭에서 뽑을 인덱스
        cur_max = -99  # 가장 늦게 사용할 것 
        for j in range(N):
            if cur_max < cur_[j]:
                change_id = j
                cur_max = cur_[j]
        answer += 1 # 뽑은 횟수를 증가시키고
        cur_muti[change_id] = cur # 현재 사용해야할 전기도구를 멀티탭에 꽂는다. 
    
print(answer)     
    